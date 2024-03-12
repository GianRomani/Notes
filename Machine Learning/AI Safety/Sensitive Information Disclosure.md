Created: 2023-12-23 16:50
#note

One of the [[Vulnerabilities in LLM-base applications]].

**The breach:** Regardless of how an AI model is accessed, there's a real risk that small parts of important data can be stolen using sophisticated methods. [Research](https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html?ref=txt.cohere.com) has shown that this form of direct fractional data exfiltration of potential sensitive or proprietary data from adversarial techniques works across an array of both open-source and production-ready closed models.

**The impact:** By querying an [[Large Language Models (LLMs)]], it is actually possible to extract some of the exact data it was trained on. Predictions indicate that it would be possible to extract around a gigabyte of the model's training dataset from the model by spending more money querying the model.

**The mitigation:** To mitigate this threat, one practical approach is to implement an input blocklist or an output filter specifically designed to counteract this type of exploit. The fundamental vulnerabilities here are the tendencies of language models to diverge from expected behaviors and to memorize training data. Addressing these issues requires not only initial model safety measures, but also ongoing research, development, and continuous red teaming throughout the model's lifecycle.

Mitigation techniques:
- **Integrate Data Sanitization and Scrubbing:** Thoroughly sanitize and scrub training data to ensure the exclusion of sensitive user information, preventing its potential exposure.
- **Implement Robust Input Validation and Sanitization:** Employ strict input validation and sanitization to identify and filter out malicious inputs, safeguarding the model against poisoning attacks.
- **Exercise Caution with Fine-tuning:** Be mindful of the risks involved in enriching or fine-tuning the model. Uphold the principle of least privilege: avoid training the model on data that exceeds the access levels of lower-privileged users.
- **Restrict External Data Access:** Limit the LLM's access to external data sources or the ability to orchestrate data flows at runtime. Enforce strong access control and a rigorous approval process to maintain a secure data supply chain.

## References
1. [Cohere](https://txt.cohere.com/the-state-of-ai-security/)
2. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)

## Tags
#aisecurity #llm #cybersecurity 