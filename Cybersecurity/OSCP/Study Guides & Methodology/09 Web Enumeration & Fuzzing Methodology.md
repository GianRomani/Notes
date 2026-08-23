---
tags:
  - oscp
  - web
  - methodology
  - fuzzing
  - gobuster
  - ffuf
  - exam-guide
created: 2026-08-21
status: active
---

# 🎯 Web Enumeration & Fuzzing Methodology — OSCP Exam Field Guide

> **Purpose:** An operational, battle-tested decision guide for web reconnaissance, directory/file fuzzing, and endpoint discovery. Designed to help you determine *what to run*, *why to run it*, *which wordlists/extensions to choose*, and *how to triage the results* quickly during the 24-hour OSCP exam.

---

## 🧭 1. The 4-Stage Web Enumeration Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: Target Fingerprinting & Port Scan Analysis                         │
│ ├─ Identify Open Ports: 80, 443, 8000, 8080, 8443, 8888, 9000, 5000, 3000   │
│ ├─ Identify Web Server & OS: Apache/Ubuntu, Nginx/Debian, Microsoft IIS     │
│ └─ Check Hostnames: SSL cert CN, DNS names -> Add to /etc/hosts             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: Low-Hanging Fruit & Passive Recon (First 2 Minutes)                │
│ ├─ robots.txt, sitemap.xml, security.txt                                    │
│ ├─ View Page Source (Ctrl+U): Comments, hidden inputs, disabled buttons     │
│ └─ Browser DevTools: Network XHR requests, Storage cookies, JS endpoints    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: Active Content Discovery & Fuzzing (Tiered Strategy)               │
│ ├─ Tier 1: Fast Surface Scan (common.txt -> 30 seconds)                    │
│ ├─ Tier 2: Deep Directory & File Scan (Medium list + Stack Extensions)      │
│ ├─ Tier 3: Subdirectory / VHost / Parameter Fuzzing                         │
│ └─ Error Handling: Calibrate for wildcards, custom 404s, SSL errors         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: Output Triage & Attack Vector Prioritization                       │
│ ├─ 200 OK: Inspect login forms, configs, backups (.bak, .old), file uploads │
│ ├─ 301/302 Redirect: Follow subdirectories, inspect redirect body & headers │
│ ├─ 401/403: Test header bypasses, basic auth, direct file access inside dir │
│ └─ 500 Error: Probe for SQLi, SSTI, command injection parameter flaws       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧠 2. The "Why & How" Decision Matrix (Self-Sufficiency Guide)

During the exam, do not guess commands randomly. Follow this decision matrix based on your recon findings:

### 2.1 How to Choose File Extensions (`-x` / `-e`)

| Detected Web Stack | Fingerprint Indicators | Mandatory Extensions to Fuzz | Why? |
| :--- | :--- | :--- | :--- |
| **PHP / Apache / Linux** | `Apache/2.4`, `PHPSESSID`, `X-Powered-By: PHP`, `.php` links | `.php, .html, .txt, .bak, .old, .zip, .save` | PHP executes server-side scripts; `.bak`/`.old` leak source code containing credentials. |
| **ASP.NET / IIS / Windows** | `Microsoft-IIS/10.0`, `ASP.NET_SessionId`, Windows OS | `.aspx, .asp, .ashx, .asmx, .txt, .bak, .config` | ASPX is default .NET; `web.config` leaks database connection strings and machine keys. |
| **Java / Tomcat / Spring** | `JSESSIONID`, Port `8080`, `/manager/html`, Spring banners | `.jsp, .war, .json, .txt, .bak` + directory paths | JSP web shells; check for `/actuator/env` and `/manager/html` administrative portals. |
| **Node.js / Express** | `connect.sid`, generic JSON errors, no file extensions in URL | Pure directory paths + `.json, .js, .txt, .bak` | Modern REST APIs rarely use file extensions; look for `/api/v1/`, `/admin`, `/login`. |
| **Python / Flask / Django** | `session` cookie (Base64+HMAC), `csrftoken`, Werkzeug | Pure directory paths + `.py, .txt, .bak, .json` | Flask/Django route by path; check for `/console` (Werkzeug PIN exploit) or `/admin`. |

---

### 2.2 How to Choose the Right Wordlist (Speed vs. Depth)

On Kali Linux, wordlists live in standardized directories. Use a **tiered strategy**:

```
[ Phase 1: Rapid Probe ] ──► [ Phase 2: Standard Deep Scan ] ──► [ Phase 3: Targeted Search ]
(common.txt | ~4.6k words)   (directory-list-2.3-med | ~220k)     (raft-medium-* or tech-specific)
```

| Fuzzing Goal | Recommended Wordlist Path on Kali Linux | Size / Speed |
| :--- | :--- | :--- |
| **Fast Initial Recon (First 30s)** | `/usr/share/wordlists/dirb/common.txt` | ~4,600 words (Fast) |
| **Standard OSCP Directory Scan** | `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` | ~220,000 words (Comprehensive) |
| **Dedicated File Fuzzing** | `/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt` | ~16,000 words (High-Yield Files) |
| **Dedicated Directory Fuzzing** | `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt` | ~30,000 words (Directories Only) |
| **Virtual Host / Subdomains** | `/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt` | ~5,000 words (Fast VHost) |
| **Hidden Parameter Discovery** | `/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt` | ~2,500 words (GET/POST params) |

> [!tip] Kali Wordlist Path Quick Reference
> If a SecLists path is not found, check both locations:
> - Pre-installed dirbuster: `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
> - Full SecLists package: `/usr/share/seclists/` or `/usr/share/wordlists/seclists/`

---

## 🛠️ 3. Troubleshooting & Error Handling Playbook

### 🔴 Error 1: Wildcard / Catch-All Redirection (Gobuster Abort)
- **The Error:**
  `the server returns a status code that matches the provided options for non existing urls. http://<IP>/<random-uuid> => 301 (redirect to http://<IP>/<random-uuid>/) (Length: 0).`
- **Root Cause:** The web server automatically issues a `301` redirect with body length `0` for any missing trailing slash.
- **The Solution:**
  - In **Gobuster**: Add `--exclude-length 0`
    ```bash
    gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt --exclude-length 0 -t 30
    ```
  - In **ffuf**: Add `-fs 0`
    ```bash
    ffuf -u http://<IP>/FUZZ -w /usr/share/wordlists/dirb/common.txt -fs 0 -c
    ```

---

### 🔴 Error 2: "Soft 404" Custom Error Pages (Everything returns HTTP 200)
- **Root Cause:** The application serves a custom "Page Not Found" HTML template that returns HTTP `200 OK` instead of `404 Not Found`.
- **The Solution:**
  1. Check the response size / word count of a non-existent page:
     ```bash
     curl -s -o /dev/null -w "%{size_download}\n" http://<IP>/thispageclearlydoesnotexist123
     # Example output: 3421 bytes
     ```
  2. Filter out that specific size in **ffuf** using `-fs`:
     ```bash
     ffuf -u http://<IP>/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -fs 3421 -c
     ```

---

### 🔴 Error 3: Self-Signed SSL / Certificate Errors (HTTPS)
- **The Error:** `tls: failed to verify certificate: x509: certificate signed by unknown authority`
- **The Solution:** Add `-k` (insecure mode) in Gobuster or ffuf:
  ```bash
  gobuster dir -u https://<IP>:8443 -k -w /usr/share/wordlists/dirb/common.txt --exclude-length 0
  ```

---

### 🔴 Error 4: Server Crashes / Connection Resets / Aggressive Rate Limits
- **Root Cause:** Fragile target VM service or embedded web server (e.g., Python `SimpleHTTPServer` / legacy PHP) crashing under high concurrency.
- **The Solution:**
  - Reduce threads: `-t 5` or `-t 10`
  - Add request delay: Gobuster `--delay 100ms` or ffuf `-p 0.1`

---

## 📊 4. Output Triage & Prioritization Matrix

When your scan produces output, triage findings by priority to avoid rabbit holes:

| Discovered Item | Status Code | Priority | Immediate Pentest Action |
| :--- | :--- | :--- | :--- |
| **`/admin`, `/portal`, `/login.php`, `/manager`** | `200` / `301` | 🔴 **CRITICAL** | Open in browser. Test default credentials (`admin:admin`, `admin:password`, `root:root`, `admin:admin123`), SQL injection auth bypass (`' OR 1=1--`), and password spraying. |
| **`/robots.txt`, `/sitemap.xml`** | `200` | 🔴 **CRITICAL** | Read immediately with `curl`. Discloses hidden developer directories and disallowed search engine paths. |
| **Backup files (`.bak`, `.old`, `.zip`, `.tar.gz`, `~`, `.swp`)** | `200` | 🔴 **CRITICAL** | Download immediately (`curl -O`). Extract and read source code, database passwords, API keys, and internal logic. |
| **`/upload`, `/uploads`, `/attachments`** | `200` / `301` / `403` | 🔴 **CRITICAL** | File upload attack vector. Check if unauthenticated uploads are allowed, or if uploaded files can be executed (`/uploads/shell.php`). |
| **`/.git/`, `/.svn/`** | `200` / `301` / `403` | 🔴 **CRITICAL** | Version control exposure. Dump full source history using `git-dumper http://<IP>/.git/ ./loot`. |
| **`/secret`, `/dev`, `/test`, `/staging`** | `200` / `301` / `403` | 🟡 **HIGH** | Run a dedicated recursive scan inside this subdirectory: `gobuster dir -u http://<IP>/dev/ -w ...` |
| **`/css`, `/js`, `/images`, `/fonts`** | `301` | 🟢 **LOW / NOISE** | Standard static assets. Ignore unless JavaScript files contain hardcoded API tokens or endpoints. |
| **`403 Forbidden` Endpoints** | `403` | 🟡 **MEDIUM** | Test bypass headers: `-H "X-Forwarded-For: 127.0.0.1"`, `-H "X-Custom-IP-Authorization: 127.0.0.1"`, or test direct subfiles (`/admin/index.php`). |

---

## ⚡ 5. Battle-Tested Command Cheatsheet (Copy-Paste Ready)

### 1. Phase 1: Rapid 30-Second Discovery
```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt --exclude-length 0 -t 30 -o gobuster_quick.txt
```

### 2. Phase 2: Full Deep Scan (Apache/PHP Environment)
```bash
gobuster dir \
  -u http://<TARGET_IP> \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -x php,html,txt,bak,old,zip \
  --exclude-length 0 \
  -t 40 \
  -o gobuster_deep.txt
```

### 3. Phase 2 Alternate: Full Deep Scan (Windows / IIS Environment)
```bash
gobuster dir \
  -u http://<TARGET_IP> \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -x aspx,asp,txt,bak,config,zip \
  --exclude-length 0 \
  -t 40 \
  -o gobuster_iis.txt
```

### 4. Phase 3: ffuf Fast Filtered Scan with Extensions
```bash
ffuf -u http://<TARGET_IP>/FUZZ \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -e .php,.html,.txt,.bak,.old \
  -fs 0 \
  -c \
  -o ffuf_results.json
```

### 5. Phase 4: Virtual Host Fuzzing (When Domain is Present)
```bash
# Add base domain to /etc/hosts first! (e.g. 10.11.1.X target.local)
ffuf -u http://target.local \
  -H "Host: FUZZ.target.local" \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -fs <default_page_size> \
  -c
```

### 6. Phase 5: Hidden GET Parameter Discovery
```bash
ffuf -u "http://<TARGET_IP>/view.php?FUZZ=test" \
  -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  -fs <default_page_size> \
  -c
```

---

## 🔗 Related Notes
- [[08 PEN-200 Module 8 - Intro to Web Applications]]
- [[Gobuster]]
- [[ffuf]]
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[00 OSCP Master Study Plan]]
