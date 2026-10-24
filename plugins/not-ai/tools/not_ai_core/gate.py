"""Small dependency-free Not Ai editorial gate for portable installations."""
from __future__ import annotations
from dataclasses import asdict, dataclass
import json, re, unicodedata

POLICIES = {
    "linkedin","personal","email","social","x","fiction","readme","technical",
    "procedure","api","tutorial","student","academic","abstract","proposal",
    "executive","marketing","essay",
}
PROTECTED_RE = re.compile(r"\[[^\]\n]{1,80}\]")
WORD_RE = re.compile(r"\b[A-Za-z]+(?:'[A-Za-z]+)?\b")
PATTERNS = {
    "template-transition": re.compile(r"\b(?:furthermore|moreover|additionally|in conclusion|to summarize)\b",re.I),
    "empty-frame": re.compile(r"\b(?:it is (?:worth|important) to note that|in today's fast-paced world)\b",re.I),
    "copula-avoidance": re.compile(r"\b(?:serves as|stands as|functions as|operates as|marks a)\b",re.I),
    "negative-parallelism": re.compile(r"\bnot just\b[^.!?]{0,80}\bbut\b",re.I),
    "nominalization-density": re.compile(r"\b\w+(?:tion|sion|ment|ness|ance|ence|ity|ization)\b",re.I),
}
TIER1 = {"camaraderie","tapestry","palpable","intricate","vibrant","cacophony","solace","fleeting","ignite","unravel","grapple","amidst","unspoken","underscore","unease","pang","waft","prioritize"}
TIER2 = {"delve","leverage","utilize","facilitate","comprehensive","robust","seamless","pivotal","foster","meticulous","nuanced","multifaceted","transformative","groundbreaking","empower","synergy","holistic","dynamic","impactful","landscape","realm","revolutionize","harness","unlock","elevate","garner","showcase","bolster","interplay","testament","boasts","enhance","crucial","enduring","valuable"}
@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    message: str
    span: str|None=None
@dataclass(frozen=True)
class Result:
    genre: str
    word_count: int
    passed: bool
    findings: list[Finding]
    def as_dict(self):
        return {"genre":self.genre,"word_count":self.word_count,"passed":self.passed,"findings":[asdict(x) for x in self.findings]}
def scan_unicode(text: str):
    findings=[]
    for i,ch in enumerate(text):
        cp=ord(ch)
        category=unicodedata.category(ch)
        if cp in (0x200B,0x2060,0xFEFF,0x00AD) or cp in (0x200C,0x200D) or 0x202A<=cp<=0x202E or 0x2066<=cp<=0x2069 or 0xE0000<=cp<=0xE007F or (category=="Zs" and ch!=" "):
            findings.append({"index":i,"codepoint":f"U+{cp:04X}","name":unicodedata.name(ch,"UNKNOWN")})
    return findings
def evaluate(text: str, genre="linkedin", protected_terms=(), ascii_punctuation=False):
    if genre not in POLICIES: raise ValueError(f"Unknown genre {genre}. Choose one of: {', '.join(sorted(POLICIES))}")
    findings=[]
    if not text.strip(): findings.append(Finding("nonempty","error","Output is empty."))
    for required in protected_terms:
        if required not in text: findings.append(Finding("protected-content","error",f"Required literal is missing: {required!r}"))
    u=scan_unicode(text)
    if u: findings.append(Finding("unicode-hygiene","advisory",f"Found {len(u)} invisible or unusual Unicode control(s); inspect before trusting text metrics."))
    prose=re.sub(r"```.*?```"," [code block] ",text,flags=re.S)
    prose=re.sub(r"`[^`\n]+`"," [code] ",prose)
    prose=re.sub(r"(?m)^\s*>\s?","",prose)
    for rule,pattern in PATTERNS.items():
        spans=list(pattern.finditer(prose))
        if spans:
            findings.append(Finding(rule,"advisory",f"Review {len(spans)} occurrence(s) of this pattern in context.",spans[0].group(0)))
    words=[w.lower() for w in WORD_RE.findall(prose)]
    for vocab,rule in ((TIER1,"tier-1-vocabulary"),(TIER2,"tier-2-vocabulary")):
        hits=[w for w in words if w in vocab]
        if hits: findings.append(Finding(rule,"advisory",f"Review corpus-associated wording only where context warrants it.",", ".join(sorted(set(hits)))))
    if ascii_punctuation and any(c in text for c in "—–“”‘’"):
        findings.append(Finding("typography","advisory","Non-ASCII punctuation found under requested ASCII house style."))
    passed=not any(f.severity=="error" for f in findings)
    return Result(genre,len(WORD_RE.findall(prose)),passed,findings)
def render(result, as_json=False):
    if as_json: return json.dumps(result.as_dict(),ensure_ascii=False,indent=2)
    lines=[f"Genre: {result.genre}",f"Words: {result.word_count}",f"Passed: {str(result.passed).lower()}"]
    lines += [f"[{f.severity}] {f.rule}: {f.message}"+(f" | {f.span}" if f.span else "") for f in result.findings]
    return "\n".join(lines)
