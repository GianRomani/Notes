Created: 2025-12-15 15:45
#note

Security misconfiguration occurs when security settings are improperly defined, implemented, or maintained, leaving systems vulnerable to attacks. Part of OWASP Top 10 (A05:2021), it's one of the most common and preventable security issues. Unlike code-level vulnerabilities, these are errors in how systems are configured and set up across the entire [[Secure SDLC]] lifecycle.

## Common Misconfigurations

### Default Settings
- Unchanged default credentials (admin/admin)
- Default ports and services enabled
- Sample applications not removed
- Overly permissive default security settings

### Unnecessary Features
- Unused services running
- Debug features in production
- Administrative interfaces publicly accessible
- Directory listing enabled
- Verbose error messages exposing system details

### Missing Security Headers
- No HSTS (HTTP Strict Transport Security)
- Missing CSP (Content Security Policy)
- Absent X-Frame-Options
- Missing X-Content-Type-Options
- Inadequate CORS configuration

### Access Control Issues
- Overly permissive file permissions
- World-readable sensitive files
- Insufficient network segmentation
- Cloud storage buckets publicly accessible
- Databases accessible from internet

### Outdated Software
- Unpatched systems and applications
- End-of-life software in use
- Inconsistent [[Patch Management]]

## Root Causes

- **Organizational**: Lack of awareness, time pressure, insufficient training
- **Technical**: Insecure defaults, configuration drift, manual processes
- **Process**: No baselines, inadequate testing, bypassed [[Change Management]]

## Impact

- Unauthorized access and data breaches
- Complete system compromise
- Lateral movement opportunities
- Service disruption
- Compliance violations

## Detection

### Automated Scanning
- Configuration scanners: Lynis, OpenSCAP, Nessus
- CSPM tools: Prisma Cloud, Wiz, Orca
- Container security: Trivy, Clair, Anchore
- Web scanners: OWASP ZAP, Burp Suite
- [[Static Code Analysis]] for infrastructure-as-code

### Manual Methods
- Configuration audits
- [[Secure Design Review]] including configuration
- Security checklists against CIS Benchmarks
- [[Penetration Testing]]

## Prevention

### Secure Baselines
- Define secure configuration standards
- Use CIS Benchmarks and NIST guidelines
- Version control all configurations
- Document and justify deviations

### Automation
- Infrastructure-as-Code (Terraform, CloudFormation, Ansible)
- Configuration management (Puppet, Chef, SaltStack)
- Automated deployment pipelines
- Policy-as-code enforcement

### Hardening
- Remove unnecessary features
- Change default credentials immediately
- Disable default accounts
- Use secure protocols (HTTPS, SSH)
- Implement principle of least privilege

### Continuous Validation
- Configuration drift detection
- Automated compliance scanning
- Regular audits
- [[Security Monitoring]] integration

## Security Headers Example

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

## Integration with Secure SDLC

- **Requirements**: Define in [[Software Security Requirements]]
- **Design**: Include in [[Threat Modeling]] and [[Secure Design Review]]
- **Implementation**: Use secure baselines, IaC, peer reviews
- **Testing**: Automated scanning, [[Penetration Testing]]
- **Deployment**: [[Change Management]], pre-deployment checks
- **Operations**: [[Security Monitoring]], [[Vulnerability Management]]

## Best Practices

- Automate configuration management
- Version control all configurations
- Test in non-production first
- Continuous monitoring and drift detection
- Defense in depth with layered controls
- Regular team training

## References
- [OWASP Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
- [NIST Security Configuration Checklists](https://csrc.nist.gov/projects/security-configuration-checklists)

#### Tags
#security #misconfiguration #owasp_top_10 #configuration_management #sdlc
