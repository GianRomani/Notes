Created: 2025-12-15 15:50
#note

Insecure design refers to security flaws arising during an application's design and architecture phase, before any code is written. Part of OWASP Top 10 (A04:2021), these are fundamental weaknesses baked into the system's foundation that persist throughout the lifecycle. Unlike implementation bugs, design flaws cannot be fixed through patching alone—they require architectural redesign.

The key distinction: insecure design exists even if code is implemented perfectly. A well-coded application built on flawed architecture remains vulnerable. This makes security during the design phase of the [[Secure SDLC]] critical for fundamentally secure systems.

## Common Design Flaws

### Missing Security Controls
- No authentication or authorization mechanisms
- Lack of input validation at architectural level
- Missing rate limiting or resource controls
- No encryption for sensitive data flows

### Broken Business Logic
- Insufficient validation of business rules
- Missing transaction integrity controls
- Race condition vulnerabilities in design
- Trust assumptions that can be violated

### Insufficient Trust Boundaries
- Failing to separate privilege levels
- Mixing trusted and untrusted data flows
- No isolation between components
- Shared resources without access controls

### Exposure of Sensitive Functionality
- Administrative functions accessible to regular users
- Debug endpoints in production design
- Sensitive operations without approval workflows
- Direct object references without authorization

## Impact

- Cannot be patched without architectural redesign
- Increased attack surface with more exploitation opportunities
- Business logic bypass and workflow circumvention
- Data breaches and system compromise
- Costly remediation (exponentially more expensive after implementation)
- Compliance failures

## Prevention

### Secure by Design
- Define security requirements in [[Software Security Requirements]]
- Default deny for access controls
- Principle of least privilege
- Defense in depth across all layers
- Security considered in all architectural decisions

### Early Integration
- Security architects involved from the start
- [[Threat Modeling]] before implementation
- [[Secure Design Review]] of architecture
- Security acceptance criteria defined upfront

### Proven Patterns
- Reuse secure architectural patterns
- Leverage established security frameworks
- Follow OWASP and NIST standards
- Avoid reinventing security mechanisms

### Documentation
- Architecture diagrams with trust boundaries
- Data flow diagrams for sensitive data
- Security control documentation
- Design decision rationale

## Threat Modeling

Structured process for identifying and mitigating threats during design. Enables thinking like attackers to discover vulnerabilities before implementation.

### Core Components

**Trust Boundaries**: Lines separating areas with different security policies
- User roles (User vs Administrator)
- Network zones (Internal vs DMZ vs Internet)
- Environments (Dev vs Staging vs Production)
- Data sensitivity levels

**Threats**: Potential actions compromising security
- Unauthorized access, data tampering, information disclosure
- Service disruption, privilege escalation
- See MITRE CAPEC for threat patterns

**Security Controls**: Safeguards mitigating threats
- Technical: Authentication, encryption, validation
- Process: Approval workflows, access reviews
- Detective: Logging, monitoring, alerting

### Methodologies

**STRIDE** (Microsoft framework):
- **S**poofing identity
- **T**ampering with data
- **R**epudiation of actions
- **I**nformation disclosure
- **D**enial of service
- **E**levation of privilege

**PASTA**: Risk-centric 7-stage approach
- Business objectives → Technical scope → Decomposition → Threat analysis → Vulnerability analysis → Attack modeling → Risk assessment

**Attack Trees**: Hierarchical diagrams of attack paths

### Process
1. Identify assets and create architecture overview
2. Decompose application (components, data flows)
3. Identify threats using STRIDE or similar
4. Document vulnerabilities
5. Prioritize by likelihood and impact
6. Define mitigations

## Examples

**Scenario 1: Insecure Communication**
Web application uses HTTPS but architecture omits TLS for API calls. All API communication transmits in plaintext, exposing sensitive data. Not a coding bug—a fundamental design flaw.

**Scenario 2: Missing Business Logic**
Booking system allows unlimited reservations without deposits or payment validation. Attackers can book all slots without intent to use, causing revenue loss. System works as designed but lacks abuse prevention.

**Scenario 3: Insufficient Access Controls**
E-commerce platform uses direct database IDs in URLs without authorization checks. Users can modify order IDs to access other customers' data. Design assumed client-side controls were sufficient.

## Integration with Secure SDLC

- **Requirements**: Define in [[Software Security Requirements]]
- **Design**: [[Threat Modeling]], [[Secure Design Review]], [[Attack Surface Evaluation]]
- **Implementation**: Follow design, [[Static Code Analysis]], code reviews
- **Testing**: Security test cases, [[Penetration Testing]], business logic testing
- **Deployment**: [[Change Management]], configuration validation
- **Operations**: [[Security Monitoring]], [[Vulnerability Management]], update threat models

## Design vs Implementation

**Insecure Design**: Architectural flaw before coding, requires redesign (e.g., no rate limiting in architecture)

**Insecure Implementation**: Coding error in sound design, fixable with code changes (e.g., SQL injection)

Both must be addressed—secure design poorly implemented is vulnerable, and insecure design perfectly implemented is also vulnerable.

## Tools

- **Threat Modeling**: Microsoft Threat Modeling Tool, OWASP Threat Dragon, IriusRisk
- **Documentation**: UML diagrams, Data Flow Diagrams (DFD)
- **Standards**: OWASP ASVS, NIST Cybersecurity Framework, ISO 27001, OWASP SAMM

## Best Practices

- Start security from day one with threat modeling
- Document architecture with security annotations
- Peer review designs with security experts
- Use proven patterns and frameworks
- Test and challenge security assumptions
- Continuously update threat models based on findings

## References
- [OWASP Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [OWASP SAMM - Design: Threat Assessment](https://owaspsamm.org/model/design/threat-assessment/)
- [MITRE CAPEC](https://capec.mitre.org/)

#### Tags
#security #insecure_design #threat_modeling #owasp_top_10 #architecture #sdlc
