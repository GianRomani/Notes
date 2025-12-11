Created: 2025-12-04 15:45
#note

Security monitoring is the continuous process of collecting, analyzing, and responding to security-relevant events and data from IT infrastructure, applications, and networks. It's a critical component of the [[Secure SDLC]] operations phase, providing visibility into potential security incidents and enabling rapid response to threats.

## Overview

While preventive controls like [[Static Code Analysis]] and [[Penetration Testing]] aim to eliminate vulnerabilities before deployment, security monitoring operates on the principle that breaches are inevitable. It focuses on early detection, rapid response, and minimizing impact when security incidents occur. Effective monitoring provides the visibility needed to detect anomalies, investigate incidents, and understand attacker behavior.

## Core Components

### 1. Log Collection
Gathering security-relevant data from:
- Application logs (authentication, errors, transactions)
- System logs (OS events, service status)
- Network logs (firewall, proxy, DNS)
- Security device logs (IDS/IPS, WAF, antivirus)
- Cloud platform logs (AWS CloudTrail, Azure Activity Log)
- Database audit logs
- Authentication and identity management logs

### 2. Log Aggregation
Centralization of logs from distributed sources:
- Normalization of different log formats
- Time synchronization across sources
- Efficient storage and indexing
- Retention policies for compliance

### 3. Analysis and Correlation
Making sense of collected data:
- Real-time analysis for immediate threats
- Correlation across multiple log sources
- Baseline establishment for normal behavior
- Statistical and behavioral analysis
- Machine learning for anomaly detection

### 4. Alerting
Notification of security events:
- Real-time alerts for critical events
- Alert routing to appropriate teams
- Priority and severity classification
- Alert enrichment with context
- Deduplication to reduce noise

### 5. Response and Remediation
Acting on detected threats:
- Automated responses for known threats
- Incident investigation workflows
- Forensic data collection
- Remediation tracking
- Post-incident analysis

## What to Monitor

### Authentication and Access
- Failed login attempts
- Successful logins from unusual locations
- Privilege escalation
- Account creation and modification
- After-hours access to sensitive resources
- Dormant account activation
- Multiple concurrent sessions

### Application Behavior
- Error rate spikes
- Unusual API usage patterns
- Input validation failures
- Suspicious user agent strings
- Rate limit violations
- File upload/download anomalies
- Business logic abuse

### Network Activity
- Unusual outbound connections
- DNS queries to suspicious domains
- Port scanning activity
- Data exfiltration patterns
- DDoS indicators
- Protocol anomalies
- Geographic anomalies (connections from unexpected countries)

### System Events
- Configuration changes
- Service failures and restarts
- Resource exhaustion (CPU, memory, disk)
- Unauthorized software installation
- System file modifications
- Patch and update status

### Data Access
- Access to sensitive data
- Large data transfers
- Database query anomalies
- Unauthorized data export
- Data deletion events
- Schema modifications

### Security Control Events
- WAF blocks and alerts
- IDS/IPS signatures triggered
- Antivirus detections
- DLP policy violations
- Firewall rule hits

## Security Information and Event Management (SIEM)

SIEM platforms provide centralized security monitoring:

### Capabilities
- Log collection and aggregation
- Real-time correlation and analysis
- Incident detection and alerting
- Dashboards and visualization
- Compliance reporting
- Threat intelligence integration
- Case management for investigations

### Popular SIEM Solutions
- **Splunk**: Powerful search and analytics
- **Elastic (ELK) Stack**: Open-source, highly customizable
- **IBM QRadar**: Enterprise SIEM with threat intelligence
- **Microsoft Sentinel**: Cloud-native SIEM
- **ArcSight**: Traditional enterprise SIEM
- **Sumo Logic**: Cloud-based log management and SIEM
- **Datadog Security Monitoring**: Modern observability platform

## Detection Strategies

### Signature-Based Detection
- Known attack patterns and indicators
- Fast and low false-positive rate
- Requires updated signature databases
- Ineffective against novel attacks
- Examples: specific malware hashes, known malicious IPs

### Anomaly-Based Detection
- Establishes baseline of normal behavior
- Detects deviations from baseline
- Can identify zero-day attacks
- Higher false-positive rate
- Requires training period
- Examples: unusual network traffic volume, abnormal user behavior

### Behavioral Analysis
- User and Entity Behavior Analytics (UEBA)
- Machine learning models
- Identifies insider threats
- Detects compromised accounts
- Examples: user accessing unusual resources, abnormal working hours

### Threat Intelligence
- Integration with external threat feeds
- Known malicious IPs, domains, file hashes
- Indicators of Compromise (IoCs)
- Tactics, Techniques, and Procedures (TTPs)
- MITRE ATT&CK framework mapping

## Alert Fatigue and Management

### Challenges
- Volume of alerts overwhelms security teams
- High false-positive rates
- Alert desensitization
- Missed critical alerts in noise
- Analyst burnout

### Mitigation Strategies
- **Tune Detection Rules**: Adjust thresholds and rules to reduce false positives
- **Prioritization**: Risk-based prioritization of alerts
- **Contextualization**: Enrich alerts with additional context
- **Automation**: Automate response for low-risk, high-volume alerts
- **Tiering**: Multi-tier alert handling (automated → L1 → L2 → L3)
- **Metrics**: Track false positive rates and time to resolution

## Security Orchestration, Automation and Response (SOAR)

SOAR platforms automate security operations:

### Capabilities
- Playbook-driven automation
- Integration with security tools
- Case management
- Threat intelligence platform (TIP)
- Automated response actions
- Workflow orchestration

### Use Cases
- Automated phishing response
- Malware containment
- Vulnerability assessment triggering
- User account lockout
- Network segmentation enforcement
- Evidence collection

### Popular Platforms
- Palo Alto Cortex XSOAR
- Splunk SOAR (formerly Phantom)
- IBM Resilient
- Swimlane
- Tines

## Metrics and KPIs

### Detection Metrics
- Mean Time to Detect (MTTD)
- Alert volume and trends
- False positive rate
- Coverage (percentage of infrastructure monitored)
- Detection rule effectiveness

### Response Metrics
- Mean Time to Respond (MTTR)
- Mean Time to Contain (MTTC)
- Mean Time to Resolve
- Incident backlog
- Escalation rate

### Operational Metrics
- Log ingestion volume and velocity
- System availability and performance
- Storage utilization
- Analyst workload
- Alert closure rate

## Integration with Secure SDLC

Security monitoring connects to:
- **[[Threat Modeling]]**: Monitors for identified threat scenarios
- **[[Attack Surface Evaluation]]**: Prioritizes monitoring of exposed components
- **[[Penetration Testing]]**: Validates detection capabilities during testing
- **[[Vulnerability Management]]**: Monitors for exploitation attempts of known vulnerabilities
- **[[Change Management]]**: Monitors impact of changes on security posture

Monitoring feeds into:
- **Incident Response**: Triggers investigation and remediation
- **[[Vulnerability Management]]**: Identifies actively exploited vulnerabilities
- **[[Threat Modeling]]**: Updates threat models based on observed attacks
- **Security Requirements**: Informs future [[Software Security Requirements]]

## Cloud Security Monitoring

### Cloud-Specific Considerations
- Ephemeral resources (containers, serverless)
- Shared responsibility model
- API-driven infrastructure
- Multi-tenancy concerns
- Cloud-native logging services

### Cloud Monitoring Tools
- **AWS**: CloudWatch, CloudTrail, GuardDuty, Security Hub
- **Azure**: Monitor, Sentinel, Security Center, Defender
- **GCP**: Cloud Logging, Security Command Center
- **Multi-cloud**: Prisma Cloud, Lacework, Orca Security

## Compliance and Monitoring

Many regulations require security monitoring:
- **PCI DSS**: Log monitoring and file integrity monitoring
- **HIPAA**: Audit controls and logging
- **SOC 2**: Monitoring and incident response
- **GDPR**: Breach detection and notification
- **ISO 27001**: Security event management

## Best Practices

### 1. Define What to Monitor
- Align monitoring with [[Threat Modeling]] scenarios
- Prioritize based on [[Attack Surface Evaluation]]
- Monitor [[Third-Party Dependency Scanning|third-party components]]
- Include business logic abuse scenarios

### 2. Centralize Logging
- Single pane of glass for all security events
- Standardize log formats
- Ensure time synchronization
- Protect log integrity

### 3. Establish Baselines
- Understand normal behavior
- Document baseline metrics
- Regular baseline updates
- Account for business cycles

### 4. Automate Where Possible
- Automated log collection
- Automated initial triage
- Playbook-driven responses
- Reduce manual toil

### 5. Enrich with Context
- Asset information (criticality, owner)
- User context (role, department, typical behavior)
- Threat intelligence
- Vulnerability information from [[Vulnerability Management]]

### 6. Test Detection Rules
- Regular testing of detection capabilities
- Purple team exercises
- Simulate attacks from [[Penetration Testing]] findings
- Measure MTTD for various scenarios

### 7. Continuous Improvement
- Regular review of detection rules
- Tune based on false positives
- Incorporate new threat intelligence
- Learn from incidents (post-mortems)

## Challenges

- **Data Volume**: Overwhelming amount of log data
- **Tool Sprawl**: Multiple disconnected security tools
- **Skills Gap**: Shortage of skilled security analysts
- **False Positives**: Alert fatigue and desensitization
- **Cost**: Infrastructure and licensing costs for SIEM/SOAR
- **Retention**: Balancing storage costs with compliance requirements

## References
1. [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/publications/detail/sp/800-92/final)
2. [SANS Security Operations Center (SOC) Resources](https://www.sans.org/security-operations-center/)
3. [MITRE ATT&CK Framework](https://attack.mitre.org/)
4. [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

#### Tags
#security #monitoring #siem #soar #incident_response #detection #sdlc
