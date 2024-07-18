Created: 2024-01-21 18:50
#note
One of the [[Vulnerabilities in LLM-base applications]].

Insecure output handling is where an [[Large Language Models (LLMs)]]'s output is not sufficiently validated or sanitized before being passed to other systems. This can effectively provide users indirect access to additional functionality, potentially facilitating a wide range of vulnerabilities, including [XSS](https://portswigger.net/web-security/cross-site-scripting) ([[Fraudulent Scam by Unknown Remote Attacker]]) and [CSRF](https://portswigger.net/web-security/csrf).

For example, an LLM might not sanitize JavaScript in its responses. In this case, an attacker could potentially cause the LLM to return a JavaScript payload using a crafted prompt, resulting in XSS when the payload is parsed by the victim's browser.

Mitigation measures:
- **Restrict LLM Access:** Enforce strict privilege controls on LLM access to backend systems. Provide the LLM with its own API tokens for extensible functionality (plugins, data access, etc.), adhering to the principle of least privilege. Limit the LLM's access to only what is essential for its intended operations.
- **Human-in-the-Loop:** For extended functionality and privileged operations (such as sending or deleting emails), require explicit user approval before the application executes the action. This reduces the chance of unauthorized actions triggered by indirect prompt injection attacks.
- **Segregate External Content:** Clearly separate external content from user prompts. This limits the influence of potentially malicious external input on user prompts. Consider using a markup language like ChatML for OpenAI API calls to signal the LLM about input sources.
- **Trust Boundaries and Input Validation:** Treat the LLM as an untrusted entity, adopting a zero-trust approach. Rigorously apply input validation on all LLM responses sent to backend functions, following OWASP ASVS (Application Security Verification Standard) guidelines for effective input validation and sanitization.
- **Output Encoding:** Encode LLM output relayed back to users to prevent undesired code execution (e.g., through JavaScript or Markdown injection). OWASP AVSV offers specific guidance on appropriate output encoding techniques.
- **Manual Monitoring:** Periodically monitor LLM input and output to ensure it behaves as expected. While not a direct mitigation, this provides valuable data for detecting potential weaknesses and addressing them proactively.

## References
1. [Portswigger](https://portswigger.net/web-security/llm-attacks)
2. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)
