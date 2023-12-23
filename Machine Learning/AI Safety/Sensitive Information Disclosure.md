Created: 2023-12-23 16:50
#note

**The breach:** Regardless of how an AI model is accessed, there's a real risk that small parts of important data can be stolen using sophisticated methods. [Research](https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html?ref=txt.cohere.com) has shown that this form of direct fractional data exfiltration of potential sensitive or proprietary data from adversarial techniques works across an array of both open-source and production-ready closed models.

**The impact:** By querying an LLM, it is actually possible to extract some of the exact data it was trained on. Predictions indicate that it would be possible to extract around a gigabyte of the model's training dataset from the model by spending more money querying the model.

**The mitigation:** To mitigate this threat, one practical approach is to implement an input blocklist or an output filter specifically designed to counteract this type of exploit. The fundamental vulnerabilities here are the tendencies of language models to diverge from expected behaviors and to memorize training data. Addressing these issues requires not only initial model safety measures, but also ongoing research, development, and continuous red teaming throughout the model's lifecycle.

## References
1. [Cohere](https://txt.cohere.com/the-state-of-ai-security/)