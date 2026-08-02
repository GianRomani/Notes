---
tags:
  - oscp
  - reporting
  - exam-guide
  - best-practices
created: 2026-08-02
status: active
---

# 📝 OSCP Exam Report Writing Guide: Best Practices, Templates & Pitfalls

> **The Golden Rule of the OSCP Report:** An OffSec grader must be able to read your report and reproduce your exact compromise path step-by-step from a fresh machine state without guessing any parameters.

---

## 🚨 1. Official OffSec Submission Rules & Deadlines

> [!danger] Mandatory Submission Requirements
> Failure to follow these rules will result in an automatic exam failure regardless of points earned.

- **Submission Window:** Exactly **24 hours** from the moment your 23h45m practical exam ends.
- **File Format:** PDF document archive.
- **Naming Convention:** `OSCP-OS-XXXXX-Exam-Report.pdf` (Replace `OS-XXXXX` with your exact OffSec OS ID number).
- **Archive Requirement:** Submit the PDF compressed inside a `.7z` or `.zip` archive named `OSCP-OS-XXXXX-Exam-Report.7z`.
- **Template Source:** Download the official OffSec Microsoft Word / OpenOffice template from your portal, or use community Markdown tools like [noraj/OSCP-Exam-Report-Template](https://github.com/noraj/OSCP-Exam-Report-Template) to compile via `pandoc`.

---

## 📸 2. Mandatory Screenshot Requirements (Proof Flags)

Every compromised target (`local.txt`/`user.txt` and `proof.txt`/`secret.txt`) requires a screenshot that satisfies **all three** of the following requirements in a single terminal view:

```text
+-------------------------------------------------------------------------+
| Terminal Window                                                         |
|                                                                         |
|  $ whoami                                                               |
|  root                                                                   |
|                                                                         |
|  $ ip a  (or ipconfig / ifconfig)                                       |
|  eth0: 192.168.200.X / tun0: 10.10.X.X                                 |
|                                                                         |
|  $ cat /root/proof.txt                                                  |
|  7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c                                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

### ✅ Proof Screenshot Checklist:
1. **Command 1:** `whoami` (showing current user identity).
2. **Command 2:** `ip a` / `ifconfig` / `ipconfig` (showing target IP address).
3. **Command 3:** `cat proof.txt` / `type proof.txt` (showing the raw 32-character flag).
4. **Visibility:** The entire terminal output must be fully un-truncated and legible.

---

## 🏛️ 3. Standard OSCP Report Structure

A professional, high-scoring OSCP report contains 5 core sections:

```
1. Executive Summary & Compromise Matrix
2. High-Level Technical Summary
3. Active Directory Domain Compromise Walkthrough
4. Standalone Machine Compromise Walkthroughs
5. Remediation & Hardening Recommendations
```

### Section 1: Executive Summary
- Brief statement of the assessment scope and overall exam result.
- Summary table listing target hosts, IP addresses, points allocated, and compromise status.

| Hostname | IP Address | Points Value | Initial Access Status | Privilege Escalation Status | Total Points |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AD DC (DC01)** | `192.168.X.10` | 40 (Set) | ✅ Domain User | ✅ Domain Admin (`secret.txt`) | 40 |
| **Target-01** | `192.168.X.20` | 20 | ✅ `local.txt` | ✅ `proof.txt` | 20 |
| **Target-02** | `192.168.X.30` | 20 | ✅ `local.txt` | ✅ `proof.txt` | 20 |
| **Target-03** | `192.168.X.40` | 10 | ✅ `local.txt` | ❌ Failed | 10 |

### Section 2: Machine Walkthrough Template
For **every single host**, include:

1. **Host Information Card:**
   - Hostname, IP Address, OS, Points Value.
2. **Phase 1 — Service Enumeration:**
   - Exact Nmap command used.
   - Code block with relevant open ports & discovered service versions.
3. **Phase 2 — Initial Exploitation (`local.txt` / `user.txt`):**
   - Explanation of the vulnerability (e.g., Unauthenticated RCE in Web App).
   - Exact command string or modified exploit script used.
   - Code block / screenshot showing shell access.
   - **Mandatory Flag Proof Screenshot** (`whoami` + `ip a` + `cat local.txt`).
4. **Phase 3 — Privilege Escalation (`proof.txt` / `secret.txt`):**
   - Internal enumeration findings (e.g., SUID binary, vulnerable service, privilege token).
   - Commands executed to elevate privileges to `root` or `SYSTEM`.
   - **Mandatory Flag Proof Screenshot** (`whoami` + `ip a` + `cat proof.txt`).
5. **Phase 4 — Remediation Recommendations:**
   - 2–3 brief bullets explaining how to fix the specific vulnerabilities exploited on this host.

---

## 💡 4. Top Practices & Efficiency Tips

### During the Exam (Real-Time Practices):
* **Take Screenshots AS YOU GO:** Do NOT wait until your exam timer ends to take flag screenshots. Take a screenshot immediately upon obtaining every flag.
* **Save Clean Screenshot Files:** Save images into a local directory with descriptive names:
  `~/oscp/exam/screenshots/192.168.X.10_root_proof.png`
* **Log All Commands (`script` or Terminal Logging):** Run `script -a exam_terminal.log` in your Kali terminal so you have a complete history of every command executed.
* **Keep Code Blocks Clean:** Include code blocks with syntax highlighting (`bash`, `powershell`, `python`).

### Writing the Report (Post-Exam Window):
* **Use Pandoc / Markdown (Recommended for Speed):** Writing your report in Markdown and converting via `pandoc` produces beautiful PDFs in minutes.
* **Highlight Custom Modifications:** If you modified a public exploit script (e.g., changing shellcode or offsets), include a clean diff block showing your edits:
  ```diff
  - LHOST = "127.0.0.1"
  + LHOST = "10.10.X.X" # Modified Kali VPN IP
  ```

---

## ⚠️ 5. Critical Pitfalls to Avoid ("Things to Avoid")

> [!caution] Avoid These Common Exam Failure Causes

1. ❌ **Missing `ip a` / `ipconfig` or `whoami` in Flag Screenshots:**
   - *Fix:* Always run `whoami`, `ip a`, and `cat proof.txt` together before taking the screenshot.
2. ❌ **Vague Steps or Missing Commands:**
   - *Fix:* Never write "I executed an exploit script and got root." Write out the full command: `python3 CVE-2021-4034.py`.
3. ❌ **Unreadable or Truncated Screenshots:**
   - *Fix:* Ensure text is large and clear. Do not resize images so small that text becomes unreadable.
4. ❌ **Forgetting Custom Exploit Modifications:**
   - *Fix:* Paste the exact modified code snippet into the report.
5. ❌ **Submitting Past the 24-Hour Reporting Window:**
   - *Fix:* Finish writing your draft within 12 hours post-exam, compile to PDF early, and verify the file before submitting.
6. ❌ **Using Prohibited Tools or Restricted AI:**
   - *Fix:* Do NOT use SQLmap, Nessus, commercial tools, or Generative AI tools (ChatGPT, Gemini, Claude) during report writing. Doing so violates OffSec academic policy.

---

## 🔗 Related Notes
- [[00 OSCP Master Study Plan]]
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[08 Out of Scope Topics & Restricted Tools]]
- [[Template - Standalone Machine Target Note]]
