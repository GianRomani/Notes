Created: 2026-07-24 13:50
#note

# 🎯 OSCP Master Study Plan (Aug - Dec 2026)

> [!important] Exam & Subscription Strategy
> - **Subscription Expiry:** Early December 2026.
> - **Exam Attempt #1:** Target **Late October / First Week of November (Oct 26 – Nov 1, 2026)**.
> - **Mandatory Cooling-Off Window:** Nov 2 – Nov 15, 2026.
> - **Exam Attempt #2 (Retake Buffer):** Target **Late November (Nov 16 – Nov 29, 2026)** — Safely before subscription expiry!

---

## 📌 Weekly Study Schedule & Capacity
- **Mon - Thu (1 hr/day max):** Theory, module reading, PortSwigger/Tib3rius videos, note taking in Obsidian, command cheat sheet refinement.
- **Friday (Dedicated Deep-Dive Day, 8–10 hrs):** Practical machine exploitation, PEN-200 Challenge Labs, AD domain compromise, full mock exams.
- **Total Capacity:** ~12–14 hours per week.

---

## 📊 16-Week Weekly Schedule Breakdown Table

| Week | Date Range | Linear Cycle | Linear Milestone | Primary Focus & Deliverables |
| :--- | :--- | :--- | :--- | :--- |
| **W1** | Jul 27 – Aug 2 | Cycle 1 | Milestone 1 | Vault Setup & PEN-200 Modules 1–5 (CLI, Bash, Nmap, Netcat) |
| **W2** | Aug 3 – Aug 9 | Cycle 2 | Milestone 1 | PEN-200 Modules 6–10 (Recon & Burp Suite) + Tib3rius Linux PrivEsc (`ClamAV`) |
| **W3** | Aug 10 – Aug 16 | Cycle 3 | Milestone 1 | PEN-200 Modules 11–15 (Web SQLi/LFI, Exploit Fix) + TCM AD (`Nibbles`, `Helpdesk`, `Kevin`) |
| **W4** | Aug 17 – Aug 23 | Cycle 4 | Milestone 1 | Phase 1 Polish & Standalone Warmup (HTB `Active` AD) |
| **W5** | Aug 24 – Aug 30 | Cycle 5 | Milestone 2 | PEN-200 Modules 16–24 & Tib3rius Windows PrivEsc (Medtech Lab M1) |
| **W6** | Aug 31 – Sep 6 | Cycle 6 | Milestone 2 | PortSwigger Web Academy & Medtech Lab M2 / DC Compromise |
| **W7** | Sep 7 – Sep 13 | Cycle 7 | Milestone 2 | PEN-200 Challenge Lab 2: Relia (M1 & M2 Domain Pwning) |
| **W8** | Sep 14 – Sep 20 | Cycle 8 | Milestone 2 | AD Kerberoasting & Relia DC + PG Practice (`Hutch`, `Heist`) |
| **W9** | Sep 21 – Sep 27 | Cycle 9 | Milestone 3 | Ligolo-ng Pivoting & Tunneling Masterclass (HTB `Forest`, `Sauna`) |
| **W10**| Sep 28 – Oct 4 | Cycle 10 | Milestone 3 | Skylark Enterprise Lab (Part 1 - Dual-Homed Pivoting & PG `Hotline`, `Syringe`) |
| **W11**| Oct 5 – Oct 11 | Cycle 11 | Milestone 3 | Skylark Enterprise Lab (Part 2 - Domain Trust Pwning & PG `Hekate`, `Pebble`) |
| **W12**| Oct 12 – Oct 18 | Cycle 12 | Milestone 3 | TJnull Medium Standalones (`Craft`, `PyScript`, `Sentinel`, `Internal`) |
| **W13**| Oct 19 – Oct 25 | Cycle 13 | Milestone 4 | **OSCP-A 24-hr Mock Exam Simulation** & Report Writing Practice |
| **W14**| **Oct 26 – Nov 1**| Cycle 14 | Milestone 4 | **🎯 EXAM ATTEMPT #1** (Sit Official OSCP Exam + 24h Report) |
| **W15**| Nov 2 – Nov 15 | Cycle 15 | Milestone 4 | Cooling-Off Window / Weak Vector Refinement & **OSCP-B Mock Exam** |
| **W16**| **Nov 16 – Nov 29**| Cycle 16 | Milestone 4 | **🛡️ EXAM ATTEMPT #2 (Backup Retake Window before sub expiry)** |

---

## 🗓️ Phase Breakdown & Useful Links

### Phase 1: Foundations, Web & AD Fundamentals (August 2026)
- **Cycle 1 (Jul 27 – Aug 2):** PEN-200 Modules 1–5 (Orientation, Linux CLI, Bash Scripting, Netcat, Nmap basics) + Obsidian Vault Setup.
- **Cycle 2 (Aug 2 – Aug 9):** PEN-200 Modules 6–10 (Recon, Port Scanning, Web App Intro, Burp Suite) + Tib3rius Linux PrivEsc.
- **Cycle 3 (Aug 9 – Aug 16):** PEN-200 Modules 11–15 (Web Attacks: SQLi, LFI/RFI, Cmd Injection; Exploit Fixing; AV Evasion) + TCM PEH AD Section.
- **Cycle 4 (Aug 17 – Aug 23):** Standalone Warmup Machines (`ClamAV`, `Nibbles`, `Helpdesk`, `Kevin`, `Active`).
- **Key Resources:**
  - [NetSecFocus TJnull OSCP Machine List](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/)
  - [Tib3rius Linux PrivEsc Notes](https://github.com/tib3rius/linux-privesc-notes)
  - [PEASS-ng (LinPEAS/WinPEAS)](https://github.com/peass-ng/PEASS-ng)

### Phase 2: PEN-200 Course Completion & Challenge Labs (September 2026)
- **Cycle 5 (Aug 23 – Aug 30):** PEN-200 Modules 16–24 + Tib3rius Windows PrivEsc.
- **Cycle 6 (Aug 30 – Sep 6):** PortSwigger Web Security Academy + PEN-200 Challenge Lab 1: [[05 Machine Progress Tracker#Medtech|Medtech]].
- **Cycle 7 (Sep 6 – Sep 13):** PEN-200 Challenge Lab 2: [[05 Machine Progress Tracker#Relia|Relia]].
- **Cycle 8 (Sep 13 – Sep 20):** PG & HTB AD Sets (`Hutch`, `Heist`, `Forest`, `Sauna`).
- **Key Resources:**
  - [PortSwigger Web Security Academy](https://portswigger.net/web-security)
  - [Tib3rius Windows PrivEsc Notes](https://github.com/tib3rius/windows-privesc-notes)
  - [OffSec Learning Library Portal](https://portal.offsec.com/)

### Phase 3: Advanced Enterprise Labs & Pivoting (October 2026)
- **Cycle 9 (Sep 20 – Sep 27):** [[04 Pivoting with Ligolo-ng|Ligolo-ng Pivoting Guide]] & Multi-hop Tunneling.
- **Cycle 10–11 (Sep 27 – Oct 11):** PEN-200 Challenge Lab 3: [[05 Machine Progress Tracker#Skylark|Skylark (Enterprise Lab)]].
- **Cycle 12 (Oct 11 – Oct 18):** PG Practice Medium Standalones (`Hotline`, `Syringe`, `Hekate`, `Pebble`, `Craft`, `PyScript`, `Sentinel`, `Internal`).
- **Key Resources:**
  - [Ligolo-ng Pivoting Repository](https://github.com/nico-cha30/ligolo-ng)
  - [0xdf Hacks Stuff Writeups](https://0xdf.gitlab.io/)
  - [BloodHound Python Ingester](https://github.com/dirkjanm/BloodHound.py)

### Phase 4: Mock Exams & Exam Attempts (November - Early December 2026)
- **Cycle 13 (Oct 18 – Oct 25):** 24-hr Simulation — Official **OSCP-A Mock Exam**.
- **Cycle 14 (Oct 26 – Nov 1):** **🎯 EXAM ATTEMPT #1**
- **Cycle 15 (Nov 1 – Nov 15):** Weak point refinement, PG Practice hard standalones, **OSCP-B Mock Exam**.
- **Cycle 16 (Nov 16 – Nov 29):** **🛡️ EXAM ATTEMPT #2 (Backup retake window before sub expiry!)**
- **Key Resources:**
  - [Reddit r/oscp Community & Advice](https://www.reddit.com/r/oscp/)
  - [Reddit OSCP Passed Tips & Guide](https://www.reddit.com/r/oscp/comments/181x4y9/oscp_passed_guide_and_tips/)

---

#### Links & Related Notes
- [[01 Theory Roadmap & Resources]]
- [[02 Active Directory Attack Methodology]]
- [[03 Privilege Escalation Guide]]
- [[04 Pivoting with Ligolo-ng]]
- [[05 Machine Progress Tracker]]
- [[Information Gathering]]
- [[SMB Enumeration]]
- [[Port scanning]]

#### Tags
#oscp #study_plan #certification #penetration_testing #active_directory #cybersecurity
