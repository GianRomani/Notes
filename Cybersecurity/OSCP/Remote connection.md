Created: 2026-03-03 12:16
#quicknote

**Remote connection** tools allow penetration testers to interact with target systems after discovering open services via [[Port scanning]]. The choice of tool depends on the target OS and protocol: RDP (TCP 3389) for Windows graphical access, SSH (TCP 22) for Linux/Unix command-line access, and various others for specific services. Establishing reliable remote access is essential for post-exploitation and lateral movement in OSCP lab environments.

- **xfreerdp3 (RDP):** The recommended tool for connecting to Windows targets via Remote Desktop Protocol. Supports NLA, clipboard redirection, and drive mounting:
  `xfreerdp3 /u:username /p:password /v:IP_address`
- **SSH:** Standard for Linux targets. Key-based authentication is preferred over passwords:
  `ssh user@IP_address`
- **Evil-WinRM:** PowerShell-based remote shell for Windows targets with WinRM enabled (port 5985/5986):
  `evil-winrm -i IP_address -u username -p password`

**Note:** After initial access, these tools are also used for lateral movement between compromised hosts within the target network.

## Resources

1. [xfreerdp man page](https://linux.die.net/man/1/xfreerdp)
2. [Evil-WinRM](https://github.com/Hackplayers/evil-winrm)

#### Tags
#oscp #remote_access #rdp #ssh #cybersecurity #penetration_testing
