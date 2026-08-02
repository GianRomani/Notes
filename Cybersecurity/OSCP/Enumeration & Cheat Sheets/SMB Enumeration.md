Created: 2026-03-03 12:10
#quicknote

**SMB (Server Message Block)** is an application-layer network protocol for shared access to files, printers, and serial ports between nodes on a network. SMB enumeration is a key step in [[Information Gathering]] for Windows-dominant environments, typically performed after [[Port scanning]] identifies port 445 as open. Related techniques include [[Get User lists from SMB Services with port 445 open]] for extracting user accounts via enum4linux.

- **Default ports:** TCP 445 (modern SMB/CIFS) and TCP 139 (NetBIOS over TCP)
- **Why it matters:** Misconfigured SMB shares often expose sensitive files, user lists, and credentials — a common entry point in OSCP lab environments
- **Key tools:** `enum4linux`, `smbclient`, `smbmap`, Nmap NSE scripts (`smb-enum-shares`, `smb-enum-users`)

## Resources

1. [enum4linux Documentation](https://github.com/CiscoCXSecurity/enum4linux)
2. [Nmap SMB Scripts](https://nmap.org/nsedoc/scripts/)

#### Tags
#oscp #smb #enumeration #cybersecurity #penetration_testing
