Created: 2025-12-04 15:45
#note

Secure design review is a systematic examination of system architecture and design to identify security flaws, ensure adherence to security best practices, and validate that [[Software Security Requirements]] are properly addressed. It's a critical checkpoint in the [[Secure SDLC]] design phase, occurring before significant development effort is invested.

## Overview

Security vulnerabilities often originate from fundamental design decisions rather than implementation bugs. A secure design review catches these architectural flaws early, when they're still relatively inexpensive to fix. This proactive approach prevents security issues that would be difficult or impossible to remediate through code-level changes alone.

## Objectives

- Validate that [[Threat Modeling]] findings are addressed in the design
- Ensure security requirements are incorporated into architecture
- Identify design patterns that could introduce vulnerabilities
- Verify defense-in-depth strategies are implemented
- Confirm that security controls are correctly positioned
- Assess [[Attack Surface Evaluation|attack surface]] and minimize exposure
- Review trust boundaries and data flow security

## What to Review

### 1. Architecture Components
- System decomposition and module boundaries
- Component interactions and dependencies
- Trust boundaries and security zones
- Data storage and processing locations
- External integrations and APIs
- Infrastructure design (cloud, on-premise, hybrid)

### 2. Authentication and Authorization
- Identity management approach
- Authentication mechanisms (passwords, MFA, SSO, OAuth)
- Session management strategy
- Authorization model (RBAC, ABAC, etc.)
- Token handling and lifecycle
- Privileged access management

### 3. Data Security
- Data classification and sensitivity levels
- Encryption at rest and in transit
- Key management and storage
- Data retention and deletion policies
- PII and sensitive data handling
- Cross-border data transfer considerations

### 4. Input Validation and Output Encoding
- Input validation strategies
- Sanitization approaches
- Output encoding mechanisms
- API contract validation
- File upload handling
- Query parameterization

### 5. Error Handling and Logging
- Error message design (avoiding information disclosure)
- Logging strategy and sensitive data in logs
- Audit trail completeness
- Log protection and integrity
- Monitoring and alerting integration

### 6. Network Security
- Network segmentation strategy
- Firewall rules and security groups
- TLS/SSL configuration
- Certificate management
- DDoS protection
- API gateway and rate limiting

### 7. Third-Party Components
- [[Third-Party Dependency Scanning|Dependency]] selection criteria
- License compliance
- Known vulnerabilities in dependencies
- Update and patching strategy
- Vendor security assessment for [[Supply Chain Security]]

## Review Process

### 1. Preparation
- Gather architecture diagrams and documentation
- Review [[Threat Modeling]] outputs
- Collect [[Software Security Requirements]]
- Identify relevant security standards and frameworks
- Assemble cross-functional review team

### 2. Review Session
- Walk through system architecture
- Examine each component and interface
- Discuss security controls and their placement
- Challenge assumptions about trust and security
- Document findings and concerns
- Identify gaps and weaknesses

### 3. Analysis
- Prioritize findings by risk
- Assess feasibility of remediation
- Consider alternative designs
- Evaluate trade-offs (security vs. performance, usability, cost)
- Map findings to security requirements

### 4. Documentation
- Create detailed finding reports
- Document security design decisions and rationale
- Update architecture diagrams with security annotations
- Record accepted risks and compensating controls
- Create action items for remediation

### 5. Follow-up
- Track remediation of findings
- Re-review significant design changes
- Update [[Threat Modeling]] based on design changes
- Ensure findings are addressed in implementation phase

## Common Design Flaws

### Authentication and Session Management
- Weak password policies
- Insecure session token generation
- Missing session timeout
- Inadequate MFA implementation
- Session fixation vulnerabilities

### Authorization
- Missing access controls
- Confused deputy problem
- Insecure direct object references
- Horizontal/vertical privilege escalation opportunities
- Over-privileged service accounts

### Data Exposure
- Storing sensitive data in plaintext
- Using weak encryption algorithms
- Inadequate key management
- Exposing sensitive data in URLs or logs
- Missing data classification

### Input Handling
- Trusting client-side validation alone
- SQL injection vulnerability paths
- Command injection possibilities
- XML/JSON injection vectors
- Path traversal opportunities

### Architecture
- Missing defense in depth
- Single points of failure
- Inadequate network segmentation
- Exposed administrative interfaces
- Missing security boundaries

## Security Design Patterns

### Good Patterns to Encourage
- **Defense in Depth**: Multiple layers of security controls
- **Least Privilege**: Minimal necessary permissions
- **Fail Secure**: Secure defaults when errors occur
- **Separation of Duties**: No single user has complete control
- **Zero Trust**: Never trust, always verify
- **Complete Mediation**: Check every access attempt
- **Economy of Mechanism**: Keep design simple and understandable

### Anti-Patterns to Avoid
- **Security by Obscurity**: Relying on secrecy of design
- **Hardcoded Secrets**: Credentials or keys in code
- **Monolithic Trust**: Large trust boundaries
- **Client-Side Security**: Trusting client validation
- **Improper Error Handling**: Revealing system internals
- **God Objects**: Components with excessive privileges

## Review Checklist

- [ ] All [[Software Security Requirements]] mapped to design elements
- [ ] [[Threat Modeling]] threats have mitigations in design
- [ ] [[Attack Surface Evaluation]] completed and minimized
- [ ] Authentication mechanism appropriate for sensitivity
- [ ] Authorization model enforces least privilege
- [ ] Sensitive data encrypted in transit and at rest
- [ ] Input validation implemented at trust boundaries
- [ ] Error handling prevents information disclosure
- [ ] Logging captures security-relevant events
- [ ] Network security controls properly positioned
- [ ] [[Third-Party Dependency Scanning|Third-party components]] assessed for security
- [ ] Security testing strategy defined for [[Penetration Testing]]
- [ ] Incident response plan considered in design
- [ ] Compliance requirements addressed

## Integration with Development

Findings should:
- Be tracked in the same system as other development tasks
- Block progression if critical security flaws exist
- Be validated during [[Static Code Analysis]] and code reviews
- Be tested during [[Penetration Testing]]
- Inform [[Security Monitoring]] and detection strategies

## Benefits

- **Early Flaw Detection**: Identifies architectural vulnerabilities before implementation
- **Cost Savings**: Fixing design flaws early is exponentially cheaper
- **Shared Understanding**: Creates security awareness across the team
- **Compliance**: Documents security due diligence
- **Quality**: Improves overall system robustness and reliability

## Challenges

- **Resource Intensive**: Requires time from multiple skilled team members
- **Expertise Required**: Need security architects or specialists
- **Subjectivity**: Different reviewers may identify different issues
- **Resistance**: Developers may view as process overhead
- **Keeping Current**: Design evolves, requiring periodic re-review

## References
1. [OWASP Application Security Architecture Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Application_Security_Architecture_Cheat_Sheet.html)
2. [Microsoft Security Development Lifecycle - Design Phase](https://www.microsoft.com/en-us/securityengineering/sdl/practices)
3. [NIST SP 800-160: Systems Security Engineering](https://csrc.nist.gov/publications/detail/sp/800-160/vol-1/final)
4. [Security by Design Principles - OWASP](https://owasp.org/www-project-security-by-design-principles/)

#### Tags
#security #secure_design #architecture #code_review #sdlc
