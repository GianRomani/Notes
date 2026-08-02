Created: 2026-07-24 14:02
#note

# 📚 OSCP External Theory & Practice Resources Roadmap

> [!tip] Theory vs Practical Strategy
> Use **Weekdays (Mon-Thu)** to digest these resources in small 1-hour chunks.
> Apply every concept immediately on **Fridays** in hands-on lab machines.

---

## 🔖 Raindrop Saved Bookmarks & Community Labs (Your Collection)

- 📌 [Free Active Directory Lab for OSCP Prep (Reddit)](https://www.reddit.com/r/oscp/s/rm74hrQohr)
- 📌 [HackerBlueprint | OSCP AD Chains Tracker](https://docs.google.com/spreadsheets/u/0/d/1FBzafhtRXI9ngXIdVRpyoMndKJ-v6JgWqIKZfr1xBNA/htmlview)
- 📌 [(FREE LAB) OSCP-Like AD Chains/Sets Built Specifically for Exam Prep](https://www.reddit.com/r/oscp/s/3cT0MELRaN)
- 📌 [OffSec - p4n4Sec (PG Practice Guide)](https://p4n4.xyz/posts/offsec)
- 📌 [AD-Attacking-Notes GitHub Repository](https://github.com/jlizarragavil/AD-Attacking-Notes/blob/main/ad.md)
- 📌 [Passed OSCP 100 points in 7 hours (Reddit Debrief)](https://www.reddit.com/r/oscp/s/g9S4iEyfWn)

---

## 1. Active Directory (AD) Exploitation (40 Points on Exam)
- **Official Course:** OffSec PEN-200 AD Modules.
- **TCM Security - Practical Ethical Hacking (PEH):**
  - Watch the Active Directory section (Password Spraying, LLMNR/NBT-NS Poisoning, Kerberoasting, AS-REP Roasting, Pass-the-Hash, DCSync).
- **Useful External Links:**
  - [Impacket GitHub Repository](https://github.com/fortra/impacket)
  - [BloodHound Python Ingester](https://github.com/dirkjanm/BloodHound.py)
  - [PayloadsAllTheThings Active Directory Architecture](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Active%20Directory%20Methodology)

---

## 2. Privilege Escalation (Linux & Windows)
- **Tib3rius Courses (Udemy / TryHackMe):**
  - *Linux Privilege Escalation for OSCP:* Sudo rights (`sudo -l`), SUID binaries, Capabilities, Cron Jobs, Writable `/etc/passwd`, NFS shares, Kernel exploits.
  - *Windows Privilege Escalation for OSCP:* Service permissions (Unquoted Service Paths, Insecure Service Executables), AlwaysInstallElevated, Token Impersonation (`PrintSpoofer`, `GodPotato`, `JuicyPotato`), Password hunting in registry/files.
- **Useful External Links:**
  - [Tib3rius Linux PrivEsc Cheatsheet](https://github.com/tib3rius/linux-privesc-notes)
  - [Tib3rius Windows PrivEsc Cheatsheet](https://github.com/tib3rius/windows-privesc-notes)
  - [PEASS-ng (LinPEAS / WinPEAS)](https://github.com/peass-ng/PEASS-ng)
  - [GTFOBins (Linux SUID/Sudo binaries)](https://gtfobins.github.io/)
  - [LOLBAS (Windows Binaries)](https://lolbas-project.github.io/)

---

## 3. Web Vulnerability Deep-Dive
- **PortSwigger Web Security Academy (Free):**
  - [PortSwigger Main Academy](https://portswigger.net/web-security)
  - [SQL Injection (SQLi)](https://portswigger.net/web-security/sql-injection)
  - [Directory Traversal / LFI](https://portswigger.net/web-security/file-path-traversal)
  - [OS Command Injection](https://portswigger.net/web-security/os-command-injection)
  - [File Upload Vulnerabilities](https://portswigger.net/web-security/file-upload)
  - [Server-Side Request Forgery (SSRF)](https://portswigger.net/web-security/ssrf)

---

## 4. Pivoting & Tunneling (Ligolo-ng Gold Standard)
- **Ligolo-ng:** Modern TUN interface tunneling tool.
  - [Ligolo-ng Official Repository](https://github.com/nico-cha30/ligolo-ng)
  - [Ligolo-ng Documentation & Usage](https://nico-cha30.github.io/ligolo-ng/)
  - See [[04 Pivoting with Ligolo-ng]] for command syntax.

---

## 5. Walkthroughs, Writeups & Community Guides
- [0xdf Hacks Stuff (Best HTB & PG Machine Writeups)](https://0xdf.gitlab.io/)
- [IPPSec Video Search Engine](https://ippsec.rocks/)
- [Reddit r/oscp Community](https://www.reddit.com/r/oscp/)

---

#### Tags
#oscp #resources #theory #cheatsheets #privesc #active_directory #web_security #raindrop
