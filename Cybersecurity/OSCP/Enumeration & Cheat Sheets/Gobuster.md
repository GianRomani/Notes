Created: 2026-03-03 12:19
#quicknote

**Gobuster** is a fast command-line brute-forcing tool written in Go, used by penetration testers for discovering hidden directories, subdomains, and virtual hosts. Its Go-based concurrency makes it significantly faster than older alternatives like DirBuster or Dirb. Gobuster is typically used during web application enumeration after [[Port scanning]] identifies HTTP/HTTPS services, as part of the [[Information Gathering]] phase.

- **`dir` mode** — brute-forces URLs to find hidden directories and files (e.g., `/admin`, `/login.php`, `/backup.zip`) on a web server
- **`dns` mode** — brute-forces subdomains of a target domain (e.g., `dev.target.com`, `staging.target.com`) to map external attack surface
- **`vhost` mode** — discovers hidden virtual hosts on a single IP, useful when multiple web applications are hosted on the same server but not in public DNS
- **`s3` mode** — scans for open or unsecured Amazon S3 buckets associated with a target

## Basic Usage

Like [[SNMP Enumeration]] tools such as onesixtyone, Gobuster relies heavily on wordlists. Standard directory brute-force:

`gobuster dir -u http://192.168.50.151 -w /usr/share/wordlists/dirb/common.txt`

- `-u` specifies the target URL
- `-w` specifies the wordlist

**Note:** Seclists (`/usr/share/seclists/`) provides more comprehensive wordlists for different scenarios. See [[Information Gathering]] for the full Seclists reference.

## Resources

1. [Gobuster GitHub](https://github.com/OJ/gobuster)
2. [Seclists](https://github.com/danielmiessler/SecLists)

#### Tags
#oscp #web_enumeration #gobuster #cybersecurity #penetration_testing
