Created: 2024-03-12 13:58
#quicknote

One of the [[Vulnerabilities in LLM-base applications]].

LLM-based systems often possess a degree of agency, meaning the ability to interact with external systems and perform actions based on prompts. Sometimes, an LLM 'agent' might determine which functions to invoke based on the input prompt or LLM output.

**Excessive Agency Vulnerability:** This vulnerability arises when an LLM is granted too much agency (excessive functionality, permissions, or autonomy). This can lead to harmful actions triggered by unexpected, ambiguous, or even malicious LLM outputs, regardless of whether the malfunction stems from hallucination, prompt injection, or other causes.

**Contrast with Insecure Output Handling:** Excessive Agency focuses on the LLM's ability to perform actions, while [[Insecure Output Handling]] involves insufficient scrutiny of the LLM's outputs themselves.

**Potential Consequences:** Excessive Agency can affect:

- **Confidentiality:** Data breaches and leakage of sensitive information.
- **Integrity:** Unauthorized modification or destruction of data.
- **Availability:** System disruptions or denial of service.

For possible mitigation techniques look at the OWASP report (page 25): https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf

## Resources
1. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)

#### Tags
#aisecurity #llm #cybersecurity 