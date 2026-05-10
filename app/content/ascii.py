"""
ascii.py - Plain-text content for curl clients
========================================================================================

ASCII portfolio and manpage strings returned when the request comes from curl or
from the man.arpatek.dev hostname. ANSI escape codes add color in supporting terminals.

Author: Juan Garcia (arpatek)
"""

# ──[ ANSI Codes ]──────────────────────────────────────────────────────────────────────
R  = '\033[0m'          # reset
C1 = '\033[38;5;51m'    # neon cyan   — links, accents
C2 = '\033[38;5;198m'   # hot pink    — boxes, legend labels
C3 = '\033[38;5;214m'   # amber       — body text
DM = '\033[2m'          # dim         — decorative lines
BD = '\033[1m'          # bold

# gradient rows: magenta → purple → blue → cyan
G0 = '\033[38;5;201m'
G1 = '\033[38;5;171m'
G2 = '\033[38;5;141m'
G3 = '\033[38;5;99m'
G4 = '\033[38;5;63m'
G5 = '\033[38;5;45m'
G6 = '\033[38;5;51m'

# ──[ Portfolio ]───────────────────────────────────────────────────────────────────────
PORTFOLIO = (
f"""

{G0}         :::     :::::::::  :::::::::     ::: ::::::::::: :::::::::: :::    :::{R}
{G1}       :+: :+:   :+:    :+: :+:    :+:  :+: :+:   :+:     :+:        :+:   :+:{R}
{G2}     +:+   +:+  +:+    +:+ +:+    +:+ +:+   +:+  +:+     +:+        +:+  +:+{R}
{G3}   +#++:++#++: +#++:++#:  +#++:++#+ +#++:++#++: +#+     +#++:++#   +#++:++{R}
{G4}  +#+     +#+ +#+    +#+ +#+       +#+     +#+ +#+     +#+        +#+  +#+{R}
{G5} #+#     #+# #+#    #+# #+#       #+#     #+# #+#     #+#        #+#   #+#{R}
{G6}###     ### ###    ### ###       ###     ### ###     ########## ###    ###{R}

  {BD}Juan Garcia{R} — Linux technologist & automation engineer
  {C1}https://arpatek.dev{R} | {C1}https://codeberg.org/arpatek{R}


{C2}┌─About───────────────────────────┐{R} {C2}┌─Links────┬────────────────────────────────┐{R}
{C2}│{R}                                 {C2}│{R} {C2}│{R}          {C2}│{R}                                {C2}│{R}
{C2}│{R}  Systems automation engineer    {C2}│{R} {C2}│{R} Codeberg {C2}│{R} {C1}codeberg.org/arpatek{R}           {C2}│{R}
{C2}│{R}  based in California. 3 years   {C2}│{R} {C2}│{R} LinkedIn {C2}│{R} {C1}linkedin.com/in/arpatek{R}        {C2}│{R}
{C2}│{R}  of hardware & UNIX lab work at {C2}│{R} {C2}│{R}          {C2}│{R}                                {C2}│{R}
{C2}│{R}  TrueNAS. Now building a        {C2}│{R} {C2}└──────────┴────────────────────────────────┘{R}
{C2}│{R}  self-hosted homelab using IaC. {C2}│{R}
{C2}│{R}  RHCSA in progress.             {C2}│{R}
{C2}│{R}                                 {C2}│{R}
{C2}└─────────────────────────────────┘{R}

  {C2}Legend{R}

  {C1}$ curl arpatek.dev{R}        Get this page
  {C1}$ curl arpatek.dev/man{R}    Full resume in manpage format



"""
)

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = (
f"""
{C2}ARPATEK(1){R}                    Personal Manual                    {C2}ARPATEK(1){R}

{C2}NAME{R}
       arpatek -- {BD}Juan Garcia{R}, Linux technologist & automation engineer

{C2}SYNOPSIS{R}
       juan [--automate] [--build] [--break-then-fix]

{C2}DESCRIPTION{R}
       Systems automation engineer with production experience building
       hardware validation tooling at scale. Strong background in Linux,
       Bash, Python, and infrastructure-as-code. Hands-on with Ansible,
       Terraform, Kubernetes, and self-hosted infrastructure monitoring
       stacks. Pursuing RHCSA cert; roadmap includes RHCE, Terraform
       Associate, CKA, CKS, and AWS.

       Location: California, USA
       Email:    {C1}juang.sh@proton.me{R}

{C2}EXPERIENCE{R}
       {BD}Senior Test Technician{R}
       {C1}TrueNAS{R} | 2021 – 2024

              * Built a 22,000+ line Bash/Python automation suite (CC &
                SWQC) for TrueNAS manufacturing QC
              * Automated BIOS, firmware, and HW validation via IPMI and
                Redfish API for 16+ systems at once
              * Developed Python Redfish API clients for BIOS push/export
                on liquid immersion platforms
              * Integrated with PBS archive servers and PostgreSQL to
                automate burn-in parsing and reporting
              * Validated firmware compliance against Redbook specs: ZFS
                pool status, HBA firmware, SMART health
              * Automated multi-node HA pair diffing and generated diff
                sheets for QC traceability

       {BD}Computer Hardware Technician{R}
       {C1}EMR CPR/Corovan{R} | 2021

              * Reconfigured and relocated desktop/server systems
              * Troubleshot hardware/software issues and blueprinted
                workstation layouts

       {BD}Post Production Specialist{R}
       {C1}Freelance{R} | 2016 – 2021

              * Managed AV setup, live audio/video services, and video editing
              * Designed and executed digital marketing strategies for SMBs

       {BD}Passenger Service Supervisor{R}
       {C1}Pacific Aviation{R} | 2019 – 2021

              * Coordinated airline operations between international teams

{C2}SKILLS{R}
       {C1}Languages{R}       Bash, Python, HCL
       {C1}Systems{R}         Linux (RHEL, Ubuntu, TrueNAS/FreeBSD), TCP/IP,
                       VLANs, ZFS, SAS/HBA, BIOS, IPMI, Redfish API
       {C1}IaC{R}             Terraform, Ansible, Puppet
       {C1}Containers{R}      Docker, Kubernetes (k3s)
       {C1}Observability{R}   Prometheus, Grafana, Loki, Alloy, node_exporter
       {C1}Services{R}        FreeIPA, Gitea, WireGuard, Pi-hole
       {C1}Tools{R}           Git, Vim, tmux, SSH

{C2}PROJECTS{R}
       {C1}home.arpa{R}        Self-hosted homelab — IaC, monitoring, identity,
                        DNS, VPN, and container orchestration
       {C1}terraform-xo{R}     XCP-ng VM provisioning via Terraform + XO API
       {C1}ansible-baseline{R} Post-provisioning automation for Debian VMs
       {C1}puppet-modules{R}   Puppet module collection for homelab VM hardening
       {C1}snaputil{R}         Modular system snapshot tool
       {C1}citadel{R}          Pattern-based password generator
       {C1}portal-22{R}        SSH key & config generator from YAML

{C2}EDUCATION{R}
       Red Hat Certified System Administrator          {C1}In Progress{R}
       Google IT Automation with Python Professional   Completed
       Google IT Support Professional Certificate      Completed
       IT Support & Services / Advanced IT             JobTrain & StreetCode Academy

{C2}LANGUAGES{R}
       English   Fluent
       Spanish   Fluent

{C2}SEE ALSO{R}
       {C1}arpatek.dev{R}   {C1}codeberg.org/arpatek{R}   {C1}linkedin.com/in/arpatek{R}

{C2}ARPATEK(1){R}                    California, USA                    {C2}ARPATEK(1){R}
"""
)
