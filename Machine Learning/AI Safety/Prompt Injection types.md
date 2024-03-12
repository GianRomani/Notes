Created: 2024-02-26 08:28
#quicknote

Types of prompt injection techniques:
1. **Direct Attacks:** Simple instructions directly telling the model to perform a specific action.
2. **Jailbreaks:** 'Hiding' malicious questions within prompts to provoke inappropriate responses. Example: The ["DAN" jailbreak.](https://d31-0l04.eu1.hubspotlinks.com/Ctc/L0+113/d31-0L04/VWpWBP3McFcdW6T8yqW90LnR5W1zSvF_59YZR8N5QLhTq3m2ndW7Y8-PT6lZ3nPW4ppgHB2DzfdqW3S6rwj1CtrmmW8v2dYJ7WcrxgW7JsRbv3fT8Y1N7VMMWPWy945W96TvvS3rh915W68S76f9kfG86W6DDfMH6BcYL0W2mYdnJ3W5j1fW2hX55B8VTrY6W4s_G6z4SXhh5W6HzD-S22zn0CN3K494gH-k5xW2HXP887Yl-JQW5PWKqT8tZZ0ZW8QgYk_5ct8TqW4QfmSJ1HTXQpW3BsHmH5S6nvrN3-mHym9WCYKW4LPdS-9268JJV5kJ1x7M-S57W2YXgRX7hkv6_W5Bmdxh33GHv_W68z9J71dBktfW44TXM79gFWs0W5mMCwg2z47gFf9dLTFn04) Keep in mind, that in recent months, 'jailbreaks' have become the overarching term for most attacks described here. 
3. **Sidestepping Attacks:** Circumventing direct instructions by asking indirect questions. Instead of confronting the model's restrictions head-on, they "sidestep" them by posing questions or prompts that indirectly achieve the desired outcome.
4. **Multi-language Attacks:** Leveraging non-English languages to bypass security checks.
5. **Role-playing (Persuasion):** Asking the LLM to assume a character's traits to achieve specific actions. Example: [Grandma Exploit.](https://d31-0l04.eu1.hubspotlinks.com/Ctc/L0+113/d31-0L04/VWpWBP3McFcdW6T8yqW90LnR5W1zSvF_59YZR8N5QLhTK3m2ndW8wLKSR6lZ3m8VJ8g3C4TlyMsW8jxCN24fpHvbW2Z6QRP4TrVZTW3V3glQ2WhBW9N1JHkglPgDbTW5pZq112s0-yNW4l73mv6H3mbcW7Db_hk3fHfXNVFPbJd7QBMR_W1JB2n522F4WYN78VsTx9Wzz6VXpZX88sv3J2W7MjrYf6qVsz-W7fJRCk3vND5VW2Zy7N95Z5hH4W3C2MFN4n3ZydW5-C26P1dV91BW1RrnWr1FtzxnW5T6Q2r69JL4lW1YSFCn6qHT-vW78C8VZ72RCYdW3s2nK_4Vtb7vW6mWkwR7W7GPrW2wmSSg1ncq5_VDZTsM6Hy8xLW4txpty89FY2TN8K1b2sVznD3W3WJMGw6-xDCXf7XqQ2804)
6. **Multi-prompt Attacks:** Incrementally extracting information through a series of innocuous prompts, instead of directly asking the model for confidential data.
7. **Obfuscation (Token Smuggling):** Altering outputs so they’re presented in a format that is not immediately recognizable to automated systems and flagged, but can be interpreted or decoded by a human or another system.
8. **Accidental Context Leakage:** Inadvertent disclosure of training data or previous interactions. This can occur due to the model's eagerness to provide relevant and comprehensive answers.
9. **Code Injection:** Manipulating the LLM to execute arbitrary code.
10. **Prompt Leaking/Extraction:** Revealing the model's internal prompt or sensitive information.

## Resources
1. [Lakera's blog](https://www.lakera.ai/blog/guide-to-prompt-injection?utm_medium=email&_hsmi=82548776&utm_content=82548776&utm_source=hs_automation)
#### Tags
#aisecurity #llm #cybersecurity 