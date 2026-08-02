---
tags:
  - oscp
  - exam-rules
  - forbidden-tools
  - out-of-scope
created: 2026-07-31
---

# 🚫 Out-of-Scope Topics & Restricted Tools for the OSCP Exam

> **Key Rule:** The OSCP exam evaluates **manual penetration testing methodology**. Automated scanners, automated exploiters, and AI tools are strictly forbidden.

---

## 📚 1. Topics in PEN-200 Course BUT Out-of-Scope for the Exam

| Module # | Topic / Module Name | Why It Is Excluded from Exam |
| :--- | :--- | :--- |
| **Modules 25–26 & 29–31** | **AWS Cloud Infrastructure & Extra Mile Cloud Labs** | Exam targets internal network Active Directory and standalone Linux/Windows hosts—not AWS/Cloud environments. |
| **Module 11** | **Phishing Basics** | OSCP footholds are gained via network/web services. Social engineering and email phishing are out of scope. |
| **Module 12** | **Client-Side Attacks** | Requires user interaction (e.g. opening malicious Office docs). No simulated user clicks occur during the exam. |
| **Legacy BoF** | **Buffer Overflow (Stack-Based)** | **Officially removed from PEN-200 and exam**. Binary exploitation/BoF is no longer tested on OSCP. |

---

## ⛔ 2. Strictly Prohibited Tools & Scanners

> [!danger] Exam Policy Violation Warning
> Using any of the tools below on an exam machine can result in **0 points for the target or immediate exam failure**.

### ❌ Mass Vulnerability Scanners
- **Nessus** (Covered in PEN-200 Module 7, but **strictly banned** on exam)
- **OpenVAS** / **Greenbone**
- **NeXpose** / **InsightVM**
- **Qualys** / **SAINT**

### ❌ Automated Exploitation Tools
- **SQLmap** (All SQL injections **must be executed manually**)
- **SQLninja**
- **Metasploit Auto-Exploiters** (`db_autopwn`, `browser_autopwn`)
- **Core Impact** / **Canvas**

### ❌ Commercial Tool Versions
- **Burp Suite Professional** (*Only Burp Suite Community Edition is permitted*)
- **Metasploit Pro**
- **Cobalt Strike**

### ❌ AI Assistants & LLMs
- **ChatGPT**, **Claude**, **Gemini**, **Copilot**, **OffSec KAI**, **DeepSeek**, etc.
- *Strict Academic Integrity Policy:* Generative AI tools cannot be consulted during the 24-hr exam or reporting window.

---

## ⚠️ 3. Restricted Tool Usage Rules

### 🟡 Metasploit Framework (`msfconsole`)
- **Strict Limit:** You can use Metasploit on **ONLY ONE target machine** during the entire exam.
- Once you launch a Metasploit exploit module against a target, your single Metasploit "allowance" is consumed for the exam.
- **Best Practice:** Save Metasploit as a backup option and rely on manual scripts (`nc`, `curl`, custom Python exploits).

---

## ✅ 4. Fully Permitted Tools

- **Recon & Port Scanning:** `Nmap`, `Masscan`, `Nikto`, `Enum4linux`, `Gobuster`, `FFuF`, `Feroxbuster`
- **Web Proxies:** `Burp Suite Community Edition`, `ZAP (Zed Attack Proxy)`
- **Shells & Utilities:** `Netcat` (`nc`), `Socat`, `PowerShell`, `Bash`, `Python3`, `Curl`, `Wget`
- **Active Directory Tools:** `BloodHound` / `bloodhound.py`, `Impacket` tools (`GetNPUsers.py`, `secretsdump.py`, `psexec.py`), `Rubeus`, `evil-winrm`, `crackmapexec` / `netexec`
- **Privilege Escalation Audit Scripts:** `LinPEAS`, `WinPEAS`, `PowerUp.ps1`, `LES (Linux Exploit Suggester)`
