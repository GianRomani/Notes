Created: 2025-12-04 15:45
#note

Patch management is the systematic process of identifying, acquiring, testing, and deploying software updates (patches) to remediate vulnerabilities, fix bugs, and improve functionality. It's a subset of [[Vulnerability Management]] and a critical operational security control in the [[Secure SDLC]] maintenance phase.

## Overview

Software vulnerabilities are continuously discovered in operating systems, applications, firmware, and dependencies. Vendors release patches to address these security issues, but the patch must be properly tested and deployed to actually reduce risk. Effective patch management balances the urgency of security fixes with the need for stability and availability.

## Types of Patches

### Security Patches
- Fix known vulnerabilities (CVEs)
- Highest priority due to exploitation risk
- May require emergency deployment
- Examples: Windows Security Updates, Chrome security releases

### Critical Patches
- Address severe bugs or security issues
- System stability or data integrity impacts
- Urgent but may allow brief testing
- Examples: Database corruption fixes, authentication bypass fixes

### Feature Updates
- Add new functionality
- May include security improvements
- Lower urgency, more extensive testing
- Examples: Windows Feature Updates, major application versions

### Maintenance Patches
- Bug fixes and performance improvements
- Routine updates
- Standard testing and deployment
- Examples: Minor version updates, stability improvements

## Patch Management Lifecycle

### 1. Inventory and Asset Management
Knowing what needs to be patched:
- Comprehensive asset inventory (hardware, software, versions)
- Operating systems and patch levels
- Installed applications
- Firmware versions
- [[Third-Party Dependency Scanning|Third-party dependencies]]
- Cloud resources and managed services

### 2. Patch Monitoring and Detection
Identifying available patches:
- Vendor security bulletins and advisories
- CVE notifications
- Vulnerability scanner findings
- CERT/CSIRT alerts
- [[Security Monitoring]] for active exploitation
- Automated patch detection tools

### 3. Assessment and Prioritization
Determining which patches to deploy and when:
- **Severity**: Critical, High, Medium, Low
- **Exploitability**: Public exploits available? Active attacks?
- **Asset Criticality**: Production vs development, critical vs non-critical
- **Impact**: Will patching cause downtime or breaking changes?
- **Dependencies**: What else might be affected?
- **Vendor Recommendations**: Deployment guidance
- Alignment with [[Vulnerability Management]] priorities

### 4. Testing
Validating patches before production deployment:
- Test in representative environment
- Functional testing (does the application still work?)
- Performance testing (any degradation?)
- Compatibility testing (conflicts with other software?)
- Security validation (does it fix the vulnerability?)
- Rollback procedure testing

### 5. Approval and Scheduling
Coordinating deployment through [[Change Management]]:
- Change request submission
- Risk assessment
- Approval from change advisory board (CAB)
- Schedule maintenance window
- Communicate to stakeholders
- Prepare rollback plan

### 6. Deployment
Applying patches to production systems:
- Phased rollout (pilot group first)
- Automated deployment where possible
- Manual deployment for critical systems
- Monitoring during deployment
- Documentation of what was patched
- Backup before patching

### 7. Verification
Confirming patches are applied successfully:
- Verify patch installation
- Confirm vulnerability is remediated
- Validate system functionality
- Update asset inventory
- Update [[Vulnerability Management]] tracking

### 8. Reporting and Documentation
Maintaining patch records:
- Patch compliance reporting
- Systems at current patch level
- Exceptions and delayed patches
- Patch deployment history
- Post-implementation review

## Patching Strategies

### Immediate/Emergency Patching
- For actively exploited vulnerabilities
- Expedited change management
- Limited testing (regression testing may be deferred)
- Close monitoring post-deployment
- Example: Zero-day exploit being actively used

### Scheduled Maintenance Windows
- Regular patching cycles (monthly, quarterly)
- Predictable for business planning
- Batch multiple patches together
- Full testing cycle
- Example: Microsoft Patch Tuesday

### Continuous Patching
- Deploy patches as soon as testing is complete
- Minimizes exposure window
- Requires mature automation
- Common for cloud-native applications
- DevOps/CI-CD integration

### Risk-Based Patching
- Prioritize based on risk, not just availability
- Use [[Threat Modeling]] and [[Attack Surface Evaluation]]
- Focus on internet-facing and critical systems first
- May defer low-risk patches
- Aligns with [[Vulnerability Management]] priorities

## Patch Management Tools

### Enterprise Patch Management
- **Microsoft WSUS/SCCM**: Windows environment patching
- **Red Hat Satellite**: Linux patch management
- **JAMF**: macOS and iOS device management
- **ManageEngine Patch Manager Plus**: Multi-platform patching
- **Ivanti Patch Management**: Enterprise-scale patch automation

### Cloud and Modern Workloads
- **AWS Systems Manager**: Patch Manager for AWS resources
- **Azure Update Management**: Azure VM patching
- **Google Cloud OS Patch Management**: GCP patching
- **Ansible/Puppet/Chef**: Infrastructure as Code patch automation

### Vulnerability and Patch Management Combined
- **Qualys VMDR**: Vulnerability detection and patch deployment
- **Rapid7 InsightVM**: Integrated vulnerability and patch management
- **Tenable.io**: Vulnerability assessment with patch intelligence

### Container and Application Patching
- Automated container rebuilds with updated base images
- Dependency update tools (Dependabot, Renovate)
- Application-specific patching (browser auto-updates, app stores)

## Challenges

### Technical Challenges
- **Breaking Changes**: Patches may break functionality or compatibility
- **Downtime Requirements**: Some patches require system restarts
- **Legacy Systems**: Old systems may not support new patches
- **Dependency Conflicts**: Patches may conflict with other software
- **Incomplete Coverage**: Not all software has automated patching
- **Testing Burden**: Testing takes time, delaying deployment

### Organizational Challenges
- **Business Impact**: Maintenance windows disrupt business
- **Resource Constraints**: Limited IT staff for testing and deployment
- **Change Resistance**: Fear of breaking production systems
- **Coordination**: Across teams, departments, geographies
- **Compliance Pressure**: Meeting patch SLAs vs stability concerns

### Process Challenges
- **Volume**: Too many patches to process efficiently
- **Prioritization**: Determining what to patch first
- **False Starts**: Patches that are pulled back by vendors
- **Zero-Day Response**: Reacting quickly to active threats
- **Patch Availability**: Vendors slow to release patches

## Best Practices

### 1. Maintain Accurate Inventory
- Automated asset discovery
- Configuration management database (CMDB)
- Track software versions and patch levels
- Include cloud resources and [[Third-Party Dependency Scanning|dependencies]]

### 2. Establish Clear Policies
- Define patch SLAs by severity (Critical: 7 days, High: 30 days, etc.)
- Exception process for systems that can't be patched
- Risk acceptance criteria
- Emergency patching procedures

### 3. Automate Where Possible
- Automated patch detection and assessment
- Automated testing in staging environments
- Automated deployment for low-risk systems
- Automated compliance reporting

### 4. Test Before Deploying
- Maintain representative test environment
- Test patches before production deployment
- Document test results
- Balance testing depth with urgency

### 5. Use Phased Rollout
- Deploy to pilot group first
- Monitor for issues before wider deployment
- Have rollback plan ready
- Gradual expansion to all systems

### 6. Integrate with [[Change Management]]
- All patches go through change control
- Exception process for critical security patches
- Risk assessment for each patch deployment
- Documentation and approval

### 7. Monitor and Verify
- Confirm patches deployed successfully
- Verify vulnerability is remediated
- Monitor for issues post-deployment
- Update tracking systems

### 8. Handle Exceptions Appropriately
- Document why systems aren't patched
- Implement compensating controls
- Risk acceptance for valid business reasons
- Regular review of exceptions

### 9. Communicate Effectively
- Notify stakeholders of maintenance windows
- Report patch compliance to management
- Escalate issues promptly
- Post-implementation reviews

### 10. Continuously Improve
- Learn from patch failures
- Measure and track metrics
- Refine processes based on experience
- Invest in automation to reduce manual effort

## Patching Different Asset Types

### Operating Systems
- Regular update cycles (Windows Patch Tuesday)
- May require reboots
- Critical for security baseline
- Use centralized management tools

### Applications
- Varied patching mechanisms (auto-update, manual, MSI)
- Test for business functionality impact
- May have dependencies on specific versions
- Consider [[Third-Party Dependency Scanning]] for application libraries

### Firmware and Embedded Devices
- Often overlooked but critical
- Network devices, printers, IoT devices
- May require manual process
- Risk of bricking devices if patch fails

### Containers and Cloud-Native
- Rebuild containers with updated base images
- Immutable infrastructure approach
- Automated CI/CD pipeline integration
- Ephemeral nature simplifies rollback

### Mobile Devices
- MDM (Mobile Device Management) solutions
- User-initiated updates (education required)
- BYOD challenges
- OS fragmentation (especially Android)

## Metrics and KPIs

### Compliance Metrics
- **Patch Compliance Rate**: Percentage of systems at current patch level
- **Time to Patch**: Days from patch release to deployment
- **SLA Compliance**: Meeting defined patching SLAs
- **Exception Rate**: Systems with approved patch exceptions

### Risk Metrics
- **Critical Vulnerabilities Unpatched**: Count of high-severity unpatched systems
- **Internet-Facing Unpatched Systems**: Exposed assets without patches
- **Mean Time to Patch (MTTP)**: Average time to deploy patches

### Operational Metrics
- **Patch Failure Rate**: Percentage of failed patch deployments
- **Rollback Rate**: Patches requiring rollback
- **Test Coverage**: Percentage of patches tested before deployment
- **Automation Rate**: Patches deployed via automation vs manual

## Compliance and Regulations

Many frameworks require timely patching:
- **PCI DSS**: Critical patches within one month
- **HIPAA**: Timely security updates
- **NIST CSF**: Vulnerability and patch management
- **CIS Controls**: Continuous vulnerability management
- **ISO 27001**: Patch management procedures
- **CMMC**: Defined patch management process

## Integration with Secure SDLC

Patch management connects to:
- **[[Vulnerability Management]]**: Patches remediate identified vulnerabilities
- **[[Change Management]]**: Patches deploy through change control
- **[[Security Monitoring]]**: Monitor for exploitation of unpatched systems
- **[[Third-Party Dependency Scanning]]**: Application-level patching
- **[[Penetration Testing]]**: Validates patch effectiveness

## Virtual Patching

When traditional patching isn't possible:
- Web Application Firewall (WAF) rules
- Intrusion Prevention System (IPS) signatures
- Network segmentation
- Access controls
- Application control
- Temporary workaround until real patch deployed

## References
1. [NIST SP 800-40: Guide to Enterprise Patch Management](https://csrc.nist.gov/publications/detail/sp/800-40/rev-4/final)
2. [CIS Control 7: Continuous Vulnerability Management](https://www.cisecurity.org/controls/)
3. [SANS Patch Management Guide](https://www.sans.org/white-papers/patch-management/)
4. [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide/)

#### Tags
#security #patch_management #vulnerability_management #change_management #operations #sdlc
