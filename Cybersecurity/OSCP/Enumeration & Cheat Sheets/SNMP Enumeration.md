Created: 2026-03-03 12:18
#note

**SNMP enumeration** is the process of extracting detailed information from network devices by querying the Simple Network Management Protocol. SNMP is typically enabled on routers, switches, firewalls, printers, and servers for network health monitoring — but if misconfigured, it exposes a massive amount of sensitive data including system information, network configuration, active services, and user accounts. SNMP enumeration is a key step in [[Information Gathering]], usually performed after [[Port scanning]] identifies UDP port 161 as open.

## Core Concepts

- **MIB (Management Information Base)** — a virtual database organising network management entities hierarchically
- **OID (Object Identifier)** — a numeric sequence pointing to a specific MIB node (e.g., `1.3.6.1.2.1.1.1.0` for system description)
- **Community Strings** — act as passwords for SNMPv1 and SNMPv2c:
  - *Public:* generally read-only access
  - *Private:* generally read-write access, allowing configuration changes

## Information Gathered During Enumeration

If an attacker guesses or brute-forces the community string (often left as the default "public"), they can extract:

- **System information** — OS version, hardware details, system name, uptime
- **Network configuration** — routing tables, ARP tables, DNS information
- **Interfaces** — active network interfaces, IP addresses, MAC addresses
- **Active services** — open ports and running processes
- **User data** — local user accounts, logged-in users, shared resources

## Tools

### Onesixtyone — Speed Scanner

Used for quickly sweeping large subnets for exposed port 161 and brute-forcing community strings. Sends requests asynchronously, making it much faster than sequential scanners.

`onesixtyone -c dict.txt -i hosts.txt`

Uses a dictionary of common community strings (`dict.txt`) against a list of target IPs (`hosts.txt`).

### Snmpwalk — Deep Diver

Once a target and community string are known, snmpwalk extracts everything the device will share by "walking" the MIB tree via continuous `GETNEXT` requests.

`snmpwalk -v 2c -c public 192.168.1.100`

Walks the entire MIB tree using SNMPv2c with community string "public".

### Nmap NSE Scripts

Nmap's scripting engine provides targeted, well-formatted SNMP enumeration:

- `snmp-brute` — brute-forces community strings
- `snmp-processes` — lists running processes and their arguments
- `snmp-win32-users` — extracts local user accounts from Windows machines

`nmap -sU -p 161 --script snmp-interfaces,snmp-sysdescr 192.168.1.100`

Scans UDP port 161 and runs scripts to list network interfaces and system description.

## Mitigation and Defense

- **Upgrade to SNMPv3** — v1 and v2c send community strings in plain text; v3 supports authentication and encryption
- **Change default strings** — never use "public" or "private"; treat community strings like strong passwords
- **Restrict access** — use ACLs or firewalls to limit SNMP communication to trusted management IPs on UDP port 161
- **Disable unnecessary services** — if a device does not need SNMP monitoring, disable it entirely

## References

1. [Nmap SNMP Scripts](https://nmap.org/nsedoc/scripts/)
2. [Onesixtyone](https://github.com/trailofbits/onesixtyone)

#### Tags
#oscp #snmp #enumeration #cybersecurity #penetration_testing
