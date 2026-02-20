`nmap -p 445 --open -oG - [Target_Range] | grep "445/open" | awk '{print $2}' | while read ip; do enum4linux -a $ip > "enum_$ip.txt"; done`

Then `grep -l "alfred" enum_*.txt`

Otherwise, step-by-step:
1. ``nmap -p 445 --open -oG smb_hosts.txt - [Target_Range]`
2. `enum4linux -a [ip from previous step] > enum_{ip}.txt`
3. `grep -l "alfred" enum_*.txt`
