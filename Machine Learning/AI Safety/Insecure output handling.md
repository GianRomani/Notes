Created: 2024-01-21 18:50
#note
Insecure output handling is where an LLM's output is not sufficiently validated or sanitized before being passed to other systems. This can effectively provide users indirect access to additional functionality, potentially facilitating a wide range of vulnerabilities, including [XSS](https://portswigger.net/web-security/cross-site-scripting) ([[Fraudulent Scam by Unknown Remote Attacker]]) and [CSRF](https://portswigger.net/web-security/csrf).

For example, an LLM might not sanitize JavaScript in its responses. In this case, an attacker could potentially cause the LLM to return a JavaScript payload using a crafted prompt, resulting in XSS when the payload is parsed by the victim's browser.

## References
1. [Portswigger](https://portswigger.net/web-security/llm-attacks)
