Created: 2025-12-04 15:45
#note

Static code analysis (also known as Static Application Security Testing or SAST) is the process of analyzing source code, bytecode, or binaries without executing the program to identify security vulnerabilities, coding errors, and violations of coding standards. It's a critical practice in the [[Secure SDLC]] implementation phase.

## Overview

Unlike dynamic testing that requires running the application, static analysis examines the codebase at rest. This enables security teams to identify vulnerabilities early in the development process, often as code is being written. Modern static analysis tools can integrate directly into IDEs and CI/CD pipelines, providing immediate feedback to developers.

## Key Benefits

- **Early Detection**: Identifies vulnerabilities before code reaches production
- **Comprehensive Coverage**: Can analyze 100% of code paths, including rarely executed ones
- **Cost Efficiency**: Finding and fixing issues early is exponentially cheaper than post-deployment remediation
- **Scalability**: Automated tools can analyze large codebases quickly
- **Compliance**: Demonstrates security due diligence for regulatory requirements
- **Education**: Helps developers learn secure coding practices through immediate feedback

## Types of Vulnerabilities Detected

### OWASP Top 10
- Injection flaws (SQL, Command, LDAP, XPath)
- Broken authentication
- Sensitive data exposure
- XML external entities (XXE)
- Broken access control
- Security misconfiguration
- Cross-site scripting (XSS)
- Insecure deserialization
- Using components with known vulnerabilities
- Insufficient logging and monitoring

### Common Coding Issues
- Buffer overflows
- Race conditions
- Resource leaks
- Null pointer dereferences
- Integer overflows
- Hardcoded credentials
- Weak cryptography
- Path traversal
- Improper error handling
- Insecure random number generation

## Analysis Techniques

### 1. Pattern Matching
- Searches for known vulnerability patterns
- Fast and low false-positive rate
- Limited to known patterns
- Example: Detecting hardcoded passwords like `password = "admin123"`

### 2. Data Flow Analysis
- Tracks how data moves through the application
- Identifies taint propagation (untrusted input reaching sensitive operations)
- Example: User input flowing to SQL query without sanitization
- More sophisticated but higher false-positive rate

### 3. Control Flow Analysis
- Analyzes possible execution paths
- Identifies dead code and unreachable statements
- Detects authorization checks that can be bypassed

### 4. Semantic Analysis
- Understands code meaning and intent
- Detects logical errors and design flaws
- Most sophisticated but computationally intensive

## Integration Points

### IDE Integration
- Real-time feedback as code is written
- Immediate visibility into introduced vulnerabilities
- Low friction for developers
- Examples: SonarLint, Snyk Code IDE plugins

### Pre-commit Hooks
- Scans code before it's committed to version control
- Prevents vulnerable code from entering the repository
- Can block commits if critical issues are found

### CI/CD Pipeline
- Automated scanning on every build or pull request
- Gates preventing vulnerable code from progressing
- Integration with code review processes
- Trend analysis across builds

### Scheduled Scans
- Regular deep scans of entire codebase
- Identifies issues from updated vulnerability databases
- Catches issues introduced by [[Third-Party Dependency Scanning|dependency]] updates

## Popular Tools

### Open Source
- **SonarQube**: Comprehensive code quality and security platform
- **Semgrep**: Fast, customizable static analysis with simple rule syntax
- **Bandit**: Python-specific security linter
- **Brakeman**: Ruby on Rails security scanner
- **FindBugs/SpotBugs**: Java bytecode analyzer
- **ESLint**: JavaScript linter with security plugins

### Commercial
- **Checkmarx**: Enterprise SAST platform
- **Veracode**: Cloud-based application security platform
- **Fortify Static Code Analyzer**: Comprehensive SAST tool
- **Snyk Code**: Developer-first static analysis
- **GitHub Advanced Security**: Native GitHub integration with CodeQL

## Best Practices

### 1. Shift Left
- Integrate early in development process
- Provide feedback in IDE when possible
- Make security visible to developers

### 2. Tune and Customize
- Configure rules based on your technology stack
- Adjust severity levels to match organizational risk tolerance
- Create custom rules for organization-specific patterns
- Reduce false positives through tuning

### 3. Manage False Positives
- Review and triage findings
- Mark false positives to avoid alert fatigue
- Document why issues are considered false positives
- Regularly review dismissed findings

### 4. Prioritize Findings
- Focus on exploitable vulnerabilities first
- Consider context (public-facing vs internal)
- Align with [[Threat Modeling]] findings
- Use risk-based prioritization

### 5. Track and Measure
- Monitor trends in vulnerability counts
- Measure time to remediation
- Track false positive rates
- Assess developer engagement with findings

### 6. Combine with Other Techniques
- Static analysis alone is insufficient
- Use with [[Third-Party Dependency Scanning]]
- Validate with [[Penetration Testing]]
- Monitor in production with [[Security Monitoring]]

## Limitations

- **False Positives**: Can generate alerts for non-issues
- **False Negatives**: May miss certain vulnerability types
- **Configuration Issues**: Doesn't detect misconfigurations in deployment
- **Business Logic**: Struggles with business logic flaws
- **Runtime Issues**: Can't detect vulnerabilities only present at runtime
- **Context Limitations**: May lack full understanding of application context
- **Performance**: Deep analysis can be time-consuming

## Complementary Approaches

Static analysis should be combined with:
- **[[Third-Party Dependency Scanning]]**: Identifies vulnerabilities in external libraries
- **Dynamic Application Security Testing (DAST)**: Tests running applications
- **[[Penetration Testing]]**: Manual security testing by experts
- **Code Review**: Human examination of code for security issues
- **Interactive Application Security Testing (IAST)**: Combines static and dynamic approaches

## Developer Adoption Strategies

### Reduce Friction
- Integrate into existing workflows
- Provide clear, actionable feedback
- Automate as much as possible
- Make findings easy to understand and fix

### Education and Training
- Explain why findings matter
- Provide secure coding examples
- Link to remediation guidance
- Celebrate security improvements

### Gamification
- Track security metrics per team/developer
- Recognize security champions
- Create friendly competition around reducing vulnerabilities

### Make it Fast
- Optimize scan times for quick feedback
- Use incremental scanning where possible
- Balance depth of analysis with speed

## Integration with Secure SDLC

Static code analysis connects to:
- **[[Software Security Requirements]]**: Validates requirements are implemented securely
- **[[Secure Design Review]]**: Confirms design decisions don't introduce vulnerabilities
- **[[Threat Modeling]]**: Verifies identified threats are mitigated
- **[[Change Management]]**: Scans before deployment to production
- **[[Vulnerability Management]]**: Feeds into overall vulnerability tracking

## Metrics

Key metrics to track:
- Vulnerability density (vulnerabilities per 1000 lines of code)
- Mean time to remediation (MTTR)
- False positive rate
- Security debt (accumulated unfixed vulnerabilities)
- Scan coverage (percentage of codebase analyzed)
- Critical vulnerabilities in production

## References
1. [OWASP Source Code Analysis Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools)
2. [NIST Software Security Assurance](https://csrc.nist.gov/projects/ssdf)
3. [SEI CERT Coding Standards](https://wiki.sei.cmu.edu/confluence/display/seccode)
4. [Static Analysis in the Software Development Lifecycle](https://www.synopsys.com/software-integrity/software-security-services/software-security-research/static-analysis.html)

#### Tags
#security #static_analysis #sast #code_quality #vulnerability #sdlc
