Created: 2025-12-04 15:45
#note

Penetration testing (pen testing) is a simulated cyber attack against a system to identify exploitable vulnerabilities. Unlike automated scanning, penetration testing involves human expertise to chain vulnerabilities, exploit complex attack paths, and assess real-world risk. It's a critical validation step in the [[Secure SDLC]] testing phase.

## Overview

While [[Static Code Analysis]] and automated scanners identify potential vulnerabilities, penetration testing validates whether these vulnerabilities are actually exploitable and assesses the real-world impact of successful attacks. Pen testers think like attackers, combining technical expertise with creativity to find security weaknesses that automated tools miss.

## Types of Penetration Testing

### By Knowledge Level

#### Black Box Testing
- Tester has no prior knowledge of the system
- Simulates external attacker with no insider information
- Most realistic for external threats
- Can miss issues that require internal knowledge
- Time-consuming as reconnaissance is required

#### White Box Testing
- Tester has complete knowledge (source code, architecture, credentials)
- Most comprehensive coverage
- Efficient use of time
- Can identify vulnerabilities that black box testing would miss
- Less realistic for external attacker simulation

#### Gray Box Testing
- Tester has partial knowledge (e.g., user-level access)
- Balanced approach between black and white box
- Simulates insider threats or compromised accounts
- Common for web application testing

### By Target Scope

#### Network Penetration Testing
- Tests network infrastructure security
- Identifies vulnerabilities in routers, firewalls, switches
- Assesses network segmentation
- Tests wireless network security
- Evaluates VPN and remote access security

#### Web Application Penetration Testing
- Focuses on web applications and APIs
- Tests for OWASP Top 10 vulnerabilities
- Includes authentication and session management
- Business logic flaws
- Client-side vulnerabilities

#### Mobile Application Penetration Testing
- Tests iOS and Android applications
- Includes local data storage security
- API communication security
- Binary security and reverse engineering
- Platform-specific vulnerabilities

#### Cloud Penetration Testing
- Tests cloud infrastructure (AWS, Azure, GCP)
- Assesses cloud configuration security
- IAM and access control testing
- Container and serverless security
- Shared responsibility model validation

#### Physical Penetration Testing
- Tests physical security controls
- Building access and badge systems
- Social engineering scenarios
- Physical device security
- Security camera and monitoring bypass

#### Social Engineering Testing
- Phishing campaigns
- Pretexting and impersonation
- Physical social engineering
- Phone-based attacks (vishing)
- Tests human factors in security

## Penetration Testing Methodology

### 1. Planning and Reconnaissance
- Define scope and objectives
- Identify systems and applications to test
- Gather intelligence about target
- Passive reconnaissance (OSINT)
- Active reconnaissance (scanning, enumeration)

### 2. Scanning and Enumeration
- Port scanning and service identification
- Vulnerability scanning
- Application fingerprinting
- [[Attack Surface Evaluation]] in practice
- Directory and file enumeration
- User enumeration

### 3. Gaining Access
- Exploit identified vulnerabilities
- Attempt authentication bypass
- Privilege escalation
- Testing input validation weaknesses
- Social engineering (if in scope)

### 4. Maintaining Access
- Establish persistent access mechanisms
- Backdoor installation (in controlled environment)
- Token persistence
- Credential harvesting
- Lateral movement preparation

### 5. Analysis and Reporting
- Document all findings
- Assess business impact
- Provide remediation recommendations
- Risk scoring and prioritization
- Executive summary for stakeholders

### 6. Remediation Verification
- Retest after fixes are implemented
- Confirm vulnerabilities are resolved
- Validate remediation doesn't introduce new issues

## Common Vulnerability Classes Tested

### OWASP Top 10
- Injection (SQL, Command, LDAP)
- Broken Authentication
- Sensitive Data Exposure
- XML External Entities (XXE)
- Broken Access Control
- Security Misconfiguration
- Cross-Site Scripting (XSS)
- Insecure Deserialization
- Using Components with Known Vulnerabilities
- Insufficient Logging & Monitoring

### Additional Testing Areas
- Business logic flaws
- Race conditions
- Server-Side Request Forgery (SSRF)
- Insecure Direct Object References (IDOR)
- Cross-Site Request Forgery (CSRF)
- Clickjacking
- API security issues
- Cryptographic weaknesses
- Session management flaws

## Tools and Techniques

### Reconnaissance
- **Nmap**: Network scanning and service detection
- **Shodan**: Search engine for internet-connected devices
- **Whois/DNS tools**: Domain and infrastructure information
- **Google Dorks**: Advanced search for exposed information
- **theHarvester**: Email and subdomain harvesting

### Vulnerability Scanning
- **Nessus**: Comprehensive vulnerability scanner
- **OpenVAS**: Open-source vulnerability scanner
- **Nikto**: Web server scanner
- **OWASP ZAP**: Web application security scanner
- **Burp Suite**: Web vulnerability scanner and proxy

### Exploitation
- **Metasploit Framework**: Exploit development and execution
- **SQLmap**: Automated SQL injection exploitation
- **BeEF**: Browser exploitation framework
- **Cobalt Strike**: Commercial adversary simulation platform
- **Empire/Covenant**: Post-exploitation frameworks

### Password Attacks
- **Hashcat**: GPU-accelerated password cracking
- **John the Ripper**: Password cracker
- **Hydra**: Network login brute forcer
- **CeWL**: Custom wordlist generator

### Post-Exploitation
- **Mimikatz**: Credential extraction
- **BloodHound**: Active Directory attack path mapping
- **PowerSploit**: PowerShell post-exploitation framework

## Best Practices

### 1. Define Clear Scope
- Specific IP ranges, domains, or applications
- Testing timeframe
- Allowed and prohibited actions
- Emergency contacts
- Legal authorization and rules of engagement

### 2. Get Proper Authorization
- Written permission from system owners
- Legal agreements and contracts
- Third-party authorization if applicable
- Notification to relevant stakeholders

### 3. Test in Appropriate Environment
- Prefer staging over production when possible
- Back up systems before testing
- Coordinate with operations team
- Have rollback plans

### 4. Document Everything
- Record all actions taken
- Screenshot evidence
- Command history and outputs
- Timeline of activities
- Proof of concept exploits

### 5. Prioritize Findings
- Consider exploitability and impact
- Align with [[Threat Modeling]] scenarios
- Business context matters
- Chain vulnerabilities for realistic attack paths

### 6. Communicate Responsibly
- Secure transmission of findings
- Appropriate audience for different reports
- Clear remediation guidance
- Follow responsible disclosure practices

## Integration with Secure SDLC

Penetration testing validates:
- **[[Software Security Requirements]]**: Verifies security controls are effective
- **[[Threat Modeling]]**: Tests whether identified threats are actually exploitable
- **[[Secure Design Review]]**: Validates architectural security decisions
- **[[Attack Surface Evaluation]]**: Confirms attack surface is minimized
- **[[Static Code Analysis]]**: Verifies code-level vulnerabilities are exploitable
- **[[Third-Party Dependency Scanning]]**: Tests if dependency vulnerabilities are reachable

Findings feed into:
- **[[Vulnerability Management]]**: Prioritized list of vulnerabilities to fix
- **[[Security Monitoring]]**: Detection rules for identified attack patterns
- **[[Change Management]]**: Remediation changes before deployment

## Penetration Testing Report Components

### Executive Summary
- High-level overview of findings
- Business impact assessment
- Risk summary
- Strategic recommendations

### Technical Details
- Detailed vulnerability descriptions
- Steps to reproduce
- Proof of concept code or screenshots
- Technical impact analysis
- CVSS scores

### Remediation Guidance
- Specific fix recommendations
- Priority and timeline suggestions
- Code examples or configuration changes
- Workarounds for temporary mitigation

### Appendices
- Methodology description
- Tools used
- Full command outputs
- Network diagrams
- Timeline of activities

## Frequency and Timing

### Regular Schedule
- Annual comprehensive penetration test
- Quarterly focused tests on high-risk areas
- After major releases or architectural changes
- Following significant security incidents

### Event-Driven
- Before launching new applications
- After major security updates
- In response to new threat intelligence
- For compliance requirements

### Continuous Testing
- Bug bounty programs for ongoing testing
- Automated penetration testing tools
- Regular security assessments by internal teams

## Compliance and Standards

Many regulations and frameworks require penetration testing:
- **PCI DSS**: Annual and after significant changes
- **HIPAA**: As part of risk analysis
- **SOC 2**: Regular security testing
- **ISO 27001**: Periodic testing required
- **GDPR**: Part of security measures
- **FedRAMP**: Annual penetration testing

## Limitations

- **Point in Time**: Results valid only at time of test
- **Scope Limited**: Only tests explicitly authorized systems
- **Time Constrained**: Limited time may not uncover all issues
- **Skill Dependent**: Quality varies with tester expertise
- **Disruptive**: Can impact system availability
- **False Sense of Security**: Passing doesn't guarantee complete security

## Red Team vs Penetration Testing

### Penetration Testing
- Defined scope and objectives
- Collaborative with defenders
- Focuses on finding vulnerabilities
- Comprehensive documentation
- Fixed timeline

### Red Team Operations
- Broader scope, simulate real adversary
- Adversarial to defenders (who may not know)
- Tests detection and response capabilities
- Goal-oriented (e.g., access specific data)
- Extended timeframe

## Bug Bounty Programs

Alternative or complement to traditional pen testing:
- Continuous testing by security researchers
- Pay for findings, not time
- Diverse perspectives and skills
- Scales beyond internal resources
- Requires mature vulnerability management process

### Popular Platforms
- HackerOne
- Bugcrowd
- Synack
- Intigriti

## References
1. [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
2. [Penetration Testing Execution Standard (PTES)](http://www.pentest-standard.org/)
3. [NIST SP 800-115: Technical Guide to Information Security Testing](https://csrc.nist.gov/publications/detail/sp/800-115/final)
4. [SANS Penetration Testing Resources](https://www.sans.org/penetration-testing/)

#### Tags
#security #penetration_testing #vulnerability #ethical_hacking #red_team #sdlc
