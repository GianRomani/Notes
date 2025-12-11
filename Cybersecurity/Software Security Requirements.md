Created: 2025-12-04 15:45
#note

Software security requirements define the security properties, controls, and constraints that a system must satisfy. They are an essential component of the [[Secure SDLC]] requirements phase and serve as the foundation for building secure systems from the ground up.

## Overview

Security requirements differ from functional requirements in that they specify what the system should prevent or withstand, rather than what it should do. These requirements guide architectural decisions, implementation practices, and testing strategies throughout the development lifecycle.

## Types of Security Requirements

### 1. Confidentiality Requirements
Ensure that sensitive information is accessible only to authorized entities:
- Data encryption requirements (at rest and in transit)
- Access control policies
- Authentication mechanisms
- Data classification and handling procedures

### 2. Integrity Requirements
Guarantee that data and systems remain accurate and unaltered:
- Data validation and sanitization
- Digital signatures and checksums
- Audit logging
- Version control and change tracking

### 3. Availability Requirements
Ensure that systems and data remain accessible to authorized users:
- Uptime and reliability targets
- Disaster recovery and business continuity
- Protection against denial-of-service attacks
- Redundancy and failover mechanisms

### 4. Authentication Requirements
Verify the identity of users and systems:
- Multi-factor authentication (MFA)
- Password policies and strength requirements
- Session management
- Single sign-on (SSO) integration

### 5. Authorization Requirements
Control what authenticated entities can access and modify:
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- Principle of least privilege
- Segregation of duties

### 6. Non-Repudiation Requirements
Ensure that actions cannot be denied by their originators:
- Digital signatures
- Audit trails and logging
- Timestamping

## Sources of Security Requirements

- **Regulatory Compliance**: GDPR, HIPAA, PCI-DSS, SOC 2, etc.
- **Industry Standards**: ISO 27001, NIST frameworks, OWASP guidelines
- **[[Threat Modeling]]**: Identified threats and attack vectors
- **Business Requirements**: Organizational security policies and risk appetite
- **Previous Incidents**: Lessons learned from past security breaches
- **[[Supply Chain Security]]**: Requirements from vendors and third-party components

## Defining Effective Security Requirements

Good security requirements should be:

- **Specific**: Clearly defined and unambiguous
- **Measurable**: Can be tested and verified
- **Achievable**: Technically and economically feasible
- **Relevant**: Address actual security risks
- **Testable**: Can be validated through security testing

### Examples

Poor requirement: "The system must be secure"

Good requirements:
- "All user passwords must be hashed using bcrypt with a minimum cost factor of 12"
- "All API communications must use TLS 1.3 or higher"
- "Users must authenticate using MFA for access to sensitive data"
- "The system must log all administrative actions with timestamps and user identifiers"
- "Session tokens must expire after 30 minutes of inactivity"

## Integration with Development

Security requirements should be:
- Documented in the same format as functional requirements
- Prioritized based on risk assessment
- Traceable throughout the development lifecycle
- Validated through [[Static Code Analysis]], [[Penetration Testing]], and security reviews
- Included in acceptance criteria and definition of done

## Common Pitfalls

- **Vague Requirements**: "System should be secure" or "Use industry best practices"
- **Conflicting Requirements**: Security requirements that contradict usability or performance goals
- **Over-Engineering**: Implementing excessive security controls that don't address actual risks
- **Under-Specification**: Missing critical security requirements due to incomplete [[Threat Modeling]]
- **Ignoring Dependencies**: Not considering security requirements of [[Third-Party Dependency Scanning|third-party dependencies]]

## References
1. [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
2. [NIST SP 800-160: Systems Security Engineering](https://csrc.nist.gov/publications/detail/sp/800-160/vol-1/final)
3. [Security Requirements Engineering Framework](https://www.sei.cmu.edu/our-work/security-requirements-engineering/)

#### Tags
#security #requirements #sdlc #secure_design
