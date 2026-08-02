Created: 2026-03-03 12:00
#note

**Information gathering** (or reconnaissance) is the first phase of any penetration test and arguably the most important — the quality of enumeration directly determines the attack surface available for exploitation. This note covers passive and active techniques for collecting intelligence about a target, from Google dorking and DNS enumeration to source code analysis and certificate transparency logs. Thorough information gathering typically leads into [[Port scanning]], [[Whois]] lookups, [[SNMP Enumeration]], and establishing [[Remote connection]] to target systems.

## Passive Information Gathering

Passive techniques collect information without directly interacting with the target's infrastructure.

### Google Dorking

Google advanced operators narrow search results to target-specific data:

- `site:megacorpone.com filetype:txt` — find text files on the target domain
- `site:megacorpone.com ext:php` — identify programming languages and frameworks in use
- `intitle:"index of" "parent directory"` — find open directory listings exposing files and folder structure

The `ext` operator is useful for discerning which programming languages are used on a web site.

### DNS Enumeration

DNS records reveal subdomains, mail servers, and infrastructure layout:

- **DNSrecon** — automated DNS enumeration supporting zone transfers, reverse lookups, and brute-forcing
- **DNSenum** — similar capabilities with automatic WHOIS lookups on discovered IPs

### Source Code and Secrets

Public repositories and version control history often leak credentials, API keys, and internal paths:

- **Gitrob** — scans GitHub repositories for sensitive files and patterns
- **Gitleaks** — detects secrets (API keys, passwords, tokens) in git history

### Infrastructure Analysis

- **Shodan** — searches for internet-connected devices, revealing open ports, services, and banners without active scanning
- **Security Headers** — checks HTTP security headers on target web applications
- **SSL Labs** — evaluates TLS/SSL configuration and certificate chain

## Active Information Gathering

Active techniques interact directly with the target and may be detected.

After passive recon, the next step is typically active [[Port scanning]] to map open services, followed by targeted enumeration (e.g., [[SNMP Enumeration]], [[Gobuster]] for web directories, [[SMB Enumeration]] for Windows shares).

### Windows-Specific Tools

- `xfreerdp` — remote desktop connections to Windows targets (see [[Remote connection]])
- `nslookup` — DNS queries from Windows command line

## Resources

1. [Google Hacking DB](https://www.exploit-db.com/google-hacking-database)
2. [DorkSearch](https://dorksearch.com/)
3. [Gitrob](https://github.com/michenriksen/gitrob)
4. [Gitleaks](https://github.com/gitleaks/gitleaks)
5. [Shodan](https://www.shodan.io/)
6. [Security Headers](https://securityheaders.com/)
7. [SSL Labs](https://www.ssllabs.com/ssltest/)
8. [Seclists](https://github.com/danielmiessler/SecLists)
9. [DNSrecon](https://github.com/darkoperator/dnsrecon)
10. [DNSEnum](https://www.kali.org/tools/dnsenum/)

#### Tags
#oscp #reconnaissance #enumeration #cybersecurity #penetration_testing
