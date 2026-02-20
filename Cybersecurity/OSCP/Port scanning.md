
## TCP Scanning
`nc -nvv -w 1 -z {ip address} {port range}` -> *-w* option specifies the connection timeout in seconds, while *-z* specifies zero-I/O mode, which is used for scanning and sends no data.

## UDP Scanning
`nc -nv -u -z -w 1 {ip address} {port range}`

## Nmap
### TCP scan using Nmap
Before starting an Nmap scan, it is better to examine the amount of traffic sent by this type of scan -> `iptables`.
`sudo iptables -I INPUT 1 -s {ip address} -j ACCEPT`
`sudo iptables -I OUTPUT 1 -d {ip address} -j ACCEPT`
`sudo iptables -Z`
The *-I* option to insert a new rule into a given chain, which in this case includes both the **INPUT** (Inbound) and **OUTPUT** (Outbound) chains, followed by the rule number. We can use *-s* to specify a source IP address, *-d* to specify a destination IP address, and *-j* to ACCEPT the traffic. Finally, the *-Z* option zeros the packet and byte counters in all chains.

Then, simply, `nmap {ip address}` (or `nmap -p {port range} {ip address}`)

To have a clearer idea of how much traffic our scan generated -> `sudo iptables -vn -L`, where *-v* option adds some verbosity to the output, *-n* enables numeric output, and *-L* lists the rules present in all chains.

Summarizing:
1. **Network Size and Traffic**: For a class C network with 254 hosts, conducting a full Nmap scan would generate over 1000 MB of data. This is due to the large number of hosts requiring individual scans.
    
2. **Scan Types**: Ideally, both TCP and UDP port scans should be performed on each machine to gather detailed information about exposed services. However, this approach can be resource-intensive in terms of bandwidth usage.
    
3. **Traffic Restrictions and Balancing**: If network uplinks are limited, it's crucial to find a balance between thorough scanning and bandwidth efficiency. This might involve prioritizing certain scans or limiting the scope to optimize data transmission without overwhelming the network.
    
4. **Larger Networks (Class A/B)**: In even larger networks, such as class A or B (with thousands or millions of hosts), the need for this balance becomes even more critical. Efficient scanning methods are essential to gather necessary information without overburdening the network.
    
5. **Real-World Applications**: This principle is vital in real-world scenarios, especially within large corporations. Efficient and scalable methods are needed to gather data without causing unnecessary strain on network resources.

The most popular Nmap scanning technique is SYN, or "stealth" scanning. There are many benefits to using a SYN scan and as such, it is the default scan option used when no scan option is specified in an nmap command and the user has the required raw socket privileges.

#### SYN scanning
SYN scanning is a TCP port scanning method that involves sending SYN packets to various ports on a target machine without completing a TCP handshake. If a TCP port is open, a SYN-ACK should be sent back from the target machine, informing us that the port is open. At this point, the port scanner does not bother to send the final ACK to complete the three-way handshake.
`sudo nmap -sS {ip address}` 

**Note**: the term "Stealth" comes from the fact that in the past application would fail to log incomplete TCP Handshakes, but this is not happening anymore with modern firewalls. 

When a user running nmap does not have raw socket privileges, Nmap will default to the *TCP connect scan* technique (much slower than a SYN Scanning) -> `nmap -sT {ip address}`

### UDP Scan using Nmap
When conducting a UDP scan, Nmap employs two distinct methods to ascertain whether a port is open or closed. For most ports, it relies on the standard 'ICMP port unreachable' method by sending an empty packet to the specified port. However, for common ports such as 161, which are associated with SNMP, it utilizes a protocol-specific SNMP packet to elicit a response from applications bound to that port. To execute a UDP scan, the *-sU* option must be employed, and sudo access is necessary to interact with raw sockets.
`sudo nmap -sU {ip address}`.

**Note:** The UDP scan (*-sU*) can also be used in conjunction with a TCP SYN scan (*-sS*) to build a more complete picture of our target.

### Network Sweeping
Network sweeping techniques are used to scan full networks, instead of a single host. Example: `nmap -sn 192.168.50.1-253`

**Note:** Nmap's "greppable" output parameter, *-oG*, can be used to save these results in a more manageable format: `nmap -v -sn 192.168.50.1-253 -oG ping-sweep.txt`

We can also scan specific TCP or UDP ports, for example is we are already aware of vulnerabilities: `nmap -p 80 192.168.50.1-253 -oG web-sweep.txt`

To optimize time and network resources, we can efficiently scan multiple IP addresses by focusing on a concise list of commonly probed ports. For instance, we can perform a TCP connect scan using Nmap's *--top-ports* option to examine the top 20 TCP ports. This approach is facilitated by enabling OS version detection (*-OS*), script scanning (*-sC*), and traceroute tracking (*-A*) to gather comprehensive network intelligence.

The selection of these ports is determined through the */usr/share/nmap/nmap-services* file, which employs a straightforward three-column format. The first column lists the service name, followed by the port number and protocol in the second column, while the third column denotes the port frequency based on periodic research scans of the internet. Any content beyond the third column is typically ignored but is often used for comments, as indicated by the use of the pound sign (*#*).
`nmap -sT -A --top-ports=20 192.168.50.1-253 -oG top-port-sweep.txt`

By leveraging this method, we ensure that our network scanning process is both efficient and informative, balancing thoroughness with resource conservation.

##### OS fingerprinting
Operating systems often use slightly different implementations of the TCP/IP stack (such as varying default Time To Live (TTL) values and TCP window sizes) and Nmap can leverage this to guess the target OS -> `sudo nmap -O 192.168.50.14 --osscan-guess` (not 100% accurate).

**Note:** Banners can be modified by system administrators and intentionally set to fake service names to mislead potential attackers.

##### Nmap Scripting Engine (NSE)
NSE is used to lunch user-created scripts to automate various scanning tasks. These scripts perform a broad range of functions including DNS enumeration, brute force attacks, and even vulnerability identification. NSE scripts are in the `/usr/share/nmap/scripts` directory.

To view more information about a script, we can use the *--script-help* option, which displays a description of the script and a URL where we can find more in-depth information, such as the script arguments and usage examples.

## Test-NetConnection 
Tool for port scanning from a Windows machine -> `Test-NetConnection -Port 445 192.168.50.151`.

We can further automate the process by scripting the scanning of the first 1024 ports on a Domain Controller using a PowerShell one-liner. To achieve this, we instantiate a _TcpClient_ Socket object as part of the `Test-NetConnection` command to send additional traffic that is not essential for our specific scanning needs. This approach allows us to leverage existing network tools while ensuring that our custom requirements are met without unnecessary overhead -> `1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null`, which starts by piping the first 1024 integer into a for-loop, which assigns the incremental integer value to the *$_* variable. Then, it creates a *Net.Sockets.TcpClient* object and perform a TCP connection against the target IP on that specific port, and if the connection is successful, it prompts a log message that includes the open TCP port.

## SMB Enumeration
SMB is an application-layer network protocol primarily used for providing shared access to files, printers, and serial ports between nodes on a network