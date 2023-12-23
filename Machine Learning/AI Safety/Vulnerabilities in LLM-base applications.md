Created: 2023-12-23 13:04
#note
LLM-based web applications present most of the security issues of traditional web applications (e.g. DOS attacks) plus additional problems related to natural language inputs (i.e they are subject to prompt injection attacks). 
![[vulnerabilities_llm.png]]

The image above highlights most of the vulnerabilities that we should consider when developing an AI-based product, but not all. Apart from traditional applications' vulnerabilities (see [OWASP guidelines](https://owasp.org/www-project-application-security-verification-standard/?ref=txt.cohere.com)), issues related to MLOSecOps, [split-view data poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg?ref=txt.cohere.com) and [frontrunning data poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg?ref=txt.cohere.com) are two examples, are not included but should be considered.
## References
1. [Cohere](https://txt.cohere.com/the-state-of-ai-security/)
2. 

## Code
1. 