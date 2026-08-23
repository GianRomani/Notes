---
tags:
  - oscp
  - burpsuite
  - web
  - authentication
  - intruder
  - repeater
  - troubleshooting
  - cheatsheet
created: 2026-08-22
status: active
---

# 🕵️ Burp Suite — Authentication Attacks, Intruder Mastery & Troubleshooting Guide

> **Target Goal:** Complete field reference for intercepting HTTP traffic, extracting login parameters, configuring Burp Intruder for password brute-forcing/spraying, triaging attack responses, and troubleshooting common real-world failure traps during PEN-200 and the OSCP exam.

---

## 🧭 1. Burp Proxy Interception Workflow

```
[ Browser / Target Action ] ──► [ Burp Proxy (127.0.0.1:8080) ] ──► [ HTTP History Log ] ──► [ Send to Tool ]
 (Submit login / forms)          (Keep Intercept OFF by default)     (Filter by POST/target)   (Repeater / Intruder)
```

### Golden Workflow Rule: Keep "Intercept is OFF" by Default
- **Why?** Having `Intercept is on` blocks *every single* CSS, JS, font, and background browser request, making pages hang indefinitely and appear broken.
- **The Pro Workflow:**
  1. Leave **`Intercept is off`** in **Proxy $\rightarrow$ Intercept**.
  2. Navigate the website and submit forms freely in your browser.
  3. Go to **Proxy $\rightarrow$ HTTP history** tab.
  4. Find the relevant request (filter by **`POST`** method or target URL).
  5. Right-click the request $\rightarrow$ **Send to Repeater (`Ctrl+R`)** for manual probing or **Send to Intruder (`Ctrl+I`)** for automation.

---

## 🔍 2. Anatomy of an HTTP Request: Headers vs. Body

Understanding where parameters live is essential to placing payload markers correctly:

```http
POST /portal HTTP/1.1                    <── 1. Request Line (Method, Path, Protocol)
Host: 192.168.56.52                      <── 2. Request Headers (Host, Headers, Cookies)
User-Agent: Mozilla/5.0 ...
Content-Type: application/x-www-form-urlencoded
Content-Length: 38
                                         <── 3. Mandatory Blank Line (CRLF)
username=admin&password=test&debug=0     <── 4. Request Body (Form Parameters / JSON Data)
```

- **`GET` Requests:** Parameters are in the URL line at the top (e.g. `GET /portal?username=admin&password=test HTTP/1.1`).
- **`POST` Requests:** Parameters are in the **Body** at the bottom below the blank line.

---

## 🎯 3. Burp Intruder Setup & Position Configuration

### 3.1 Intruder Attack Types
- **`Sniper` (Single variable):** Tests one list of payloads across one or more positions sequentially. **Use this for password brute-forcing a known username (`admin`).**
- **`Pitchfork` (Paired lists):** Iterates through 2 lists simultaneously in lock-step (User1:Pass1, User2:Pass2). **Use for credential stuffing when you have paired lists.**
- **`Cluster Bomb` (Matrix permutations):** Tests every password in List B against every user in List A ($N \times M$). **Use when spraying multiple usernames with multiple passwords.**

---

### 3.2 Setting Payload Positions (`Positions` Tab)

```
┌─────────────────────────────────────────────────────────────┐
│                   INTRUDER POSITIONS SETUP                  │
├─────────────────────────────────────────────────────────────┤
│ 1. Attack type: Select 'Sniper'                             │
│ 2. Click 'Clear §' to remove all auto-assigned markers      │
│ 3. Highlight ONLY the target value                          │
│ 4. Click 'Add §' to wrap strictly around target value       │
└─────────────────────────────────────────────────────────────┘
```

#### ✅ Correct Position Example:
```http
username=admin&password=§admin§&debug=0
```
*Intruder swaps the actual password string on every iteration.*

#### ❌ The Common "Phantom Append" Trap (Identical Length Failure):
```http
username=admin&password=admin&debug=0§§
```
*Why this fails:* The markers `§§` were placed at the very end. Intruder leaves `password=admin` fixed and appends the wordlist to `debug=0` (e.g. `debug=0zeddemore`), causing every attempt to fail with the exact same error response length!

---

### 3.3 Loading Payloads (`Payloads` Tab)
1. **Payload Set:** `1`
2. **Payload Type:** `Simple list`
3. **Loading Wordlists:**
   - **Target-hosted wordlists:** If a custom list is hosted on the target (e.g. `http://<IP>/passwords.txt`), download it first via CLI:
     ```bash
     curl -s http://<TARGET_IP>/passwords.txt -o /tmp/passwords.txt
     ```
   - In Burp, click **Load...** $\rightarrow$ select `/tmp/passwords.txt`.
   - **Standard Kali Wordlists:** `/usr/share/wordlists/fasttrack.txt` or `/usr/share/wordlists/rockyou.txt`.
4. **Payload Encoding:** Ensure **URL-encode these characters** is checked so special characters don't corrupt HTTP form encoding.

---

## 📊 4. Triage & Identifying the Successful Login

When the Attack Results window opens (after clicking OK on the Community Edition pop-up):

```
┌───────┬──────────────┬────────┬────────┬───────────────────────────┐
│ Req # │ Payload      │ Status │ Length │ Result Interpretation     │
├───────┼──────────────┼────────┼────────┼───────────────────────────┤
│ 1     │ password123  │ 200    │ 354    │ ❌ Failed Attempt         │
│ 2     │ admin123     │ 200    │ 353    │ ❌ Failed Attempt         │
│ 3     │ zeddemore    │ 302    │ 2450   │ 🎯 SUCCESS! (Length/Code) │
│ 4     │ letmein      │ 200    │ 354    │ ❌ Failed Attempt         │
└───────┴──────────────┴────────┴────────┴───────────────────────────┘
```

1. **Sort by `Length` Column:** Failed attempts typically share the exact same response length (e.g. `353`–`354` bytes). The valid password produces an **anomaly** in length (e.g. `2450` or `312` bytes).
2. **Sort by `Status` Column:** Successful authentication often triggers a **`302 Found`** redirect to the dashboard or admin portal.
3. **Inspect Response Body:** Click the anomalous request $\rightarrow$ switch to **Response** tab $\rightarrow$ search for `Welcome`, `Dashboard`, `Session`, or `Set-Cookie:`.

---

## 🛠️ 5. Troubleshooting: What to Do When All Requests Fail

If every row in Intruder returns identical lengths and failed status codes, run through this diagnostic checklist:

| Symptom / Cause | Root Cause | Exact Solution |
| :--- | :--- | :--- |
| **Identical lengths (~353/354 bytes)** | Target markers placed incorrectly (`§§` at end of body). | Go to **Positions** tab, click **`Clear §`**, highlight only the password value, click **`Add §`**. |
| **Wrong Target VM / Path** | Lab exercises often have multiple VMs or updated paths (`/portal` vs root `/`). | Check exercise prompt: verify target IP and target path (`http://<IP>/` vs `http://<IP>/portal`). |
| **Hidden Debug Parameters** | Application has a parameter like `debug=0` controlling verbose error output. | Send request to **Repeater (`Ctrl+R`)**, change `debug=0` to `debug=1`, click Send to inspect verbose error traces. |
| **Anti-CSRF / Nonce Token Required** | Server requires a fresh CSRF token per login attempt. | Community Intruder cannot extract dynamic nonces easily $\rightarrow$ use Burp Macros or a Python script / `hydra`. |
| **Intruder Speed Throttling** | Burp Community Edition introduces artificial delays. | For larger wordlists, switch to high-speed CLI tools like **`ffuf`** or **`hydra`**. |

---

## ⚡ 6. High-Speed CLI Alternative: `ffuf` Form Brute-Force

When wordlists have hundreds or thousands of passwords and Burp Community is too slow:

```bash
# Form POST brute-force with ffuf
ffuf -u http://192.168.56.52/portal \
  -X POST \
  -d "username=admin&password=FUZZ&debug=0" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -w /tmp/passwords.txt \
  -fs 354 \
  -c
```

- **`-X POST`**: Sends HTTP POST requests.
- **`-d "..."`**: Form body substituting `FUZZ` in the password position.
- **`-fs 354`**: Filters out the failure response size so **only the successful login is displayed**!

---

## 🔗 Related Notes
- [[08 PEN-200 Module 8 - Intro to Web Applications]]
- [[09 Web Enumeration & Fuzzing Methodology]]
- [[ffuf]]
- [[Gobuster]]
- [[00 OSCP Master Study Plan]]
