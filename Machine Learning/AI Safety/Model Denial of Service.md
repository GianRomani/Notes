Created: 2024-03-12 13:33
#quicknote

One of the [[Vulnerabilities in LLM-base applications]].

Attackers can target LLMs in several ways:

- **Resource Exhaustion:** By crafting interactions designed to consume excessive computational resources, attackers can degrade the quality of service for both themselves and legitimate users. This can also lead to unexpectedly high costs for the application owner.
- **Context Manipulation:** An emerging security threat involves attackers attempting to manipulate or interfere with the LLM's context window. This manipulation could lead to unpredictable behavior, compromised outputs, and potential security vulnerabilities.

Mitigation techniques:
- **Input Validation and Sanitization:** Enforce strict input validation and sanitization to ensure user input conforms to defined limits and filters out malicious content.
- **Escaping and Request Segmentation:** Escape user input for each request step to prevent complex requests from executing in a less controlled manner.
- **API Rate Limiting:** Restrict the number of requests an individual user or IP address can make within a specific timeframe.
- **Action and Resource Limits:** Limit the number of queued actions and total actions related to LLM responses.
- **Resource Monitoring:** Continuously monitor LLM resource utilization to detect abnormal spikes or patterns indicative of a DoS (Denial of Service) attack.
- **Strict Input Limits:** Set strict input limits based on the LLM's context window to prevent overload and resource exhaustion.
- **Developer Awareness:** Educate developers about potential DoS vulnerabilities in LLMs. Provide clear guidelines for secure LLM implementation practices.

## Resources
1. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)
#### Tags
#aisecurity #llm #cybersecurity 

