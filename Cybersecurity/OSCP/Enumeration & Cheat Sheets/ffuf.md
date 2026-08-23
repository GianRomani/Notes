---
tags:
  - oscp
  - web_enumeration
  - ffuf
  - directory-fuzzing
  - parameter-fuzzing
  - vhost
  - cheatsheet
created: 2026-08-21
status: active
---

# ⚡ ffuf (Fuzz Faster U Fool) — OSCP Cheatsheet & Comprehensive Guide

**`ffuf`** is an extremely fast web fuzzer written in Go. It is considered the **gold standard tool for OSCP** because it seamlessly handles directory/file discovery, virtual host (VHost) enumeration, GET/POST parameter discovery, and raw data fuzzing using a unified, consistent syntax with powerful filtering capabilities.

---

## 📌 1. The `FUZZ` Keyword Mental Model

In `ffuf`, the keyword `FUZZ` acts as a placeholder that gets replaced line-by-line with entries from your wordlist:
- In URL path: `http://10.11.1.X/FUZZ` (Directory/file discovery)
- In HTTP Header: `-H "Host: FUZZ.domain.com"` (Virtual host enumeration)
- In Query String: `http://10.11.1.X/index.php?FUZZ=test` (GET parameter discovery)
- In POST Body: `-d "username=admin&password=FUZZ"` (Password / auth brute-forcing)

---

## 📌 2. Essential Parameters & Flags Breakdown

| Flag | Parameter | Description / Pentest Use Case |
| :--- | :--- | :--- |
| **`-u`** | Target URL | The target endpoint containing the `FUZZ` keyword (e.g. `-u http://10.11.1.X/FUZZ`). |
| **`-w`** | Wordlist | Path to wordlist, with optional custom keyword alias (e.g. `-w wordlist.txt:W1`). |
| **`-e`** | Extensions | Comma-separated extension list (e.g. `-e .php,.html,.txt,.bak,.old`). |
| **`-t`** | Threads | Number of concurrent worker threads (default: `40`). Fast & stable. |
| **`-c`** | Colorized Output | Colorizes status codes in terminal (`200` green, `301` blue, `403` yellow, `500` red). |
| **`-v`** | Verbose Output | Displays full URL and redirect target (`Location:` header). |
| **`-o` / `-of`** | Output & Format | Saves results (`-o results.json -of json` or `-o results.md -of md`). |
| **`-recursion`** | Recursive Fuzzing | Automatically recurses into newly discovered subdirectories. |
| **`-recursion-depth`** | Max Recursion Depth | Restricts depth of directory crawling (e.g. `-recursion-depth 2`). |
| **`-x`** | Proxy | Routes all requests through an HTTP/S proxy (e.g. `-x http://127.0.0.1:8080` for Burp Suite). |

---

## 📌 3. Powerful Response Matching & Filtering (The Magic of ffuf)

When a web server returns catch-all responses, wildcard redirects, or custom 404 pages, `ffuf` provides fine-grained match and filter controls:

```
┌─────────────────────────────────────────────────────────────┐
│                    MATCH vs FILTER FLAGS                    │
├──────────────────────────────┬──────────────────────────────┤
│  MATCH FLAGS (Show ONLY)     │  FILTER FLAGS (HIDE / DROP)  │
├──────────────────────────────┼──────────────────────────────┤
│  -mc (Match Status Code)     │  -fc (Filter Status Code)    │
│  -ms (Match Response Size)   │  -fs (Filter Response Size)  │
│  -mw (Match Word Count)      │  -fw (Filter Word Count)     │
│  -ml (Match Line Count)      │  -fl (Filter Line Count)     │
│  -mr (Match Regex Pattern)   │  -fr (Filter Regex Pattern)  │
└──────────────────────────────┴──────────────────────────────┘
```

### Solving the Wildcard / Catch-All Redirect Issue in ffuf
If a server returns `301` or `200` with length `0` for non-existent pages (the exact error encountered in Gobuster), filter out size `0` instantly with **`-fs 0`**:

```bash
ffuf -u http://192.168.71.16/FUZZ \
  -w /usr/share/wordlists/dirb/common.txt \
  -fs 0 \
  -c
```

---

## 📌 4. Practical `ffuf` Command Recipes

### 1. Directory & File Discovery (Standard Web Fuzzing)
```bash
# Directory discovery with colorized output and 404 filter
ffuf -u http://10.11.1.X/FUZZ \
  -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt \
  -c -fc 404

# File discovery with extensions & size filter
ffuf -u http://10.11.1.X/FUZZ \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt \
  -e .php,.html,.txt,.bak,.old,.zip \
  -fs 0 \
  -c
```

---

### 2. Virtual Host (VHost) Discovery (Host Header Fuzzing)
> [!important] Crucial for Shared Hosting
> When multiple hostnames point to the same IP address, fuzz the `Host` header. Always filter the default page response size (`-fs <default_size>`)!

```bash
# 1. Step 1: Note the response size of the default IP page:
curl -s -I http://10.11.1.X/ # or check length in browser

# 2. Step 2: Fuzz the Host header and filter out the default size:
ffuf -u http://target.local \
  -H "Host: FUZZ.target.local" \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -fs 1024 \
  -c
```

---

### 3. Hidden Parameter Discovery (GET & POST)

#### A. GET Parameter Discovery
Find undocumented URL query parameters (e.g. `page.php?debug=1`, `view.php?file=...`):
```bash
ffuf -u "http://10.11.1.X/index.php?FUZZ=test" \
  -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  -fs <default_page_size> \
  -c
```

#### B. POST Parameter Discovery
Find hidden parameters sent inside POST request body:
```bash
ffuf -u "http://10.11.1.X/login.php" \
  -X POST \
  -d "FUZZ=admin" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  -fs <default_page_size> \
  -c
```

---

### 4. Advanced: Fuzzing Through Burp Suite (Proxy Inspection)
Send `ffuf` requests directly through Burp Suite (e.g. to inspect payloads or use Burp's session handling):

```bash
ffuf -u http://10.11.1.X/FUZZ \
  -w /usr/share/wordlists/dirb/common.txt \
  -x http://127.0.0.1:8080 \
  -t 5
```

---

## ⚖️ Gobuster vs. ffuf Quick Comparison

| Feature | `gobuster` | `ffuf` (Recommended) |
| :--- | :--- | :--- |
| **Speed** | Very fast (Go) | Extremely fast (Go) |
| **Placement Flexibility** | Primarily path/vhost/dns flags | `FUZZ` placeholder anywhere (URL, Header, Body, Cookie) |
| **Filtering Options** | `-b` (Status codes), `--exclude-length` | `-fs` (Size), `-fc` (Code), `-fw` (Words), `-fl` (Lines), `-fr` (Regex) |
| **Parameter Fuzzing** | Limited (`fuzz` mode) | Native & Industry standard |
| **Recursion** | No (manual subpath runs) | Yes (`-recursion -recursion-depth N`) |

---

## 🔗 Related Notes
- [[Gobuster]]
- [[08 PEN-200 Module 8 - Intro to Web Applications]]
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[Information Gathering]]
