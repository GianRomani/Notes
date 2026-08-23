---
tags:
  - oscp
  - pen200
  - web
  - module8
  - enumeration
  - burpsuite
  - ffuf
  - gobuster
created: 2026-08-21
status: active
linear_task: GIA-94
---

# 🌐 PEN-200 Module 8: Introduction to Web Applications & Web Attack Fundamentals

> **Target Goal:** Master web application architecture, HTTP protocol mechanics, proxy interception with Burp Suite, comprehensive web fingerprinting, directory/vhost fuzzing, parameter discovery, and source code reconnaissance for initial foothold access.

---

## 🧭 Web Application Assessment Methodology (OSCP Workflow)

```
                       [ 1. Web Recon & Fingerprinting ]
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           ▼                         ▼                         ▼
  [ Tech Stack & CMS ]      [ robots.txt / Leaks ]     [ DevTools & Source ]
  (whatweb, Wappalyzer)      (.git, .env, backups)    (JS files, hidden fields)
           │                         │                         │
           └─────────────────────────┼─────────────────────────┘
                                     │
                     [ 2. Content & Routing Discovery ]
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
  [ Directory & File Fuzzing ]                     [ VHost / Subdomain Enum ]
  (ffuf, gobuster, feroxbuster)                     (ffuf Host header fuzzing)
           │                                                   │
           └─────────────────────────┬─────────────────────────┘
                                     │
                      [ 3. Parameter & Input Fuzzing ]
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
  [ GET / POST Parameter Fuzzing ]                  [ Burp Suite Tampering ]
  (ffuf, arjun, param-miner)                        (Repeater, Decoder, Proxies)
                                     │
                                     ▼
                [ 4. Vulnerability Identification & Exploitation ]
               (LFI/RFI, File Upload, SQLi, RCE -> Modules 9 & 10)
```

---

## 📌 1. HTTP/HTTPS Protocol & Web Mechanics Deep-Dive

> [!info] 💡 Core Protocol Concepts
> Web applications communicate using stateless HTTP/HTTPS requests and responses over TCP (typically ports `80`, `443`, `8080`, `8443`, `8000`, `5000`).

### 1.1 HTTP Request Methods & When to Test Them
| Method | Purpose | Security & Pentest Significance |
| :--- | :--- | :--- |
| `GET` | Retrieve resource | Parameters exposed in URL & access logs; often vulnerable to Reflected XSS, SQLi, LFI. |
| `POST` | Submit data / body | Transmits form payloads, JSON/XML bodies, credentials, and file uploads. |
| `PUT` | Upload / overwrite resource | If misconfigured, allows arbitrary file upload (e.g. uploading a PHP web shell directly). |
| `DELETE` | Remove resource | Can delete application files or user records if authorization is missing. |
| `OPTIONS` | Query allowed methods | Identifies supported methods via `Allow:` header (e.g., `Allow: GET, POST, PUT, OPTIONS`). |
| `HEAD` | Like `GET` but response headers only | Fast testing for resource existence without downloading large response bodies. |
| `PATCH` | Partial resource update | Used heavily in REST APIs; check for parameter pollution or mass assignment. |

### 1.2 HTTP Response Status Codes
- **`200 OK`**: Request succeeded.
- **`201 Created`**: Resource created (often seen in file upload / API creation).
- **`301 Moved Permanently` / `302 Found`**: Redirection. *Tip: Always check response body of 302 redirects in Burp—sometimes the sensitive data is rendered before redirection!*
- **`400 Bad Request`**: Malformed syntax or invalid parameters.
- **`401 Unauthorized`**: Authentication required (e.g., HTTP Basic/Digest Auth).
- **`403 Forbidden`**: Server understands request but refuses access. *Tip: Test bypasses with headers like `X-Forwarded-For: 127.0.0.1`, `X-Custom-IP-Authorization: 127.0.0.1`, or path normalizations like `//admin`, `/admin/.`.*
- **`404 Not Found`**: Resource does not exist.
- **`405 Method Not Allowed`**: Target method not supported on this endpoint.
- **`500 Internal Server Error`**: Server-side exception. *Tip: Great indicator of SQL injection, template injection, or unhandled exceptions leaking stack traces.*

### 1.3 Key Request & Response Headers
- **`Host`**: Identifies domain/vhost being requested (critical for virtual host routing).
- **`User-Agent`**: Client browser identity (some sites render different versions or log User-Agent, leading to User-Agent SQLi/Command Injection/Log4j).
- **`Content-Type`**: `application/x-www-form-urlencoded`, `multipart/form-data`, `application/json`, `application/xml`.
- **`Cookie` & `Set-Cookie`**: Session tokens (`PHPSESSID`, `JSESSIONID`, `ASP.NET_SessionId`, `connect.sid`). Look for flags: `HttpOnly` (blocks JS access), `Secure` (HTTPS only), `SameSite`.
- **`Server` & `X-Powered-By`**: Fingerprints underlying backend (e.g., `Server: Apache/2.4.41 (Ubuntu)`, `X-Powered-By: PHP/7.4.3`).

### 1.4 Encodings in Web Applications
- **URL Encoding (Percent Encoding)**: Spaces become `%20` or `+`, quotes become `%22`, `#` becomes `%23`, `&` becomes `%26`.
- **HTML Entity Encoding**: `<` becomes `&lt;`, `>` becomes `&gt;`, `"` becomes `&quot;`.
- **Base64**: Alphanumeric + `+`, `/`, `=` padding. Heavily used in authorization headers (`Basic dXNlcjpwYXNz`), session tokens, cookies, and serialised data.

---

## 📌 2. Intercepting Proxies: Burp Suite Mastery

> [!info] 💡 Tool Context: **Burp Suite**
> - **What it is:** The premier web application security testing platform acting as a Man-in-the-Middle (MitM) HTTP/S proxy.
> - **When to use:** Every time you touch a web application in PEN-200 labs or the OSCP exam.
> - **Why it's helpful:** Full visibility into raw HTTP streams, granular request tampering, decoding, and custom replay.

### 2.1 Core Burp Suite Modules
```
┌─────────────────────────────────────────────────────────────┐
│                       BURP SUITE CORE                       │
├───────────────┬───────────────┬──────────────┬──────────────┤
│  Proxy / HTTP │   Repeater    │   Intruder   │   Decoder    │
│  History      │ (Manual edit  │ (Automated   │ (URL, B64,   │
│ (Inspect/Drop/│  & instant    │  fuzzing &   │  Hex, Hash,  │
│  Forward)     │  re-test)     │  brute force)│  Smart Parse)│
└───────────────┴───────────────┴──────────────┴──────────────┘
```

#### 1. Proxy & Target Scope
- **Proxy Listener:** Default `127.0.0.1:8080`. Configure browser (via FoxyProxy extension) to forward traffic here.
- **Target Scope:** Right-click target in *Target -> Site Map -> Add to Scope*. In *Proxy -> HTTP History*, toggle **"Show only in-scope items"** to prevent noise from background OS/browser traffic.
- **Match and Replace Rules:** In *Proxy Settings -> Match and Replace*, auto-inject headers like `X-Forwarded-For: 127.0.0.1` or rewrite User-Agents.

#### 2. Repeater (Your Primary Tool)
- Press `Ctrl + R` (`Cmd + R` on macOS) on any captured request to send to Repeater.
- Change HTTP methods, inject payloads into query strings or body, strip headers, inspect raw responses.
- Useful Shortcuts:
  - `Ctrl + Space`: Issue request.
  - `Ctrl + U`: URL-encode or URL-decode selected text in-place.
  - `Ctrl + Shift + U`: Full URL-encode.

#### 3. Intruder Attack Types
> [!warning] Burp Community Edition Throttling
> Burp Suite Community intentionally throttles Intruder requests. For high-speed wordlist fuzzing (directories, parameters, passwords), **always use `ffuf` or `wfuzz` instead**!

- **Sniper (Single payload set):** Replaces one position `§payload§` at a time.
- **Battering Ram (Single payload set):** Puts the exact same payload into multiple positions simultaneously.
- **Pitchfork (Multiple payload sets):** Iterates through 2+ wordlists in parallel line-by-line (e.g. user1:pass1, user2:pass2).
- **Cluster Bomb (Multiple payload sets):** Tests all permutations/cartesian combinations (e.g. all passwords against user1, then user2).

#### 4. Decoder
- Rapid transformations: `URL`, `HTML`, `Base64`, `ASCII Hex`, `Hex`, `Octal`, `Binary`, `Gzip`.
- Multi-step decoding (e.g. Base64 decode -> URL decode -> Hex inspection).

---

## 📌 3. Web Reconnaissance & Tech Stack Fingerprinting

### 3.1 Passive & Active Fingerprinting Commands
```bash
# 1. Quick banner & header grab with curl
curl -I http://10.11.1.X/
curl -I -k https://10.11.1.X/

# 2. Detailed tech stack identification with whatweb
whatweb http://10.11.1.X
whatweb -a 3 http://10.11.1.X # Aggressive probing

# 3. Nmap HTTP enumeration scripts
nmap -p 80,443,8080,8443 --script http-enum,http-headers,http-methods,http-title 10.11.1.X
```

### 3.2 Common Web Stacks & What to Look For
| Stack / Technology | Typical Artifacts & Clues | Common OSCP Vectors |
| :--- | :--- | :--- |
| **PHP / Apache** | `.php` extensions, `PHPSESSID`, `X-Powered-By: PHP`, `.htaccess` | LFI/RFI wrappers, File Upload bypasses, PHP type juggling, Command Injection. |
| **ASP.NET / IIS** | `.aspx`, `.ashx`, `.asmx`, `ASP.NET_SessionId`, `web.config` | Deserialization (`ysoserial.net`), SQL Injection (MSSQL `xp_cmdshell`), Web.config leaks. |
| **Java / Tomcat / Spring** | `JSESSIONID`, port `8080`, `/manager/html`, `/host-manager` | Default Tomcat credentials (`tomcat:s3cret`, `admin:admin`), WAR webshell deployment, Spring Boot Actuators (`/actuator/env`, `/actuator/heapdump`). |
| **Node.js / Express** | `connect.sid`, generic JSON errors, no file extensions | Node eval injection, Prototype Pollution, SSRF, Command injection via child_process. |
| **Python / Flask / Django** | `session` cookie (often Base64 + HMAC), `csrftoken`, Werkzeug debug console | Server-Side Template Injection (SSTI: Jinja2 `{{ config.items() }}`), Werkzeug PIN exploit, Pickle deserialization. |
| **WordPress CMS** | `/wp-admin/`, `/wp-content/`, `/wp-includes/`, `/xmlrpc.php` | Vulnerable plugins, user enumeration (`/wp-json/wp/v2/users`), `wpscan`, XML-RPC brute force. |

---

## 📌 4. Directory & File Discovery (Fuzzing Mastery)

> [!info] 💡 Tool Context: **`ffuf` vs `gobuster` vs `feroxbuster`**
> - **`ffuf` (Fuzz Faster U Fool):** Fastest, most versatile web fuzzer. Supports directory fuzzing, VHost fuzzing, parameter fuzzing, and advanced filtering. **(Recommended primary tool for OSCP)**.
> - **`gobuster`:** Simple, clean, standard directory and DNS/vhost brute-forcer.
> - **`feroxbuster`:** Fast, recursive by default, auto-tunes threads.

### 4.1 Essential SecLists Wordlists
```bash
# Top general directory lists
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/big.txt

# Technology specific
/usr/share/seclists/Discovery/Web-Content/Apache.fuzz.txt
/usr/share/seclists/Discovery/Web-Content/IIS.fuzz.txt
/usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt
```

### 4.2 Practical `ffuf` Directory & File Fuzzing Recipes
```bash
# 1. Standard directory discovery
ffuf -u http://10.11.1.X/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -c -v

# 2. File discovery with extensions
ffuf -u http://10.11.1.X/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt -e .php,.html,.txt,.bak,.old,.zip,.json -c

# 3. Recursive directory fuzzing (depth 2)
ffuf -u http://10.11.1.X/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -recursion -recursion-depth 2 -c

# 4. Filtering responses (Essential for wildcard / false-positive suppression)
# Filter by HTTP status code (-fc), size (-fs), word count (-fw), line count (-fl)
ffuf -u http://10.11.1.X/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -fc 404,403
ffuf -u http://10.11.1.X/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -fs 1542 # Filter specific response size
```

### 4.3 `gobuster` Quick Recipes
```bash
# Standard directory scan
gobuster dir -u http://10.11.1.X -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 30 -o gobuster_root.txt

# Directory scan with extensions and status code exclusion
gobuster dir -u http://10.11.1.X -w /usr/share/seclists/Discovery/Web-Content/common.txt -x php,txt,html,bak,old,zip -b 404,403 -t 30
```

---

## 📌 5. Virtual Host (VHost) & Subdomain Enumeration

> [!important] VHost Routing in OSCP Labs
> Many machines host multiple websites on the same IP (e.g. `domain.com`, `admin.domain.com`, `dev.domain.com`). If you only browse by IP, the web server serves the default catch-all page. **Always check for VHosts if a domain name is revealed in certificates, footer text, or DNS!**

### 5.1 Host Header Fuzzing with `ffuf`
```bash
# First, add base domain to /etc/hosts:
# 10.11.1.X  target.thm  target.local

# Fuzz for virtual hosts (always filter default response size -fs!)
ffuf -u http://target.local -H "Host: FUZZ.target.local" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fs <default_page_size>

# Example finding: 'dev' returns size 2341 while default is 1024 -> Add dev.target.local to /etc/hosts!
```

### 5.2 `gobuster vhost` Command
```bash
gobuster vhost -u http://target.local -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain
```

---

## 📌 6. Hidden Parameter Discovery & Fuzzing

> [!info] 💡 Why Parameter Fuzzing Matters
> Web endpoints like `index.php` or `view.php` often contain undocumented parameters that trigger file inclusion, debugging modes, or command execution (e.g. `view.php?page=...`, `index.php?debug=1`, `account.php?id=...`).

### 6.1 GET Parameter Fuzzing with `ffuf`
```bash
# Fuzz GET parameters
ffuf -u "http://10.11.1.X/index.php?FUZZ=test" -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs <default_size> -c

# Fuzz parameter value once parameter name is known
ffuf -u "http://10.11.1.X/index.php?view=FUZZ" -w /usr/share/seclists/Fuzzing/LFI/LFI-graceful-security-linux.txt -c
```

### 6.2 POST Parameter Fuzzing with `ffuf`
```bash
# Fuzz POST parameters (form-data / x-www-form-urlencoded)
ffuf -u "http://10.11.1.X/login.php" -X POST -d "FUZZ=admin" -H "Content-Type: application/x-www-form-urlencoded" -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs <default_size>
```

### 6.3 Dedicated Parameter Discovery Tools
```bash
# Arjun (Fast HTTP parameter discovery tool)
arjun -u http://10.11.1.X/page.php -m GET
arjun -u http://10.11.1.X/page.php -m POST
```

---

## 📌 7. Information Leakage, Source Inspection & Sensitive Files

### 7.1 Manual Code & Browser DevTools Reconnaissance
1. **View Page Source (`Ctrl + U`):**
   - Developer comments (`<!-- TODO: Remove default admin credentials admin/admin123 -->`).
   - Commented-out HTML links or hidden endpoints (e.g. `<!-- <a href="/admin_test.php">Admin</a> -->`).
   - Hidden form fields: `<input type="hidden" name="role" value="user">` -> Tamper in Burp to `value="admin"`.
   - Disabled submit buttons: `<button disabled>Submit</button>` -> Remove `disabled` in Elements tab.
2. **Sources / Debugger Tab:**
   - Client-side JavaScript logic: Look for hardcoded API keys, JWT tokens, AWS/S3 bucket URLs, password validation routines, API route declarations (`/api/v1/users`).
3. **Network Tab:**
   - Observe background XHR / AJAX / Fetch API requests.
   - Inspect JSON responses containing verbose error messages or additional unrendered data fields.
4. **Storage Tab:**
   - Inspect Cookies, LocalStorage, and SessionStorage for session IDs, tokens, or role flags.

### 7.2 Standard Sensitive Paths Checklist
```bash
# Check standard compliance & crawler files
curl -s http://10.11.1.X/robots.txt
curl -s http://10.11.1.X/sitemap.xml
curl -s http://10.11.1.X/.well-known/security.txt

# Check Version Control leaks
curl -s -I http://10.11.1.X/.git/
curl -s -I http://10.11.1.X/.svn/

# If .git is exposed, dump the full repository:
git-dumper http://10.11.1.X/.git/ ./dumped_repo/
# Or use gitjack
gitjack -u http://10.11.1.X/.git/
```

### 7.3 Common Backup & Config File Extensions
Always probe for backup copies of core files:
- `config.php.bak`, `config.php.old`, `config.php.save`, `config.php.txt`
- `index.php~`, `.index.php.swp`, `.index.php.swo` (Vim swap files)
- `.env`, `.env.local`, `.env.backup`
- `web.config`, `web.config.bak`
- `settings.py`, `database.yml`, `config.json`

---

## 🎯 8. OSCP Web Enumeration Decision Tree & Traps Checklist

### 🌲 Decision Tree
1. **Port Scan finds Port 80/443/8080/8000/5000:**
   - Grab banners (`curl -I`, `whatweb`).
   - Add domain to `/etc/hosts` if hostname or SSL certificate CN is present.
2. **Initial Browser Walkthrough:**
   - View `robots.txt`, `sitemap.xml`.
   - Click every button and submit form to populate Burp Suite site map.
   - Inspect page source, comments, and JavaScript files.
3. **Fuzzing Phase:**
   - Run `ffuf` directory discovery with `directory-list-2.3-medium.txt`.
   - Run `ffuf` file discovery with extensions matching the target tech (`.php`, `.aspx`, `.txt`, `.bak`, `.old`).
   - If domain name exists, run VHost fuzzing with `-H "Host: FUZZ.domain.local" -fs <size>`.
4. **Endpoint Deep-Dive:**
   - If endpoint accepts parameters (e.g. `page.php?file=...`), test for LFI/RFI/Command Injection.
   - If login form exists, test SQLi bypass (`' OR '1'='1`), default credentials (`admin:admin`, `admin:password`, `root:root`), and password spraying.
   - If file upload form exists, test extension filtering, MIME types, and webshell execution.

### ⚠️ Common Traps & Pitfalls
- ❌ **Failing to check non-standard ports:** Web servers are often on ports `8000`, `8080`, `8443`, `8888`, `9000`, `5000`, `3000`.
- ❌ **Missing VHosts:** Forgetting to fuzz virtual hosts when the default page looks like standard Apache/IIS landing page.
- ❌ **Trusting client-side validation:** JavaScript validation, hidden inputs, or disabled buttons can easily be bypassed in Burp Suite.
- ❌ **Ignoring response sizes in fuzzing:** A custom 404 page returning HTTP 200 will flood fuzzers unless filtered with `-fs` or `-fl`.

---

## 🔗 Related Notes & Next Modules
- [[06 PEN-200 Modules 1-5 Study Guide]]
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[Gobuster]]
- [[01 Theory Roadmap & Resources]]
- **Next Up:** Module 9 (Common Web Application Attacks - Directory Traversal, LFI, RFI, File Upload, OS Command Injection) & Module 10 (SQL Injection).
