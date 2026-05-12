"""
ascii.py - Plain-text content for curl clients
========================================================================================

ASCII portfolio and manpage strings returned when the request comes from curl or
from the man.arpatek.dev hostname. ANSI escape codes add color in supporting terminals.

Author: Juan Garcia (arpatek)
"""

# ──[ ANSI Codes ]──────────────────────────────────────────────────────────────────────
R  = '\033[0m'          # reset
C1 = '\033[38;5;109m'   # teal    — links (#9db9b2)
C2 = '\033[38;5;115m'   # green   — boxes, legend labels (#79be9a)
C3 = '\033[38;5;188m'   # light   — body text (#dcd6d6)
DM = '\033[2m'          # dim     — decorative lines
BD = '\033[1m'          # bold

# gradient rows: muted red → pink → gold → teal → green → near-white
G0 = '\033[38;5;138m'   # #b9746f muted red
G1 = '\033[38;5;181m'   # #cd9b98 dusty pink
G2 = '\033[38;5;180m'   # #c3b283 muted gold
G3 = '\033[38;5;109m'   # #9db9b2 teal
G4 = '\033[38;5;115m'   # #79be9a sage green
G5 = '\033[38;5;151m'   # #a2d2b9 mint
G6 = '\033[38;5;188m'   # #dcd6d6 near-white

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
  {C1}https://arpatek.dev{R} | {DM}"No future. Only uptime."{R}


{C2}┌─About───────────────────────────┐{R} {C2}┌─Links────┬────────────────────────────────┐{R}
{C2}│{R}                                 {C2}│{R} {C2}│{R}          {C2}│{R}                                {C2}│{R}
{C2}│{R}  Systems automation engineer    {C2}│{R} {C2}│{R} Codeberg {C2}│{R} {C1}codeberg.org/arpatek{R}           {C2}│{R}
{C2}│{R}  based in California. 3 years   {C2}│{R} {C2}│{R} LinkedIn {C2}│{R} {C1}linkedin.com/in/arpatek{R}        {C2}│{R}
{C2}│{R}  of hardware & UNIX lab work at {C2}│{R} {C2}│{R}          {C2}│{R}                                {C2}│{R}
{C2}│{R}  TrueNAS. Now building a        {C2}│{R} {C2}└──────────┴────────────────────────────────┘{R}
{C2}│{R}  self-hosted homelab using IaC. {C2}│{R} {C2}┌─Latest────────────────────────────────────┐{R}
{C2}│{R}                                 {C2}│{R} {C2}│{R}  RHCSA                        {C1}in progress{R} {C2}│{R}
{C2}└─────────────────────────────────┘{R} {C2}└───────────────────────────────────────────┘{R}

  {C2}Legend{R}

  {C1}$ curl arpatek.dev{R}        Get this page
  {C1}$ curl arpatek.dev/man{R}    Full resume in manpage format
  {C1}$ curl arpatek.dev/help{R}   All available endpoints



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

# ──[ Uses ]────────────────────────────────────────────────────────────────────────────
USES = (
f"""
{C2}USES(1){R}                    Hardware & Software                    {C2}USES(1){R}

{C2}HARDWARE{R}
       {BD}M1 Mac Mini{R}
       {C1}Main workstation{R} | macOS

       {BD}M1 MacBook Air{R}
       {C1}Laptop{R} | Asahi Linux

       {BD}ASUS PN51 — Ryzen 7 5700U{R}
       {C1}Proxmox hypervisor{R} | devstem

       {BD}Raspberry Pi{R}
       {C1}DNS / DHCP / VPN{R} | netrunner-rpi

{C2}SOFTWARE{R}
       {C1}Shell{R}       zsh (Mac, Asahi)  |  bash (servers)
       {C1}Editor{R}      Neovim + LazyVim (Mac, MacBook)  |  Vim (RHEL)
       {C1}Terminal{R}    iTerm2 (Mac)  |  Ghostty (MacBook)
       {C1}OS{R}          macOS  |  Asahi Linux  |  Rocky Linux 9  |  Debian 13

{C2}USES(1){R}                    California, USA                    {C2}USES(1){R}
"""
)

# ──[ Lab ]─────────────────────────────────────────────────────────────────────────────
LAB = (
f"""
{C2}LAB(1){R}                         home.arpa                         {C2}LAB(1){R}

{C2}INFRASTRUCTURE{R}
       {BD}Proxmox VE 9{R}
       {C1}devstem{R} | ASUS PN51 (Ryzen 7 5700U) | pve.arpatek.dev
              Single-node hypervisor. All VMs run here. No cluster, no HA.

       {BD}k3s — 3-node cluster{R}
       {C1}prod-k3s-master-0 + 2 workers{R} | Debian 13
              Traefik ingress, cert-manager wildcard TLS (Let's Encrypt).
              Runs arpatek.dev and proxies all internal service UIs publicly.

{C2}IDENTITY & NETWORK{R}
       {BD}FreeIPA{R}
       {C1}prod-ipa-0{R} | Rocky Linux 9
              Central identity, SSH auth, sudo policy, DNS for home.arpa.

       {BD}Pi-hole{R}
       {C1}netrunner-rpi{R} | Raspberry Pi | pi.arpatek.dev
              Network-wide DNS, DHCP, content filter. Upstream for FreeIPA.

       {BD}WireGuard{R}
       {C1}netrunner-rpi{R} | Raspberry Pi
              VPN into 10.33.111.0/24. Clients use Pi-hole for DNS.

{C2}DEV & OBSERVABILITY{R}
       {BD}Gitea + act_runner{R}
       {C1}prod-git-0{R} | Debian 13 | git.arpatek.dev
              Self-hosted Git, container registry, and CI/CD.
              Push-to-deploy pipeline for arpatek.dev.

       {BD}PLG Stack — Prometheus, Loki, Grafana{R}
       {C1}prod-mon-0{R} | Debian 13 | gf.arpatek.dev | pm.arpatek.dev
              Hub-and-spoke observability. node_exporter + cAdvisor + Alloy
              agents ship metrics and logs from every host.

{C2}LAB(1){R}                         home.arpa                         {C2}LAB(1){R}
"""
)

# ──[ Changelog ]───────────────────────────────────────────────────────────────────────
CHANGELOG = (
f"""
{C2}CHANGELOG(1){R}                    arpatek                    {C2}CHANGELOG(1){R}

{C2}2026-05{R}
       {BD}site{R}     /uses, /lab, /changelog pages added
       {BD}lab{R}      Traefik ingresses for all internal services
                (pve, pi, gf, pm.arpatek.dev via k3s + Cloudflare)
       {BD}site{R}     Styling pass — dark background, underscore cursor,
                viewport fill, box-shadow cleanup
       {BD}site{R}     Initial launch — terminal animation, screensaver,
                ASCII art banner, easter eggs (/gif /boo /xmas)
       {BD}lab{R}      k3s cluster provisioned, arpatek.dev on Kubernetes,
                wildcard TLS via cert-manager + Let's Encrypt
       {BD}lab{R}      Gitea + act_runner CI/CD pipeline (push-to-deploy)
       {BD}lab{R}      PLG observability stack (Prometheus, Loki, Grafana)
       {BD}lab{R}      Identity and network layer — FreeIPA, Pi-hole, WireGuard

{C2}CHANGELOG(1){R}                    arpatek                    {C2}CHANGELOG(1){R}
"""
)

# ──[ Help ]────────────────────────────────────────────────────────────────────────────
HELP = (
f"""
  {C2}arpatek.dev — available endpoints{R}

  {C1}$ curl arpatek.dev{R}             This page
  {C1}$ curl arpatek.dev/man{R}          Full resume in manpage format
  {C1}$ curl arpatek.dev/uses{R}         Hardware & software setup
  {C1}$ curl arpatek.dev/lab{R}          Homelab services (home.arpa)
  {C1}$ curl arpatek.dev/changelog{R}    Site and project history
  {C1}$ curl arpatek.dev/help{R}         This list

  {C2}hidden{R}

  {C1}$ curl arpatek.dev/gif{R}          Trippy circle animation
  {C1}$ curl arpatek.dev/boo{R}          👻
  {C1}$ curl arpatek.dev/xmas{R}         🎄

"""
)
