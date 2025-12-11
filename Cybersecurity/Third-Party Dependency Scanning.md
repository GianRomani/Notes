Created: 2025-12-04 15:45
#note

Third-party dependency scanning (also known as Software Composition Analysis or SCA) is the process of identifying, cataloging, and analyzing external libraries, frameworks, and components used in an application to detect known vulnerabilities, license compliance issues, and outdated versions. It's a critical component of [[Secure SDLC]] and [[Supply Chain Security]].

## Overview

Modern applications typically consist of 70-90% third-party code through libraries, frameworks, and packages. While these dependencies accelerate development, they also introduce security risks. A vulnerability in a widely-used library can affect thousands of applications simultaneously, making dependency scanning essential for maintaining security posture.

## Why It Matters

### Security Risks
- Known vulnerabilities (CVEs) in dependencies
- Transitive dependencies (dependencies of dependencies) with vulnerabilities
- Unmaintained or abandoned libraries
- Malicious packages (supply chain attacks)
- Zero-day vulnerabilities in popular packages

### Compliance and Legal
- License compatibility issues (GPL, MIT, Apache, etc.)
- Export control restrictions
- Intellectual property concerns
- Regulatory requirements (e.g., FDA for medical devices, GDPR)

### Operational Risks
- Outdated dependencies with bugs
- Performance issues
- Compatibility problems
- Support and maintenance burden

## What Gets Scanned

### Direct Dependencies
Explicitly declared dependencies in:
- `package.json` (Node.js/JavaScript)
- `pom.xml` (Java/Maven)
- `requirements.txt` or `Pipfile` (Python)
- `Gemfile` (Ruby)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `packages.config` or `.csproj` (C#/.NET)

### Transitive Dependencies
Indirect dependencies pulled in by direct dependencies, which can:
- Introduce unexpected vulnerabilities
- Create complex dependency trees
- Be difficult to track manually
- Cause version conflicts

### Container Images
For containerized applications:
- Base image vulnerabilities
- OS-level packages
- Application dependencies within containers

### Binary Analysis
For closed-source or compiled components:
- Identifying embedded third-party libraries
- Detecting known vulnerable code patterns
- Fingerprinting commercial components

## Vulnerability Databases

Scanning tools reference multiple databases:

### CVE (Common Vulnerabilities and Exposures)
- Industry-standard vulnerability naming
- Maintained by MITRE
- Referenced by all major tools

### NVD (National Vulnerability Database)
- NIST's vulnerability database
- Includes CVSS scores and detailed information
- Updates CVE records with analysis

### GitHub Advisory Database
- Community-maintained database
- Specific to GitHub ecosystems
- Includes security advisories for packages

### Ecosystem-Specific Databases
- npm Security Advisories (JavaScript)
- PyPI Safety DB (Python)
- RubySec (Ruby)
- Rust Security Advisory Database

## Scanning Approaches

### 1. Manifest Analysis
- Analyzes dependency declaration files
- Fast and lightweight
- May miss transitive dependencies without resolution
- Example: Scanning `package.json` without `package-lock.json`

### 2. Dependency Resolution
- Resolves complete dependency tree
- Includes transitive dependencies
- More accurate but requires package manager
- Example: Running `npm install` to generate lock file

### 3. Binary Scanning
- Analyzes compiled artifacts or deployed applications
- Detects dependencies even without source code
- Useful for legacy applications or third-party binaries
- Can identify embedded libraries

### 4. Runtime Analysis
- Monitors actual loaded dependencies during execution
- Identifies only actively used components
- Reduces false positives from unused dependencies
- More complex to implement

## Integration Points

### Development Environment
- IDE plugins for real-time feedback
- Pre-commit hooks to prevent vulnerable dependencies
- Local scanning before pushing code

### CI/CD Pipeline
- Automated scanning on every build
- Pull request checks and gates
- Integration with code review workflows
- Blocking deployments with critical vulnerabilities

### Repository Management
- GitHub Dependabot
- GitLab Dependency Scanning
- Artifact repository scanning (Nexus, Artifactory)

### Production Monitoring
- Continuous monitoring of deployed applications
- Runtime dependency analysis
- Integration with [[Security Monitoring]] systems

## Popular Tools

### Open Source
- **OWASP Dependency-Check**: Multi-language support, widely used
- **Snyk Open Source**: Developer-friendly, good database
- **Trivy**: Container and filesystem scanner
- **Grype**: Fast vulnerability scanner for containers
- **npm audit / yarn audit**: Built into Node.js package managers
- **pip-audit**: Python dependency checker
- **bundler-audit**: Ruby gem scanner

### Commercial
- **Snyk**: Comprehensive SCA with developer-first approach
- **WhiteSource (Mend)**: Enterprise SCA platform
- **Black Duck**: Deep binary analysis and license compliance
- **Sonatype Nexus Lifecycle**: Integration with artifact repository
- **JFrog Xray**: Artifact analysis and impact analysis

## Remediation Strategies

### 1. Update to Fixed Version
- Simplest approach when available
- Check release notes for breaking changes
- Test thoroughly after updating
- May require code changes for major version updates

### 2. Find Alternative Package
- When maintainer has abandoned the package
- When license is incompatible
- Requires effort to refactor code
- May introduce new risks

### 3. Patch or Fork
- Apply security patches to current version
- Maintain internal fork with fixes
- High maintenance burden
- Consider contributing patch upstream

### 4. Remove Dependency
- Eliminate if functionality not needed
- Replace with internal implementation
- Reduces [[Attack Surface Evaluation|attack surface]]
- Can be time-consuming

### 5. Compensating Controls
- When updates aren't possible (legacy systems)
- Add input validation or sanitization
- Network segmentation
- Web Application Firewall rules
- Document as accepted risk in [[Vulnerability Management]]

## Best Practices

### 1. Scan Regularly
- Integrate into CI/CD pipeline
- Schedule periodic scans of production systems
- Monitor for new CVEs affecting existing dependencies
- Automate where possible

### 2. Prioritize Remediation
- Focus on exploitable vulnerabilities
- Consider CVSS score and exploitability
- Assess whether vulnerable code paths are used
- Align with [[Threat Modeling]] and [[Attack Surface Evaluation]]

### 3. Maintain Inventory
- Keep Software Bill of Materials (SBOM)
- Track all dependencies and versions
- Document license information
- Update as dependencies change

### 4. Establish Policies
- Define acceptable licenses
- Set vulnerability severity thresholds
- Establish SLAs for remediation
- Require security review for new dependencies

### 5. Monitor Transitive Dependencies
- Don't focus only on direct dependencies
- Understand the full dependency tree
- Use lock files to ensure reproducible builds
- Be aware of dependency confusion attacks

### 6. Stay Informed
- Subscribe to security advisories
- Follow security researchers and bulletins
- Monitor ecosystem-specific security channels
- Participate in security communities

## Challenges

### False Positives
- Vulnerabilities in unused code paths
- CVEs that don't apply to your usage
- Requires manual review and triaging

### Vulnerability Overload
- Large applications can have hundreds of findings
- Alert fatigue can lead to ignoring real issues
- Need risk-based prioritization

### Breaking Changes
- Updates may introduce API changes
- Testing effort for each update
- Balance between security and stability

### Transitive Dependencies
- Limited control over indirect dependencies
- Dependency conflicts
- Version pinning vs staying current

### License Compliance
- Complex license compatibility rules
- Legal review requirements
- Business constraints on certain licenses

## Integration with Secure SDLC

Dependency scanning connects to:
- **[[Software Security Requirements]]**: Define acceptable dependency policies
- **[[Threat Modeling]]**: Consider third-party risks in threat model
- **[[Secure Design Review]]**: Evaluate security of chosen dependencies
- **[[Static Code Analysis]]**: Combined analysis for comprehensive coverage
- **[[Penetration Testing]]**: Validate that vulnerabilities aren't exploitable
- **[[Vulnerability Management]]**: Feed findings into overall vulnerability tracking
- **[[Patch Management]]**: Coordinate dependency updates with patching
- **[[Supply Chain Security]]**: Core component of supply chain risk management

## Software Bill of Materials (SBOM)

An SBOM is a formal, machine-readable inventory of components:

### Benefits
- Enables rapid response to new vulnerabilities
- Supports compliance and audit requirements
- Facilitates license management
- Improves supply chain transparency

### Standards
- SPDX (Software Package Data Exchange)
- CycloneDX
- SWID (Software Identification Tags)

### Generation
- Most SCA tools can generate SBOMs
- Should be updated with each release
- Include transitive dependencies
- Document version and licensing information

## Metrics

Key metrics to track:
- Number of dependencies (direct and transitive)
- Known vulnerabilities by severity
- Mean time to remediation (MTTR)
- Dependency freshness (time since last update)
- License compliance rate
- Vulnerability introduction rate

## References
1. [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
2. [NIST Software Supply Chain Security](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/software-supply-chain-security-guidance)
3. [SBOM Standards and Formats](https://www.cisa.gov/sbom)
4. [Snyk State of Open Source Security Report](https://snyk.io/reports/open-source-security/)

#### Tags
#security #dependencies #sca #supply_chain #vulnerability #sdlc
