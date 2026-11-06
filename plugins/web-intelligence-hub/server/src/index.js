import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { chromium } from 'playwright';

const env = process.env;
const server = new Server({ name: 'web-intelligence-hub', version: '0.1.0' }, { capabilities: { tools: {} } });
let browser, page;
const configured = () => ({
  tavily: !!env.TAVILY_API_KEY, exa: !!env.EXA_API_KEY,
  jina: true, crawl4ai: !!env.CRAWL4AI_BASE_URL,
  playwright: true, browserless: !!env.BROWSERLESS_URL,
  brightdata: !!(env.BRIGHTDATA_API_TOKEN && env.BRIGHTDATA_ZONE)
});
const json = async (url, options={}) => { const r=await fetch(url,{...options,headers:{'content-type':'application/json',...(options.headers||{})}}); const t=await r.text(); if(!r.ok) throw new Error(`${r.status} ${r.statusText}: ${t.slice(0,500)}`); try{return JSON.parse(t)}catch{return {text:t}} };
const text = (s) => ({ content:[{type:'text',text:typeof s==='string'?s:JSON.stringify(s,null,2)}] });
const tools = [
 {name:'web_search',description:'Search the web using configured Tavily and Exa providers with automatic fallback and URL deduplication.',inputSchema:{type:'object',properties:{query:{type:'string'},limit:{type:'integer',minimum:1,maximum:20},mode:{type:'string',enum:['automatic','compare']}},required:['query']}},
 {name:'web_scrape',description:'Extract readable Markdown from a URL using Jina, Crawl4AI, then Bright Data fallback.',inputSchema:{type:'object',properties:{url:{type:'string'},formats:{type:'array',items:{type:'string'} }},required:['url']}},
 {name:'web_crawl',description:'Crawl a bounded set of pages using a configured Crawl4AI service.',inputSchema:{type:'object',properties:{url:{type:'string'},maxPages:{type:'integer',minimum:1,maximum:30}},required:['url']}},
 {name:'browser_navigate',description:'Open a URL in a user-authorized Playwright browser session.',inputSchema:{type:'object',properties:{url:{type:'string'}},required:['url']}},
 {name:'browser_click',description:'Click a visible element using a Playwright text or CSS selector.',inputSchema:{type:'object',properties:{selector:{type:'string'}},required:['selector']}},
 {name:'browser_type',description:'Type text into a field selected by CSS selector. Does not submit forms.',inputSchema:{type:'object',properties:{selector:{type:'string'},value:{type:'string'}},required:['selector','value']}},
 {name:'browser_snapshot',description:'Return current page title, URL and readable body text.',inputSchema:{type:'object',properties:{}}},
 {name:'browser_close',description:'Close the current browser session.',inputSchema:{type:'object',properties:{}}},
 {name:'provider_status',description:'Show configured provider availability without exposing credentials.',inputSchema:{type:'object',properties:{}}}
];
server.setRequestHandler(ListToolsRequestSchema, async()=>({tools}));

async function searchTavily(query,limit){
 const d=await json('https://api.tavily.com/search',{method:'POST',body:JSON.stringify({api_key:env.TAVILY_API_KEY,query,max_results:limit,search_depth:'advanced',include_answer:true})});
 return {provider:'tavily',answer:d.answer||null,results:(d.results||[]).map(x=>({title:x.title,url:x.url,content:x.content,score:x.score}))};
}
async function searchExa(query,limit){
 const d=await json('https://api.exa.ai/search',{method:'POST',headers:{'x-api-key':env.EXA_API_KEY},body:JSON.stringify({query,numResults:limit,type:'auto',contents:{text:{maxCharacters:3000}}})});
 return {provider:'exa',results:(d.results||[]).map(x=>({title:x.title,url:x.url,content:x.text,score:x.score}))};
}
async function scrapeJina(url){
 const r=await fetch('https://r.jina.ai/'+url,{headers:{...(env.JINA_API_KEY?{Authorization:`Bearer ${env.JINA_API_KEY}`}:{})}}); const t=await r.text(); if(!r.ok) throw new Error(`Jina ${r.status}: ${t.slice(0,300)}`); return {provider:'jina',url,content:t};
}
async function scrapeCrawl(url){ const base=(env.CRAWL4AI_BASE_URL||'').replace(/\/$/,''); if(!base) throw new Error('CRAWL4AI_BASE_URL not configured'); const d=await json(base+'/crawl',{method:'POST',body:JSON.stringify({urls:[url],word_count_threshold:50,exclude_external_links:true})}); return {provider:'crawl4ai',url,content:JSON.stringify(d)}; }
async function scrapeBright(url){ if(!configured().brightdata) throw new Error('Bright Data not configured'); const r=await fetch(env.BRIGHTDATA_UNLOCKER_URL||'https://api.brightdata.com/request',{method:'POST',headers:{Authorization:`Bearer ${env.BRIGHTDATA_API_TOKEN}`,'Content-Type':'application/json'},body:JSON.stringify({zone:env.BRIGHTDATA_ZONE,url,format:'raw'})}); const t=await r.text(); if(!r.ok) throw new Error(`Bright Data ${r.status}: ${t.slice(0,300)}`); return {provider:'brightdata',url,content:t}; }
async function getBrowser(){ if(browser && page) return page; if(env.BROWSERLESS_URL){browser=await chromium.connectOverCDP(env.BROWSERLESS_URL);} else {browser=await chromium.launch({headless:env.BROWSER_HEADLESS!=='false'});} const ctx=browser.contexts()[0]||await browser.newContext(); page=ctx.pages()[0]||await ctx.newPage(); return page; }
server.setRequestHandler(CallToolRequestSchema, async(req)=>{
 const a=req.params.arguments||{}; try {
  switch(req.params.name){
   case 'provider_status': return text(configured());
   case 'web_search': {
    const limit=Math.min(20,Math.max(1,a.limit||8)), mode=a.mode||'automatic', attempts=[]; const out=[];
    if(env.TAVILY_API_KEY){try{out.push(await searchTavily(a.query,limit));}catch(e){attempts.push({provider:'tavily',error:e.message});}}
    if((mode==='compare'||!out.length)&&env.EXA_API_KEY){try{out.push(await searchExa(a.query,limit));}catch(e){attempts.push({provider:'exa',error:e.message});}}
    if(!out.length) throw new Error(`No search provider succeeded. Configure TAVILY_API_KEY or EXA_API_KEY. ${JSON.stringify(attempts)}`);
    const seen=new Set(), results=[]; for(const batch of out) for(const item of batch.results||[]){const u=(item.url||'').split('#')[0]; if(u&&!seen.has(u)){seen.add(u);results.push({...item,source:batch.provider});}}
    return text({query:a.query,providers:out.map(x=>x.provider),answer:out.find(x=>x.answer)?.answer||null,results:results.slice(0,limit* (mode==='compare'?2:1)),providerErrors:attempts});
   }
   case 'web_scrape': {
    const errors=[]; for(const fn of [scrapeJina,scrapeCrawl,scrapeBright]){try{return text(await fn(a.url));}catch(e){errors.push(e.message);}} throw new Error('All extraction providers failed: '+errors.join(' | '));
   }
   case 'web_crawl': { const base=(env.CRAWL4AI_BASE_URL||'').replace(/\/$/,''); if(!base) throw new Error('CRAWL4AI_BASE_URL not configured. Start a Crawl4AI service and set its URL.'); const d=await json(base+'/crawl',{method:'POST',body:JSON.stringify({urls:[a.url],crawler_config:{type:'CrawlerRunConfig'},browser_config:{type:'BrowserConfig'},max_pages:Math.min(30,a.maxPages||10)})}); return text({provider:'crawl4ai',data:d}); }
   case 'browser_navigate': { const p=await getBrowser(); await p.goto(a.url,{waitUntil:'domcontentloaded',timeout:45000}); return text({url:p.url(),title:await p.title(),text:(await p.locator('body').innerText({timeout:10000})).slice(0,12000)}); }
   case 'browser_click': { if(!page) throw new Error('No browser page. Call browser_navigate first.'); await page.locator(a.selector).first().click({timeout:10000}); return text({url:page.url(),title:await page.title()}); }
   case 'browser_type': { if(!page) throw new Error('No browser page. Call browser_navigate first.'); await page.locator(a.selector).first().fill(a.value,{timeout:10000}); return text({typed:true,selector:a.selector}); }
   case 'browser_snapshot': { if(!page) throw new Error('No browser page. Call browser_navigate first.'); return text({url:page.url(),title:await page.title(),text:(await page.locator('body').innerText()).slice(0,16000)}); }
   case 'browser_close': { if(browser) await browser.close(); browser=null; page=null; return text({closed:true}); }
   default: throw new Error('Unknown tool: '+req.params.name);
  }
 } catch(e){ return {isError:true,content:[{type:'text',text:e.message}]}; }
});
const transport=new StdioServerTransport(); await server.connect(transport);
