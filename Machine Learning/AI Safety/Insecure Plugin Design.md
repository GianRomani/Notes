Created: 2024-03-12 13:49
#quicknote

One of the [[Vulnerabilities in LLM-base applications]].

LLM plugins extend model functionalities but raise security concerns due to their automatic execution and potential lack of control by the application. Here's why:
- **Limited Application Control:** When hosted by a third party, the application may have limited control over plugin execution.
- **Unvalidated Model Inputs:** Plugins often operate on free-text inputs from the LLM with minimal validation or type-checking. This creates vulnerabilities due to potential context size limitations.
- **Attack Vectors:** Malicious actors can exploit vulnerabilities through these free-text inputs, potentially leading to:
	- Remote code execution (RCE): This allows attackers to execute arbitrary code on the system hosting the LLM.
    - Data Exfiltration: Confidential data may be stolen and transmitted to unauthorized parties.
    - Privilege Escalation: Attackers can gain elevated privileges within the system.
- **Inadequate Access Control:** Plugins often lack proper access control mechanisms, leading to vulnerabilities:
    - Blind Trust: Plugins may blindly trust other plugins and user inputs, allowing malicious inputs to propagate through the chain.
    - Authorization Tracking: Failure to track user authorization across plugins allows unauthorized access to resources.
## Resources
1. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)

#### Tags
#aisecurity #llm #cybersecurity 