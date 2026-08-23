---
tags:
  - oscp
  - web_enumeration
  - gobuster
  - directory-fuzzing
  - vhost
  - cheatsheet
created: 2026-08-21
updated: 2026-08-21
---

# 🚀 Gobuster — Comprehensive Guide & Troubleshooting Cheat Sheet

**Gobuster** is a high-performance directory, DNS, and virtual host brute-forcing tool written in Go. Its multi-threaded concurrency makes it significantly faster than legacy tools like DirBuster or Dirb. It is a staple tool for web enumeration during PEN-200 labs and the OSCP exam.

---

## 📌 1. Gobuster Operating Modes

| Mode | Command Syntax | Description & Pentest Use Case |
| :--- | :--- | :--- |
| **`dir`** | `gobuster dir [flags]` | Brute-forces web directories and file paths on HTTP/HTTPS servers. |
| **`vhost`** | `gobuster vhost [flags]` | Enumerates virtual hosts on a target IP by brute-forcing the `Host:` header. |
| **`dns`** | `gobuster dns [flags]` | Subdomain brute-forcing via DNS queries against a target domain. |
| **`fuzz`** | `gobuster fuzz [flags]` | Generic replacement mode substituting the `FUZZ` keyword anywhere in URL/headers/body. |
| **`s3`** | `gobuster s3 [flags]` | Scans for publicly accessible or misconfigured AWS S3 buckets. |

---

## 📌 2. Detailed Parameter & Flag Breakdown (`dir` mode)

### Essential Flags
- **`-u <URL>`**: Target URL including protocol (e.g. `-u http://192.168.71.16` or `-u https://192.168.71.16:8443`).
- **`-w <PATH>`**: Path to wordlist (e.g. `-w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt`).
- **`-x <EXTENSIONS>`**: File extensions to search for, comma-separated without dots (e.g. `-x php,html,txt,bak,old,zip,json`).
- **`-t <THREADS>`**: Number of concurrent worker threads. Default is `10`. Recommended for OSCP labs: `30`–`50`.
- **`-o <OUTPUT_FILE>`**: Saves output to a clean text file for notes/reporting (e.g. `-o gobuster_port80.txt`).
- **`-k` / `--no-tls-validation`**: Skips SSL/TLS certificate verification (crucial for self-signed HTTPS lab targets).

### Status Code & Filtering Flags
- **`-s <STATUS_CODES>`**: Positive status codes to report (default: `200,204,301,302,307,401,403`).
- **`-b <STATUS_CODES>`**: Blacklisted/negative status codes to exclude (default: `404`). Example: `-b 301,404` to suppress redirects.
- **`--exclude-length <LENGTH>`**: **Excludes responses of specific body byte length**. Essential when wildcard redirects or custom 404 pages return a constant size.
- **`--wildcard`**: Forces Gobuster to continue operation when wildcard/catch-all responses are detected.

### Request Customization Flags
- **`-H "Header: Value"`**: Appends custom HTTP headers (e.g. `-H "X-Forwarded-For: 127.0.0.1"` or `-H "Cookie: PHPSESSID=..."`).
- **`-a <USER_AGENT>`**: Custom User-Agent string.
- **`-U <USER> -P <PASS>`**: HTTP Basic Authentication credentials.
- **`-c <COOKIES>`**: Pass session cookies directly (e.g. `-c "session=xyz"`).
- **`--delay <DURATION>`**: Adds a delay between requests (e.g. `--delay 100ms`) to avoid crashing fragile services or triggering WAF blocks.

---

## 📌 3. Common Gobuster Issues & Real-World Fixes

### ⚠️ Issue 1: Wildcard / Catch-All Redirect Error (The Redirection Trap)

#### The Error Output:
```text
the server returns a status code that matches the provided options for non existing urls. 
http://192.168.71.16/3bfcda3e-4372-4318-bee4-1aa9c2bb3268 => 301 (redirect to http://192.168.71.16/3bfcda3e-4372-4318-bee4-1aa9c2bb3268/) (Length: 0). 
Please exclude the response length or the status code or set the wildcard option.. To continue please exclude the status code or the length
```

#### Why it Happens:
Before Gobuster starts scanning, it tests a random UUID string (e.g., `/3bfcda3e-...`) to see how the server responds to non-existent pages. Many web servers (Apache, Nginx, or single-page apps) are configured to automatically redirect *every* request without a trailing slash using a **`301 Moved Permanently`** or **`302 Found`** with a body length of `0`. 

Because `301` is in Gobuster's default list of valid status codes, Gobuster aborts to avoid flooding your terminal with thousands of false positives.

#### 💡 Fix (Recommended First Choice): Exclude the Response Length
Filter out responses whose content length is exactly `0` bytes (or whatever length the error message reported):

```bash
gobuster dir \
  -u http://192.168.71.16 \
  -w /usr/share/wordlists/dirb/common.txt \
  --exclude-length 0 \
  -t 30
```

#### Alternative Fixes:
- **Use `--wildcard`**: Tells Gobuster to accept the wildcard response and calibrate internally:
  ```bash
  gobuster dir -u http://192.168.71.16 -w /usr/share/wordlists/dirb/common.txt --wildcard -t 30
  ```
- **Blacklist status code 301 (`-b 301`)**: If you only want `200 OK` and `403 Forbidden` responses:
  ```bash
  gobuster dir -u http://192.168.71.16 -w /usr/share/wordlists/dirb/common.txt -b 301,404 -t 30
  ```

---

### ⚠️ Issue 2: HTTPS / SSL Handshake Failure
- **Symptom:** `Get "https://10.11.1.X": tls: failed to verify certificate: x509: certificate signed by unknown authority`
- **Fix:** Add `-k` flag to disable certificate verification:
  ```bash
  gobuster dir -u https://10.11.1.X -k -w /usr/share/wordlists/dirb/common.txt
  ```

---

### ⚠️ Issue 3: Virtual Host Discovery on Shared Hosting / Non-Default Sites
- **Symptom:** Browsing to `http://10.11.1.X` shows default Apache/IIS landing page, but SSL certificate or Nmap scripts indicate domain name `target.local`.
- **Command:** Use `vhost` mode to find hidden subdomains hosted on the same IP:
  ```bash
  gobuster vhost \
    -u http://target.local \
    -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
    --append-domain \
    -t 30 \
    -o gobuster_vhost.txt
  ```

---

## 📌 4. Practical Gobuster Command Recipes

```bash
# 1. Quick Initial Discovery (dirb common.txt)
gobuster dir -u http://10.11.1.X -w /usr/share/wordlists/dirb/common.txt -t 30 --exclude-length 0

# 2. Deep Directory & File Search with Extensions (SecLists Medium)
gobuster dir \
  -u http://10.11.1.X \
  -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt \
  -x php,html,txt,bak,old,zip,json \
  --exclude-length 0 \
  -t 40 \
  -o gobuster_deep.txt

# 3. Authenticated Scan with Cookie Header
gobuster dir \
  -u http://10.11.1.X \
  -w /usr/share/wordlists/dirb/common.txt \
  -H "Cookie: PHPSESSID=d94f29a0b12f4587c" \
  -t 30

# 4. Target Specific Subdirectory Discovered from Initial Scan
gobuster dir \
  -u http://10.11.1.X/admin/ \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt \
  -x php,txt,config,bak \
  -t 30
```

---

## 🔗 Related Notes
- [[ffuf]] — Modern, high-speed alternative for directories, parameters, and vhosts.
- [[08 PEN-200 Module 8 - Intro to Web Applications]]
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[Information Gathering]]
