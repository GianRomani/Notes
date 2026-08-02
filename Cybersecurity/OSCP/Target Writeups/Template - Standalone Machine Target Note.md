---
tags:
  - oscp
  - machine
  - writeup
  - template
created: {{date}}
target_name: ""
target_ip: ""
os: Linux / Windows
difficulty: Easy / Medium
user_flag: ""
root_flag: ""
status: todo
---

# 🖥️ Machine Target: {{target_name}} (`{{target_ip}}`)

> **OS:** `{{os}}` | **Difficulty:** `{{difficulty}}` | **Status:** `In Progress / Completed`

---

## 1. Executive Summary & Compromise Path
- **Initial Access:** Briefly describe how initial access was gained (e.g., vulnerable web endpoint, weak credentials).
- **Privilege Escalation:** Describe privilege escalation vector (e.g., SUID binary, sudo privilege, unquoted service path).
- **Key Takeaways / Vulnerabilities:**
  1. Vulnerability 1
  2. Vulnerability 2

---

## 2. Information Gathering & Port Scanning

### Nmap Scan Results
```text
# Insert Nmap output here
```

### Discovered Services & Attack Surface
- **Port 80 (HTTP):** Web application notes, technology stack, directory enumeration.
- **Port 22 (SSH):** Banner version, user logins tested.

---

## 3. Vulnerability Assessment & Exploitation

### Web Enumeration / Service Exploitation
- Endpoint tested:
- Payload used:
- Shell returned:

```bash
# Insert exploit command or web request payload here
```

---

## 4. Initial Access (`user.txt`)

- **User Flag:** `{{user_flag}}`
- **Compromised Account:** `username`
- **Shell Type:** Web shell / Reverse Bash Shell / Meterpreter

---

## 5. Privilege Escalation (`root.txt` / `system.txt`)

### Internal Enumeration
- **Enumeration tool used:** `linpeas.sh` / `winPEAS.exe` / `sudo -l`
- **Findings:**

```bash
# Privilege Escalation Command
```

- **Root / System Flag:** `{{root_flag}}`

---

## 6. Artifacts & Command Log
```bash
# History of key operational commands run on target
```
