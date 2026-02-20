---
name: oscp-scenarios
description: |
  **OSCP Scenario Generator**: Create realistic practice penetration testing scenarios based on vault security notes.
  - MANDATORY TRIGGERS: scenario, practice scenario, oscp scenario, lab, simulation, htb scenario, prove grounds, exam scenario, practice pentest
---

## Purpose

The OSCP scenario generator transforms security concepts from the vault (privilege escalation, exploitation techniques, post-exploitation, enumeration methods) into executable practice scenarios. Each scenario is a mini-lab that mimics real OSCP exam conditions: target environment, initial access state, constraints, and success criteria.

## Input

Accepts:
- A security/exploitation concept from the vault (e.g., "privilege escalation via SUID binaries", "SQL injection to RCE", "buffer overflow exploitation")
- Optional difficulty level (easy, medium, hard)
- Optional constraints (e.g., "network filtering enabled", "WAF active", "assume limited system info")
- Optional hints preference (with or without hints)

## Output Format

Scenarios are saved to `Study/OSCP/` as a single markdown file with format:

```markdown
YYYY-MM-20 HH:MM
#quicknote

## Scenario: [Descriptive Title]

**Based on**: [[vault-concept-note]]

### Scenario Details

**Difficulty**: Medium | **Estimated Time**: 45 minutes | **Technique**: SQL Injection

**Target Machine**: Windows Server 2019, IIS 10, custom web app
**Initial Access**: Low-privilege shell (www-data user)
**Constraints**: No Internet access, only tools in `/opt/tools/`, WAF blocks common payloads
**Success Criteria**: Gain SYSTEM-level access, extract database credentials, dump NTDS.dit

### Reconnaissance & Enumeration

Begin by enumerating the target:

- Use `whoami /all` to check current privileges and group memberships
- Run `systeminfo` to identify OS version, patches, and installed software
- Execute `tasklist /v` to find running services and their associated users
- Check for scheduled tasks with `schtasks /query /fo LIST /v`
- Examine `C:\Program Files\` and `C:\Program Files (x86)\` for custom applications
- Look for unquoted service paths with `wmic service list brief`

**Enumeration Goal**: Identify a potential privilege escalation vector (SUID binary, unquoted path, weak service permissions, or kernel vulnerability).

### Exploitation Approach

**Hypothesis**: The custom web application likely has a SQL injection vulnerability in the login form.

**Exploitation Steps**:

1. Capture HTTP traffic using Burp Suite; test the login parameter for SQL injection
2. Construct a time-based blind SQL injection payload (if error-based fails)
3. Enumerate the database: database user, table names, column contents
4. Check for command execution: attempt `xp_cmdshell` or `sp_OACreate` if SQL Server
5. Gain a reverse shell or upload a web shell for easier access
6. Establish persistence before lateral movement

**Tools**: Burp Suite Community, SQLmap, msfvenom, Netcat

### Post-Exploitation & Escalation

Once inside the web application context:

- Examine configuration files: `web.config`, `appsettings.json`, database connection strings
- Check file permissions on sensitive directories
- Hunt for plaintext credentials in logs, temp files, or registry
- Identify a privilege escalation vector discovered during enumeration
- Execute privilege escalation exploit (e.g., compile and run C# exploit if kernel vuln, or exploit weak service permissions)
- Verify SYSTEM access with `whoami /all` and `hostname`

**Success Indicators**: You can read `C:\Windows\System32\config\SAM` and extract credential hashes, or execute arbitrary commands as SYSTEM.

### Hints (Optional)

- The custom web app is NOT secure; simple SQL injection payloads may not work due to WAF — try encoding or alternative syntax
- The SUID binary is in `/opt/services/` and may accept user input; fuzz it or analyze with `file` and `strings`
- Post-exploitation: check `/root/.ssh/authorized_keys` for additional persistence vectors

### References

- [[SQL Injection]] — Detection and exploitation methods
- [[Privilege Escalation]] — Windows and Linux vectors
- [[Post-Exploitation]] — Persistence, lateral movement, data exfiltration
- [[OWASP Top 10 for LLMs]] — Web application vulnerabilities context

---

**Scenario Created**: 2026-02-20 | **Difficulty**: Medium | **Time**: 45 min | **Status**: Ready for practice

#### Tags
oscp, scenario, sql_injection, privilege_escalation, lab, practice, windows
```

## Scenario Structure Components

### 1. Scenario Details (Required)
- **Difficulty**: Easy, Medium, or Hard
- **Estimated Time**: 30–120 minutes
- **Technique**: Primary exploitation technique
- **Target Machine**: OS, services, application stack
- **Initial Access**: Starting point (unauthenticated, low-priv shell, credentials)
- **Constraints**: Network restrictions, WAF, intrusion detection, limited tools
- **Success Criteria**: What constitutes completion (flag, RCE, creds, persistence)

### 2. Reconnaissance & Enumeration (Required)
Lists actionable enumeration commands specific to the target OS and services. This section mirrors real OSCP exam approach: gather information systematically before attempting exploitation.

**Quality standard**: Commands should be:
- Executable with standard tools
- OS-specific and realistic
- Ordered logically (passive → active)
- Include expected output hints

### 3. Exploitation Approach (Required)
Explains the attack chain without giving away exact payloads:
- Vulnerability hypothesis
- Step-by-step exploitation logic
- Tools needed
- Fallback methods if primary approach fails

**Quality standard**: Learner should understand *why* each step happens, not just *how* to copy-paste commands.

### 4. Post-Exploitation & Escalation
Objectives after initial access:
- Persistence establishment
- Privilege escalation path
- Lateral movement prep
- Data exfiltration targets
- Success verification

### 5. Hints (Optional)
Non-spoiler hints if learner is stuck:
- "The service is vulnerable to X"
- "Check for Y file type in Z directory"
- "The encoding/obfuscation technique is Z"

## Difficulty Guidance

**Easy (30-40 min)**
- One clear vulnerability path
- Exploit available in Metasploit or public PoC
- Minimal enumeration steps
- No privilege escalation needed

**Medium (45-90 min)**
- Two vulnerability chains (initial access + privilege escalation)
- Requires custom payload development or exploitation
- Moderate enumeration
- Post-exploitation complexity

**Hard (90-120 min)**
- Multiple exploitation paths, requires choosing optimal one
- Kernel vulnerability or complex logic bug
- Extensive enumeration and pattern recognition
- Chained post-exploitation (persistence + pivot + exfiltration)

## Integration Rules

1. **Always reference vault notes** via `[[wikilinks]]` to related concepts
2. **Include tools that exist in standard OSCP toolkits** (Nmap, Metasploit, Burp, impacket, etc.)
3. **Use realistic constraints** (WAF, AV, limited shell, network filtering) that mirror exam conditions
4. **Group scenarios by technique** — if creating multiple, organize by: privilege escalation, exploitation, post-exploitation, lateral movement
5. **Suggest prerequisite vault reading** — at the end, suggest which notes to study before attempting the scenario

## Example Scenario Titles

- "Unauthenticated SQLi → RCE on IIS 10 with Custom Webapp"
- "Kernel Vulnerability (CVE-XXXX) Privilege Escalation on Ubuntu 18.04"
- "SUID Buffer Overflow with ASLR Bypass using Return-Oriented Programming"
- "Active Directory Lateral Movement via Kerberoasting and Pass-the-Ticket"

## Post-Generation

After creating a scenario, the agent should recommend:
- Which vault notes to review for theory
- Whether to attempt easy/medium/hard version first
- Related scenarios that build on the same techniques
