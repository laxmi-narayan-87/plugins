---
name: cookie-debugging
description: Use when diagnosing browser cookie behavior, login/session persistence, SameSite or Secure attributes, domain/path scope, and authentication flows in Chrome.
---

# Cookie and session troubleshooting

1. Identify the precise symptom and the page/origin involved. Reproduce only in a user-authorized test account or non-sensitive environment where possible.
2. Inspect relevant requests using `list_network_requests` and `get_network_request`; compare request/response headers and redirect hops without copying secret values into notes or the final response.
3. Check whether a cookie is set, sent, or rejected; consider domain/path, expiration, Secure, SameSite, third-party cookie restrictions, redirect origin changes, and credentialed CORS behavior.
4. Correlate the browser console and network evidence. Verify the server's `Set-Cookie` response and subsequent request behavior rather than assuming a frontend-only problem.
5. Recommend the smallest appropriate change and re-test login/session continuity. Redact cookie values, authorization headers, personal identifiers, and tokens in all outputs.

Never harvest or disclose session cookies. Do not copy secrets from browser storage into chat or files. This workflow is for authorized debugging, not session theft or authentication bypass. Reference: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/cookie-debugging/SKILL.md.
