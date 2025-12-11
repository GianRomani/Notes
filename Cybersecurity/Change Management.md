Created: 2025-12-04 15:45
#note

Change management is the systematic approach to proposing, reviewing, approving, implementing, and documenting changes to IT systems and infrastructure. From a security perspective, it ensures that modifications don't introduce vulnerabilities, that security controls remain effective, and that changes are traceable and reversible. It's a critical control in the [[Secure SDLC]] deployment and operations phases.

## Overview

Uncontrolled changes are a leading cause of security incidents and system outages. Change management provides governance and oversight to ensure changes are:
- Necessary and beneficial
- Properly reviewed for security implications
- Tested before deployment
- Documented and traceable
- Reversible if issues arise
- Coordinated to minimize disruption

Security considerations must be integrated throughout the change management process, not treated as an afterthought.

## Types of Changes

### Standard Changes
- Pre-approved, low-risk, routine changes
- Follow established procedures
- Minimal review required
- Examples: [[Patch Management|routine security patches]], certificate renewals, adding users
- Still require documentation and tracking

### Normal Changes
- Most common type of change
- Requires assessment, testing, and approval
- Goes through Change Advisory Board (CAB)
- Examples: Application updates, configuration changes, infrastructure modifications
- Full change management process

### Emergency Changes
- Urgent changes to address critical issues
- Expedited approval process
- May have reduced testing due to time constraints
- Requires post-implementation review
- Examples: Critical [[Vulnerability Management|vulnerability]] patches, security incident response, system outages

### Major Changes
- Significant impact or risk
- Extensive testing and review
- Senior leadership approval
- May require external parties
- Examples: Data center migration, major application upgrades, architecture changes

## Security-Relevant Changes

Changes that have security implications:
- Application code deployments
- Infrastructure modifications (network, servers, cloud)
- Security tool and control changes
- Access control and permission updates
- Firewall and security policy changes
- Encryption and key management changes
- Third-party integrations ([[Supply Chain Security]])
- Configuration changes
- [[Patch Management|Security patches]]
- Certificate and credential updates

## Change Management Process

### 1. Change Request (RFC - Request for Change)
Initiating the change:
- **Description**: What is changing and why
- **Justification**: Business need or security requirement
- **Risk Assessment**: Potential security and operational risks
- **Impact Analysis**: What systems and users are affected
- **Rollback Plan**: How to reverse if needed
- **Testing Plan**: How change will be validated
- **Schedule**: Proposed implementation time
- **Dependencies**: Related systems or changes
- **Security Review**: Required for security-relevant changes

### 2. Assessment and Review
Evaluating the proposed change:
- Technical feasibility review
- Security impact assessment (security team review)
- Risk analysis (aligns with [[Threat Modeling]])
- Resource requirements
- Testing requirements
- Compliance implications
- Business impact assessment
- Conflict check with other changes

### 3. Approval
Obtaining authorization to proceed:
- **Standard Changes**: Automatic or delegated approval
- **Normal Changes**: CAB or change manager approval
- **Emergency Changes**: Emergency CAB (ECAB) or designated authority
- **Major Changes**: Senior leadership and stakeholders

Change Advisory Board typically includes:
- Change manager
- Security representative
- Operations team
- Application owners
- Business representatives

### 4. Implementation Planning
Preparing for deployment:
- Detailed implementation steps
- Resource allocation
- Communication plan (stakeholder notification)
- Maintenance window scheduling
- Backup and rollback procedures
- Monitoring plan
- Success criteria

### 5. Testing
Validating changes before production:
- Development/test environment deployment
- Functional testing
- Security testing (validate no new vulnerabilities from [[Static Code Analysis]], [[Third-Party Dependency Scanning]])
- Performance testing
- Integration testing
- Rollback testing
- Documentation of test results

### 6. Implementation
Deploying the change:
- Pre-implementation backup
- Follow documented procedures
- Monitor during deployment
- Document actual steps taken
- Note any deviations from plan
- Immediate issue escalation

### 7. Verification
Confirming successful deployment:
- Validate change implemented correctly
- Confirm systems functioning as expected
- Security validation (no new vulnerabilities, controls still effective)
- User acceptance testing if applicable
- Update [[Security Monitoring]] for changed environment
- Update [[Vulnerability Management]] tracking

### 8. Post-Implementation Review
Learning and documenting:
- Was change successful?
- Any issues encountered?
- Was rollback needed?
- Documentation complete and accurate?
- Lessons learned
- Update procedures if needed
- Close change ticket

## Security Considerations in Change Management

### Pre-Change Security Review
Questions to ask:
- Does this change affect the [[Attack Surface Evaluation|attack surface]]?
- Are we introducing new vulnerabilities?
- Will existing security controls remain effective?
- Does this align with [[Software Security Requirements]]?
- Are we following [[Secure Design Review]] principles?
- Have we scanned for vulnerabilities ([[Static Code Analysis]], [[Third-Party Dependency Scanning]])?
- What are the security risks if rollback is needed?
- Are security logs and monitoring still effective post-change?

### Security Testing Requirements
Changes should be tested for:
- New vulnerabilities introduced
- Security control effectiveness
- Authentication and authorization still working
- Encryption and data protection maintained
- Audit logging still functioning
- [[Penetration Testing]] for significant changes
- Compliance requirements still met

### Security in Rollback
Security implications of rolling back:
- Does rollback reintroduce vulnerabilities?
- Will security monitoring detect the rollback?
- Are backups encrypted and protected?
- Can attackers exploit the rollback window?
- Are credentials rotated if compromised?

## Change Management Tools

### IT Service Management (ITSM) Platforms
- **ServiceNow**: Comprehensive change management
- **BMC Remedy**: Enterprise ITSM platform
- **Jira Service Management**: Agile-friendly change management
- **Cherwell**: ITIL-aligned change management

### DevOps and CI/CD Integration
- **GitHub/GitLab**: Pull request workflows
- **Jenkins**: Pipeline-based change deployment
- **Azure DevOps**: Integrated change management
- **Terraform/Ansible**: Infrastructure as Code change tracking

### Security-Specific Tools
- Change detection and monitoring tools
- Configuration management databases (CMDB)
- Security Information and Event Management ([[Security Monitoring|SIEM]])
- File Integrity Monitoring (FIM)

## Metrics and KPIs

### Process Metrics
- **Change Success Rate**: Percentage of changes implemented successfully
- **Emergency Change Rate**: Percentage of emergency vs planned changes
- **Change Velocity**: Number of changes per period
- **Rollback Rate**: Percentage of changes requiring rollback
- **Approval Time**: Time from request to approval

### Security Metrics
- **Security Review Coverage**: Percentage of changes receiving security review
- **Security-Related Rollbacks**: Changes rolled back due to security issues
- **Vulnerability Introduction Rate**: New vulnerabilities per change
- **Time to Security Approval**: Delays due to security review
- **Security Incidents from Changes**: Incidents caused by changes

### Compliance Metrics
- **Process Compliance**: Changes following proper procedures
- **Documentation Completeness**: Properly documented changes
- **Unauthorized Changes**: Changes bypassing process
- **Audit Findings**: Issues found in change management audits

## Common Pitfalls

### Bypassing Process
- "Emergency" changes that aren't emergencies
- Undocumented changes
- Changes in production without testing
- Shadow IT changes
- Risk: Introduces vulnerabilities, breaks systems, untraceable

### Inadequate Testing
- Skipping security testing
- Testing only "happy path"
- Not testing rollback
- Inadequate test environment
- Risk: Breaks production, introduces vulnerabilities

### Poor Documentation
- Incomplete change records
- Undocumented implementation steps
- Missing rollback procedures
- No lessons learned captured
- Risk: Can't troubleshoot, repeat mistakes

### Insufficient Security Review
- Security team not involved
- Superficial security assessment
- No vulnerability scanning
- Assuming change is secure
- Risk: Vulnerabilities in production

### Change Fatigue
- Too many changes too quickly
- Insufficient time for review
- Rubber-stamping approvals
- Skipping steps due to volume
- Risk: Missing critical issues

## Best Practices

### 1. Automate Where Possible
- Automated change request creation
- Automated security scanning (pre-deployment)
- Automated testing in CI/CD
- Automated notifications and approvals
- Automated documentation

### 2. Risk-Based Approach
- Tailor rigor to risk level
- Standard changes for routine, low-risk activities
- Intensive review for high-risk changes
- Emergency process for genuine emergencies
- Align with [[Threat Modeling]] and risk appetite

### 3. Integrate Security Early
- Security review in change assessment
- Automated security scanning in CI/CD
- Security representative on CAB
- Security testing before approval
- Security verification post-implementation

### 4. Clear Ownership and Accountability
- Designated change owners
- Clear approval authorities
- Defined roles and responsibilities
- Accountability for outcomes

### 5. Comprehensive Testing
- Representative test environments
- Security testing requirements
- Rollback testing
- Performance and functionality testing
- Document test results

### 6. Effective Communication
- Notify affected stakeholders
- Clear maintenance window communication
- Status updates during implementation
- Post-implementation communication
- Transparent about issues and delays

### 7. Continuous Improvement
- Regular process review
- Learn from failures
- Update procedures based on lessons learned
- Metrics-driven optimization
- Balance control with agility

### 8. Documentation Standards
- Consistent change request format
- Complete implementation documentation
- Rollback procedures documented
- Post-implementation review captured
- Searchable change history

## Integration with Secure SDLC

Change management connects to all security practices:
- **[[Software Security Requirements]]**: Changes must meet security requirements
- **[[Threat Modeling]]**: Assess if changes affect threat model
- **[[Secure Design Review]]**: Architectural changes reviewed
- **[[Attack Surface Evaluation]]**: Changes may expand attack surface
- **[[Static Code Analysis]]**: Code changes scanned before deployment
- **[[Third-Party Dependency Scanning]]**: Dependency updates tracked
- **[[Penetration Testing]]**: Major changes may require pen testing
- **[[Vulnerability Management]]**: Remediation changes tracked
- **[[Patch Management]]**: Patches deployed through change management
- **[[Security Monitoring]]**: Monitor for issues post-change
- **[[Supply Chain Security]]**: Third-party changes assessed

## DevOps and Agile Considerations

### Adapting Change Management
Traditional change management can seem at odds with DevOps:
- High frequency of changes
- Need for speed and agility
- Automation-first approach
- Continuous delivery

### Modern Approach
- **Automated Gates**: Security scans, tests as approval gates
- **Pull Request Workflows**: Peer review and automated checks
- **Infrastructure as Code**: Version-controlled infrastructure changes
- **Feature Flags**: Deploy dark, enable through configuration
- **Gradual Rollout**: Canary deployments, blue-green deployments
- **Monitoring-Driven**: Robust [[Security Monitoring|monitoring]] replaces some testing

The goal is "auditability and oversight without bureaucracy."

## Compliance Requirements

Many regulations require change management:
- **SOC 2**: Change management controls
- **ISO 27001**: Change control procedures
- **PCI DSS**: Change control processes for security-relevant changes
- **HIPAA**: Change control for systems handling PHI
- **NIST CSF**: Configuration change control

## References
1. [ITIL Change Management](https://www.axelos.com/best-practice-solutions/itil)
2. [NIST SP 800-128: Guide for Security-Focused Configuration Management](https://csrc.nist.gov/publications/detail/sp/800-128/final)
3. [CIS Control 3: Data Protection and Control 4: Secure Configuration](https://www.cisecurity.org/controls/)
4. [COBIT Framework: Change Management](https://www.isaca.org/resources/cobit)

#### Tags
#security #change_management #operations #governance #sdlc #devops
