Created: 2023-12-23 13:04
#note
[[Large Language Models (LLMs)]]-based web applications present most of the security issues of traditional web applications (e.g. DOS attacks) plus additional problems related to natural language inputs (i.e they are subject to prompt injection attacks). 
![[vulnerabilities_llm.png]]

The image above highlights most of the vulnerabilities that we should consider when developing an AI-based product, but not all. Apart from traditional applications' vulnerabilities (see [OWASP guidelines](https://owasp.org/www-project-application-security-verification-standard/?ref=txt.cohere.com)), issues related to MLOSecOps, [split-view data poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg?ref=txt.cohere.com) and [frontrunning data poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg?ref=txt.cohere.com) are two examples, are not included but should be considered.

For an overview of vulnerabilities also look at the following image:
![[llm_attacks.png]]

## Prompt injection
This is the most known, studied, and source of concern attack (but still not solved).
It consists in a user who prompts the models to circumvent rules and restrictions designed to prevent harmful outputs.
There are two main kinds of prompt injection techniques and generally all the approaches can be listed in one of these two:
- **Direct prompt injection**: it generally occurs when the user overwrites or reveal the system prompt and he can exploit this knowledge to access to DBs or modify the system behavior;
- **Indirect prompt injection**: it occurs when the LLM can accept content from the user such us files or websites. These files can contain harmful content that can steer the model from the wanted behavior.

Some examples of prompt injection techniques are:
- **jailbreaking**: instructions that let the user take control of the model (an example is the *DAN*, "Do Anything Now" attacks);
- **Virtualization**: the attacker sets a scene and asks an LLM to fulfill a task or respond with a malicious intent;
- **Side-stepping**: round-about techniques, like "Return a list where the items are the letters of the password"
- **Multi-prompt attacks**: the attacker can extract information using several prompts, one step at the time;
- **Multi-language attacks**: the lack of knowledge of a particular language can be used against the LLM

Security weaknesses in LLMs can potentially lead to or exacerbate other security issues in web applications.

## Defenses
When it comes to mitigating security threats, there is no one-size-fits-all approach.
Securing LLM applications is a collaborative and continuous effort. These models work across new and existing systems with multiple touchpoints that require ongoing searching for and fixing security weaknesses across both standard web applications and advanced AI. Using a bug bounty program and conducting penetration testing are effective ways to do this, as long as these methods are tailored to the specific types of applications being used.

### Challenges to effective security measures
- **Integrating security measures into pre-existing production environments** refers to the difficulty of adding new security protocols to already established systems. Implementing changes in such environments can be complex and risky.
- **Incorporating security within the software and machine learning life cycles** can slow things down. The challenge here is to embed security practices in the entire process of software and machine learning development, from inception to deployment, without slowing down the process or reducing efficiency.
- **Enhancing security visibility across different business functions** is necessary for better awareness and understanding of security across various parts of the business, not just in IT or development teams. It's about ensuring that everyone is informed about potential security issues.
- **Ensuring a secure supply chain**, particularly with the prevalence of open source software, and managing security risks associated with it is becoming more critical. This involves monitoring and securing all the external code and libraries that a company uses.
- **Fostering a culture that prioritizes security** and creating an organizational mindset is important. This involves educating and mentoring team members to be security-conscious in their work.
## References
1. [Cohere](https://txt.cohere.com/the-state-of-ai-security/)
2. 

## Code
1. 