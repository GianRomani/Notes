Created: 2023-12-23 16:56
#note

One of the [[Vulnerabilities in LLM-base applications]].

Large Language Models (LLMs) rely on a complex supply chain encompassing not just software components, but also pre-trained models and training data. This introduces new vulnerability risks compared to traditional software:

- **Data and Model Tampering:** The training data and pre-trained models obtained from third parties can be susceptible to manipulation or "poisoning," potentially leading to biased outputs or security vulnerabilities in the final LLM.
- **Integrity Concerns:** These vulnerabilities can erode the overall integrity of the LLM, resulting in biased model outputs, security breaches, or even complete system failures.

This highlights the importance of securing the entire LLM supply chain, including careful selection of trusted data sources and pre-trained models.

Examples of vulnerabilities:
- **Traditional Third-Party Dependencies:** Outdated or deprecated packages introduce known software vulnerabilities.
- **Vulnerable Pre-Trained Models:** Fine-tuning LLMs on vulnerable pre-trained models inherits those vulnerabilities.
- **Poisoned Training Data:** Crowd-sourced data, if not carefully vetted, can introduce biases or security flaws into the LLM.
- **Outdated Models:** Using unmaintained models poses security risks due to unpatched vulnerabilities.
- **Inadequate Privacy Policies:** Unclear terms and conditions could expose your application's sensitive data for further model training, potentially leading to information disclosure or copyright issues if the original model used copyrighted material.

## Example in details:
**The breach:** A [dependency vulnerability](https://vuldb.com/?id.246286=&ref=txt.cohere.com) has been identified in ray, an open-source unified compute framework for machine learning engineers to scale AI and Python workloads. It is classed under the Common Vulnerabilities and Exposure list (CVE-2023-48023) and the Common Weakness Enumeration (CWE-918). Affected versions of this package are vulnerable to arbitrary command injection through the `**/log_proxy` function. An attacker can inject [arbitrary commands](https://security.snyk.io/vuln/SNYK-PYTHON-RAY-6096054?ref=txt.cohere.com) by submitting raw HTTP requests or via the Jobs SDK, with no authentication by default. An arbitrary code execution vulnerability is a security flaw in software or hardware, allowing random sample code execution.

**The impact:** The impact of this vulnerability can spread to server-side request forgery, where a web server can be tricked into making a request where it shouldn’t. Without proper checks, it can lead to data leaks or unauthorized actions. For example, an attacker can send a URL to the web server, the request might bypass authentication, and the server may then retrieve the contents of this URL, but it does not sufficiently ensure or check that the request is being sent to a safe or intended destination.

**The mitigation:** For starters, to mitigate this breach, developers for enterprise use cases must ensure that a rigorous supply chain is kept throughout both the software and model development life cycle to understand what dependencies the application and model are built on. A strong vulnerability management process should be in place to address these issues. Developers must generate both software and machine-learning bill of materials (SBOM and MLBOM) attestations to provide clarity and transparency on artifacts, and align on streamlined security operations within the life cycle prior to production release. For example, it is important to apply static application security testing (SAST) within version control to detect vulnerable or outdated components, and to automatically apply patching when needed. Not all vulnerabilities may be relevant to an application given their context and unique risk profile. Finding a balance between staying alert to new vulnerabilities and understanding the real implications of the vulnerabilities is critical for continuous monitoring and ongoing management.

## References
1. [Cohere](https://txt.cohere.com/the-state-of-ai-security/)
2. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)

## Tags
#aisecurity #llm #cybersecurity 