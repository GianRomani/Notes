Created: 2025-12-04 15:45
#note

Threat modeling is a structured approach to identifying, quantifying, and addressing security threats during the design phase of the [[Secure SDLC]]. It enables development teams to proactively discover potential vulnerabilities and attack vectors before they manifest in production systems.

## Overview

Rather than reacting to security issues after they occur, threat modeling allows teams to anticipate and mitigate threats early in the development process. This shift-left approach significantly reduces the cost and complexity of security remediation.

The process involves understanding the system architecture, identifying what could go wrong, determining countermeasures, and validating that threats have been addressed.

## Key Concepts

### Assets
Resources that need protection:
- Data (customer information, credentials, intellectual property)
- Systems and services
- Reputation and brand
- Financial resources

### Threats
Potential dangers to assets:
- Unauthorized access
- Data breaches
- Service disruption
- Data tampering

### Vulnerabilities
Weaknesses that can be exploited:
- Software bugs
- Configuration errors
- Design flaws
- Missing security controls

### Attack Vectors
Paths an attacker might use to exploit vulnerabilities:
- Network-based attacks
- Social engineering
- Physical access
- Supply chain compromise

## Common Threat Modeling Methodologies

### 1. STRIDE
Developed by Microsoft, STRIDE categorizes threats into six types:
- **S**poofing - Impersonating another user or system
- **T**ampering - Unauthorized modification of data
- **R**epudiation - Denying actions were performed
- **I**nformation Disclosure - Exposing confidential information
- **D**enial of Service - Making systems unavailable
- **E**levation of Privilege - Gaining unauthorized permissions

### 2. PASTA (Process for Attack Simulation and Threat Analysis)
Risk-centric methodology with seven stages:
1. Define objectives
2. Define technical scope
3. Application decomposition
4. Threat analysis
5. Vulnerability analysis
6. Attack modeling
7. Risk and impact analysis

### 3. DREAD
Risk assessment model rating threats by:
- **D**amage potential
- **R**eproducibility
- **E**xploitability
- **A**ffected users
- **D**iscoverability

### 4. Attack Trees
Hierarchical diagrams showing how assets can be attacked, with the root node representing the attacker's goal and branches showing different attack paths.

## Threat Modeling Process

### 1. Define System Scope
- Create architecture diagrams
- Identify components, data flows, and trust boundaries
- Document external dependencies and integrations
- Understand user roles and access patterns

### 2. Identify Threats
- Use frameworks like STRIDE to systematically identify threats
- Consider each component and data flow
- Brainstorm with cross-functional teams
- Review historical vulnerabilities in similar systems

### 3. Analyze and Prioritize Threats
- Assess likelihood and impact of each threat
- Calculate risk scores
- Prioritize based on business context and [[Attack Surface Evaluation]]
- Consider existing security controls

### 4. Define Mitigations
- Identify countermeasures for each significant threat
- Document as [[Software Security Requirements]]
- Balance security with usability and performance
- Consider defense in depth strategies

### 5. Validate
- Review with security experts
- Test mitigations through [[Secure Design Review]]
- Plan for validation during [[Penetration Testing]]
- Update threat model as system evolves

## Data Flow Diagrams (DFD)

Threat modeling often uses DFDs to visualize:
- **External entities** - Users, external systems
- **Processes** - Application components
- **Data stores** - Databases, files, caches
- **Data flows** - How information moves through the system
- **Trust boundaries** - Where security context changes (e.g., moving from client to server)

## Benefits

- **Early Detection**: Identifies vulnerabilities before code is written
- **Cost Reduction**: Fixing design flaws early is exponentially cheaper than post-deployment fixes
- **Improved Architecture**: Forces thoughtful consideration of security in system design
- **Risk Awareness**: Provides clear understanding of security risks for stakeholders
- **Compliance**: Demonstrates due diligence for regulatory requirements
- **Team Alignment**: Creates shared understanding of security concerns

## Challenges

- **Time Investment**: Requires dedicated effort from multiple team members
- **Expertise Required**: Effective threat modeling needs security knowledge
- **Keeping Updated**: Threat models can become outdated as systems evolve
- **Complexity**: Large systems can be overwhelming to model comprehensively
- **Subjectivity**: Risk assessment can vary based on participants' perspectives

## Integration with Development

Threat modeling should be:
- Performed early in the design phase
- Updated when significant architectural changes occur
- Integrated into [[Change Management]] processes
- Referenced during [[Static Code Analysis]] and code reviews
- Validated through [[Penetration Testing]]
- Documented and accessible to the development team

## Tools

- **Microsoft Threat Modeling Tool**: Free tool based on STRIDE methodology
- **OWASP Threat Dragon**: Open-source threat modeling tool
- **IriusRisk**: Commercial platform for threat modeling and security requirements
- **ThreatModeler**: Automated threat modeling platform
- **Cairis**: Requirements management tool with threat modeling capabilities

## References
1. [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
2. [Microsoft Threat Modeling Guide](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)
3. [Threat Modeling: Designing for Security by Adam Shostack](https://shostack.org/books/threat-modeling-book)
4. [NIST Guide to Threat Modeling](https://csrc.nist.gov/publications/detail/sp/800-154/draft)

#### Tags
#security #threat_modeling #sdlc #risk_assessment #stride
