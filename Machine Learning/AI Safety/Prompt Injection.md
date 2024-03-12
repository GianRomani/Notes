Created: 2024-03-12 11:53
#quicknote

One of the [[Vulnerabilities in LLM-base applications]].

Prompt Injection Vulnerability occurs when an attacker manipulates a large language model (LLM) through crafted inputs, causing the LLM to unknowingly execute the attacker's intentions. This can be done directly by "jailbreaking" the system prompt or indirectly through manipulated external inputs, potentially leading to data exfiltration, social engineering, and other issues.

For more details on the types of Prompt Injection attacks, check: [[Prompt Injection types]].

Mitigations:
- **Restrict LLM Access:** Enforce strict privilege controls on LLM access to backend systems. Provide the LLM with its own API tokens for extensible functionality (plugins, data access, etc.), adhering to the principle of least privilege. Limit the LLM's access to only what is essential for its intended operations.
- **Human-in-the-Loop:** For extended functionality and privileged operations (such as sending or deleting emails), require explicit user approval before the application executes the action. This reduces the chance of unauthorized actions triggered by indirect prompt injection attacks.
- **Segregate External Content:** Clearly separate external content from user prompts. This limits the influence of potentially malicious external input on user prompts. Consider using a markup language like ChatML for OpenAI API calls to signal the LLM about input sources.
- **Trust Boundaries:** Treat the LLM as an untrusted entity, even with plugins or downstream functions, and maintain ultimate user control over decision-making. A compromised LLM could act as a "man-in-the-middle," manipulating information before presenting it to the user. Highlight potentially untrustworthy LLM responses visually to the user.
- **Manual Monitoring:** Periodically monitor LLM input and output to ensure it behaves as expected. While not a direct mitigation, this provides valuable data for detecting potential weaknesses and addressing them proactively.

## Resources
1. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)

#### Tags
#aisecurity #llm #cybersecurity 