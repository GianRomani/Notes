Created: 2026-03-03 12:05
#note

**Port scanning** is the process of probing a target host or network to identify open TCP and UDP ports and the services behind them. It is a core step in the [[Information Gathering]] phase, following passive reconnaissance and preceding targeted enumeration ([[SNMP Enumeration]], [[Gobuster]], [[SMB Enumeration]]). The primary tools are Nmap and Netcat for Linux, and `Test-NetConnection` with PowerShell for Windows environments.

## TCP Scanning with Netcat

Netcat provides a lightweight port scan without requiring Nmap:

`nc -nvv -w 1 -z {ip} {port_range}`

- `-w 1` — connection timeout of 1 second
- `-z` — zero-I/O mode (scanning, sends no data)

## UDP Scanning with Netcat

`nc -nv -u -z -w 1 {ip} {port_range}`

## Nmap

### Monitoring Scan Traffic

Before starting a scan, it is useful to measure the traffic it generates using iptables:

```
sudo iptables -I INPUT 1 -s {ip} -j ACCEPT
sudo iptables -I OUTPUT 1 -d {ip} -j ACCEPT
sudo iptables -Z
```

- `-I` inserts a rule into INPUT/OUTPUT chains
- `-s` / `-d` specify source/destination IP
- `-j ACCEPT` allows the traffic
- `-Z` zeros packet and byte counters

After the scan, check generated traffic with `sudo iptables -vn -L`.

### Traffic Considerations for Large Networks

For a class C network (254 hosts), a full Nmap scan generates over 1000 MB of traffic. Key principles:

- Both TCP and UDP scans should ideally be run on each host, but this is resource-intensive
- On bandwidth-constrained networks, balance thoroughness with efficiency
- For class A/B networks (thousands–millions of hosts), efficient scanning methods become essential

### SYN Scanning (Stealth Scan)

SYN scanning is the default and most popular Nmap technique. It sends SYN packets without completing the TCP handshake — if a port is open, the target responds with SYN-ACK, and the scanner never sends the final ACK.

`sudo nmap -sS {ip}`

**Note:** The "stealth" label is historical — older applications failed to log incomplete handshakes, but modern firewalls and IDS detect SYN scans reliably.

### TCP Connect Scan

When the user lacks raw socket privileges, Nmap defaults to a full TCP connect scan (slower than SYN):

`nmap -sT {ip}`

### UDP Scanning

Nmap uses two methods: an empty packet for most ports (relying on ICMP port unreachable responses), and protocol-specific packets for common ports like SNMP (port 161). See [[SNMP Enumeration]] for SNMP-specific scanning.

`sudo nmap -sU {ip}`

**Note:** UDP scanning can be combined with TCP SYN scanning (`-sS -sU`) for a more complete picture.

### Network Sweeping

Scan full networks rather than single hosts:

`nmap -sn 192.168.50.1-253`

Save results in greppable format with `-oG`:

`nmap -v -sn 192.168.50.1-253 -oG ping-sweep.txt`

Scan a specific port across a range (e.g., to find web servers):

`nmap -p 80 192.168.50.1-253 -oG web-sweep.txt`

Scan the top 20 most common ports with OS detection, script scanning, and traceroute:

`nmap -sT -A --top-ports=20 192.168.50.1-253 -oG top-port-sweep.txt`

Port frequency data comes from `/usr/share/nmap/nmap-services` (three-column format: service name, port/protocol, frequency from internet-wide scans).

### OS Fingerprinting

Operating systems use slightly different TCP/IP stack implementations (varying default TTL values, TCP window sizes). Nmap leverages these differences to guess the target OS:

`sudo nmap -O 192.168.50.14 --osscan-guess`

**Note:** Banners can be modified by administrators to fake service names and mislead attackers. OS fingerprinting is not 100% accurate.

### Nmap Scripting Engine (NSE)

NSE runs user-created scripts from `/usr/share/nmap/scripts` to automate various tasks: DNS enumeration, brute force attacks, vulnerability identification. View script details with `--script-help`.

## Windows Port Scanning

### Test-NetConnection

PowerShell's built-in tool for port scanning from Windows machines:

`Test-NetConnection -Port 445 192.168.50.151`

### PowerShell One-Liner for Range Scanning

Scan the first 1024 ports on a target by creating a TcpClient socket for each port:

`1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null`

This pipes integers 1–1024 into a for-loop, creates a `Net.Sockets.TcpClient` object for each, and logs open ports.

## References

1. [Nmap Documentation](https://nmap.org/docs.html)
2. [Nmap Services File](https://nmap.org/book/nmap-services.html)

#### Tags
#oscp #port_scanning #nmap #enumeration #cybersecurity #penetration_testing
