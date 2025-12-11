Created: 2025-12-04 15:45
#note

Supply chain security (also called software supply chain security or third-party risk management) is the practice of identifying, assessing, and mitigating security risks introduced by external vendors, suppliers, contractors, and third-party components used in software development and operations. It's a critical aspect of the [[Secure SDLC]] that extends security considerations beyond organizational boundaries.

## Overview

Modern software systems rarely exist in isolation. They depend on:
- Open-source libraries and frameworks
- Commercial software components
- Cloud service providers
- Software-as-a-Service (SaaS) applications
- Hardware and firmware from vendors
- Outsourced development teams
- Third-party APIs and integrations

Each dependency represents a potential security risk. High-profile supply chain attacks (SolarWinds, Log4Shell, Codecov) have demonstrated that attackers increasingly target the supply chain as a way to compromise multiple victims simultaneously.

## Types of Supply Chain Risks

### 1. Software Component Risks
Risks from code dependencies:
- Known vulnerabilities in [[Third-Party Dependency Scanning|third-party libraries]]
- Malicious packages (typosquatting, dependency confusion)
- Abandoned or unmaintained dependencies
- Licensing issues
- Backdoors in dependencies
- Compromised package repositories

### 2. Vendor and Supplier Risks
Risks from external organizations:
- Vendor security practices and posture
- Access to systems and data
- Subcontractors and fourth parties
- Geographic and regulatory risks
- Financial stability and continuity
- Incident response capabilities

### 3. Development Process Risks
Risks in how software is built:
- Compromised build systems
- Malicious code injection during build
- Stolen code signing certificates
- Compromised developer accounts
- Insider threats in outsourced teams
- Lack of source code verification

### 4. Operational Risks
Risks during deployment and operation:
- Compromised software updates
- Malicious patches
- Supply chain attacks via managed services
- Cloud provider security incidents
- Third-party data breaches
- Service availability and resilience

## Software Supply Chain Attack Vectors

### Dependency Attacks
- **Malicious Packages**: Attacker publishes malicious code disguised as legitimate package
- **Typosquatting**: Similar package names to trick developers
- **Dependency Confusion**: Exploiting how package managers resolve dependencies
- **Compromised Maintainer**: Attacker gains control of legitimate package
- **Backdoored Updates**: Legitimate package updated with malicious code

### Build System Compromise
- **Compromised CI/CD**: Attacker modifies build pipeline
- **Modified Source Code**: Injection of malicious code pre-build
- **Build Tool Tampering**: Compromised compilers or build tools
- **Artifact Poisoning**: Tampering with built artifacts

### Distribution Attacks
- **Package Repository Compromise**: Attacker modifies packages in repository
- **Man-in-the-Middle**: Intercepting package downloads
- **Update Mechanism Abuse**: Compromising software update systems
- **Code Signing Certificate Theft**: Signing malicious code with legitimate certificate

### Vendor Compromise
- **Upstream Vendor Breach**: Vendor's systems compromised, malicious updates distributed
- **SaaS Provider Compromise**: Hosted service compromised, affecting all customers
- **Cloud Provider Breach**: Infrastructure provider compromised

## Supplier Risk Assessment and Management

### Supplier Evaluation Process

#### 1. Pre-Engagement Assessment
Before engaging with a supplier:
- Security questionnaires and assessments
- Review of security policies and practices
- Security certifications (SOC 2, ISO 27001, etc.)
- Penetration testing or audit results
- Incident response capabilities
- Data handling and protection practices
- Geographic location and regulatory compliance
- Financial stability
- References from other customers

#### 2. Due Diligence
Deeper evaluation for critical suppliers:
- Security audits (on-site or remote)
- Technical security reviews
- Code reviews for software vendors
- [[Penetration Testing]] of vendor solutions
- Review of access controls and authentication
- Data encryption practices
- [[Vulnerability Management]] and [[Patch Management]] processes
- [[Security Monitoring]] capabilities
- Business continuity and disaster recovery plans

#### 3. Contractual Security Requirements
Legal and contractual protections:
- Security requirements and SLAs
- Right to audit clauses
- Incident notification requirements
- Data protection and privacy terms
- Liability and indemnification
- Compliance with regulations
- Subcontractor management requirements
- Termination and data return provisions

#### 4. Ongoing Monitoring
Continuous assessment of supplier security:
- Regular security assessments (annual or quarterly)
- Monitoring for security incidents and breaches
- Tracking vendor security posture changes
- Review of [[Third-Party Dependency Scanning|vulnerability]] disclosures
- Compliance attestation reviews
- Service availability and performance monitoring
- Relationship management and communication

#### 5. Incident Response Coordination
Preparing for supplier-related incidents:
- Defined incident notification procedures
- Contact information for security teams
- Coordinated response processes
- Communication protocols
- Forensic investigation coordination
- Customer notification procedures

### Risk Categorization
Classifying suppliers by risk level:

**Critical Suppliers**:
- Access to sensitive data
- Critical business functions
- Integration with core systems
- High volume of data processing
- Requires most rigorous assessment

**High-Risk Suppliers**:
- Access to important systems
- Moderate data exposure
- Important business functions
- Requires regular assessment

**Medium/Low-Risk Suppliers**:
- Limited access
- Non-sensitive functions
- Minimal data exposure
- Lighter assessment process

## Software Bill of Materials (SBOM)

An SBOM is a formal, machine-readable inventory of software components:

### Purpose
- Visibility into all dependencies
- Rapid response to vulnerability disclosures (e.g., Log4Shell)
- License compliance tracking
- Supply chain transparency
- Regulatory compliance

### SBOM Standards
- **SPDX** (Software Package Data Exchange): Linux Foundation standard
- **CycloneDX**: OWASP standard designed for security use cases
- **SWID Tags**: ISO/IEC standard for software identification

### SBOM Generation
- Generated during build process
- Include direct and transitive dependencies
- Version information for all components
- License information
- Supplier/author information
- Cryptographic hashes for verification

### SBOM Usage
- Vulnerability management ([[Third-Party Dependency Scanning]])
- Incident response (quickly identify if vulnerable component is used)
- License compliance
- Procurement and risk assessment
- Regulatory compliance

## Secure Software Development Framework (SSDF)

NIST guidance for secure software supply chain:

### Key Practices
1. **Prepare the Organization**: Security culture, roles, and processes
2. **Protect the Software**: [[Secure Design Review]], secure coding, [[Static Code Analysis]]
3. **Produce Well-Secured Software**: Security testing, [[Penetration Testing]]
4. **Respond to Vulnerabilities**: [[Vulnerability Management]], incident response

## Supply Chain Security Controls

### 1. Dependency Management
- Maintain inventory of all dependencies (SBOM)
- [[Third-Party Dependency Scanning]] for vulnerabilities
- Approve dependencies before use
- Pin dependency versions (don't use "latest")
- Monitor for security advisories
- Regular dependency updates
- Remove unused dependencies

### 2. Source Code Verification
- Verify package integrity (checksums, signatures)
- Use trusted package sources
- Lock files for reproducible builds
- Dependency signature verification
- Code review for new dependencies

### 3. Build Security
- Secure and monitored build environments
- Build reproducibility
- Sign build artifacts
- Isolate build systems from production
- Audit build process
- Use trusted base images for containers

### 4. Access Control
- Limit vendor access to minimum necessary
- Multi-factor authentication for vendor access
- Just-in-time access for vendors
- Monitor vendor access and activities
- Regular access reviews
- Revoke access when no longer needed

### 5. Network Segmentation
- Isolate vendor access
- Limit lateral movement
- Dedicated VPN or VDI for vendors
- Microsegmentation for critical systems

### 6. Data Protection
- Encrypt data shared with vendors
- Minimize data exposed to vendors
- Use data masking or anonymization
- Monitor data transfers
- Data loss prevention (DLP) controls

### 7. Continuous Monitoring
- Monitor vendor access and activities
- [[Security Monitoring]] for suspicious behavior
- Alert on anomalies from vendor connections
- Track vendor security incidents
- Vendor risk scoring and dashboards

## Integration with Secure SDLC

Supply chain security touches all phases:
- **[[Software Security Requirements]]**: Include supply chain security requirements
- **[[Threat Modeling]]**: Consider supply chain attack vectors
- **[[Secure Design Review]]**: Evaluate third-party integrations
- **[[Attack Surface Evaluation]]**: Include vendor access in attack surface
- **[[Static Code Analysis]]**: Scan dependencies for vulnerabilities
- **[[Third-Party Dependency Scanning]]**: Core component of supply chain security
- **[[Penetration Testing]]**: Test third-party integrations
- **[[Security Monitoring]]**: Monitor vendor access and behavior
- **[[Vulnerability Management]]**: Track third-party vulnerabilities
- **[[Patch Management]]**: Update third-party components
- **[[Change Management]]**: Control changes involving third parties

## Regulatory and Compliance

Increasing regulatory focus on supply chain security:
- **Executive Order 14028** (US): Software supply chain security requirements
- **NIST SSDF**: Framework for secure software development
- **SOC 2**: Third-party management controls
- **ISO 27001**: Supplier relationships security
- **GDPR**: Third-party processor requirements
- **PCI DSS**: Third-party service provider requirements
- **CMMC**: Supply chain risk management
- **FDA**: Software Bill of Materials for medical devices

## Vendor Security Rating Services

Third-party services that assess vendor security:
- **BitSight**: Security ratings based on external observations
- **SecurityScorecard**: Vendor risk management platform
- **RiskRecon**: Cyber risk assessment
- **UpGuard**: Third-party risk management
- **Prevalent**: Third-party risk management platform

## Best Practices

### 1. Know Your Dependencies
- Maintain comprehensive SBOM
- Understand direct and transitive dependencies
- Track license and security information
- Regular inventory updates

### 2. Assess Before Adoption
- Security review before adding dependencies
- Evaluate maintainer reputation and activity
- Check for known vulnerabilities
- Review license compatibility
- Consider alternatives

### 3. Minimize Dependencies
- Use only necessary dependencies
- Avoid bloated libraries for simple needs
- Consider implementing simple functionality internally
- Remove unused dependencies

### 4. Keep Dependencies Updated
- Regular dependency updates
- Automated dependency update tools (Dependabot, Renovate)
- Monitor security advisories
- Balance updates with stability

### 5. Verify Integrity
- Use package signatures and checksums
- Verify from trusted sources
- Use private package mirrors when possible
- Implement software attestation

### 6. Manage Vendor Risk
- Risk-based vendor assessment
- Continuous monitoring of vendor posture
- Contractual security requirements
- Regular vendor reviews
- Incident response coordination

### 7. Secure the Build Pipeline
- Hardened build environments
- Build process monitoring and logging
- Code signing and artifact verification
- Reproducible builds
- Isolated build systems

### 8. Plan for Incidents
- Incident response plan for supply chain attacks
- Vendor incident notification procedures
- Rapid vulnerability assessment (enabled by SBOM)
- Communication plans

## Metrics

Key metrics for supply chain security:
- Number of third-party dependencies
- Percentage with known vulnerabilities
- Vendor security assessment coverage
- Time to update vulnerable dependencies
- Number of critical vendors
- Vendor security incident rate
- SBOM generation coverage
- Dependency freshness (average age)

## References
1. [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/Projects/ssdf)
2. [OWASP Software Component Verification Standard](https://owasp.org/www-project-software-component-verification-standard/)
3. [CISA Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom)
4. [NIST SP 800-161: Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final)
5. [Cloud Security Alliance: Managing Third-Party Security Risk](https://cloudsecurityalliance.org/)

#### Tags
#security #supply_chain #third_party_risk #vendor_management #sbom #dependencies #sdlc
