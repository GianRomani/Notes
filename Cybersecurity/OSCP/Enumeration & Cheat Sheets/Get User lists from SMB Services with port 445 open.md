Created: 2026-03-03 12:17
#quicknote

Extracting user lists from exposed SMB services (port 445) is a common enumeration step in OSCP labs, typically performed after [[Port scanning]] identifies open SMB ports and before attempting password attacks. The workflow uses Nmap for discovery and **enum4linux** for detailed enumeration, which queries SMB and NetBIOS to extract user accounts, shares, group memberships, and password policies. See [[SMB Enumeration]] for broader SMB enumeration context.

## One-Liner Approach

Scan a range for port 445, then enumerate each host and search for a specific user:

`nmap -p 445 --open -oG - [Target_Range] | grep "445/open" | awk '{print $2}' | while read ip; do enum4linux -a $ip > "enum_$ip.txt"; done`

Then search results for a target username:

`grep -l "alfred" enum_*.txt`

## Step-by-Step Approach

1. `nmap -p 445 --open -oG smb_hosts.txt [Target_Range]` — find hosts with SMB open
2. `enum4linux -a [ip] > enum_{ip}.txt` — full enumeration of each host
3. `grep -l "alfred" enum_*.txt` — search for target user across results

**Note:** The `-a` flag in enum4linux runs all enumeration modules (users, shares, groups, policies). For targeted enumeration, use `-U` (users only) or `-S` (shares only) to reduce noise and time.

## Resources

1. [enum4linux](https://github.com/CiscoCXSecurity/enum4linux)

#### Tags
#oscp #smb #enumeration #user_enumeration #cybersecurity #penetration_testing
