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

  {G6}${R} {G2}curl{R} {C1}arpatek.dev{R}              This page
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/man{R}          Full resume in manpage format
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/env{R}          Hardware & software setup
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/lab{R}          Homelab services (home.arpa)
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/status{R}       What I'm working on
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/latest{R}       Updates, reading, watching, playing
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/changelog{R}    Site and project history
  {G6}${R} {G2}curl{R} {C1}arpatek.dev/help{R}         All available endpoints



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
       Systems automation engineer with three years of hardware
       validation and QC automation. Strong background in Linux and
       Bash; hands-on with IPMI, Redfish, ZFS, and SAS/HBA. Runs a
       self-hosted lab on Proxmox, k3s, FreeIPA, and WireGuard. Pursuing
       RHCSA (EX200); roadmap includes AWS SAA, Terraform Associate,
       CKA, RHCE, and CKS.

{C2}EXPERIENCE{R}
       {BD}Independent Infrastructure Study{R}
       {C1}Personal Lab{R} | 2025 – Present

              * Self-hosted lab on Proxmox: 3-node k3s cluster, FreeIPA
                identity/DNS, Pi-hole HA pair
              * Runs arpatek.dev on k3s behind Traefik with wildcard
                TLS; single inbound UDP port for WireGuard
              * CI/CD via Gitea Actions and act_runner: builds to a
                self-hosted registry, rolls out to k3s on push
              * Metrics, logs, and dashboards across 6 hosts via
                Prometheus, Loki, Grafana, Alloy, node_exporter
              * Documented per service in home.arpa: architecture,
                decisions, gotchas, and upgrade notes
              * Preparing for RHCSA (EX200) on RHEL 10; Linux
                administration and Bash scripting coursework

       {BD}Senior Test Technician{R}
       {C1}TrueNAS{R} | 2021 – 2024

              * Extended and maintained a 22,000+ line Bash/Python
                automation suite (CC & SWQC) for manufacturing QC
              * Cut per-system validation from 30–60 min of manual
                checks to minutes of report review
              * Sustained batches of 50+ systems/day, raising
                configuration/QC throughput without added headcount
              * Automated BIOS, firmware, and HW validation via IPMI and
                Redfish API for 16+ server platforms
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

# ──[ Env ]─────────────────────────────────────────────────────────────────────────────
ENV = (
f"""
{C2}ENVIRON(7){R}                  Hardware & Software                  {C2}ENVIRON(7){R}

{C2}HARDWARE{R}
       {BD}M1 MacBook Air{R}
       {C1}Main workstation{R} | darwin | 2 aarch64 RHEL VMs, shared net

       {BD}M1 Mac Mini{R}
       {C1}Dedicated UTM hypervisor{R} | mizutani | 4 lab VMs, bridged

       {BD}ASUS PN51 — Ryzen 7 5700U{R}
       {C1}Proxmox hypervisor{R} | blackwall

       {BD}Raspberry Pi x2{R}
       {C1}DNS / DHCP / VPN / NAS{R} | netrunner + edgerunner

{C2}SOFTWARE{R}
       {C1}Shell{R}       zsh (macOS)  |  bash (servers)
       {C1}Editor{R}      Neovim + LazyVim (macOS)  |  Vim (RHEL)
       {C1}Terminal{R}    Ghostty
       {C1}OS{R}          macOS  |  RHEL 10  |  Rocky Linux 9  |  Debian 13

{C2}ENVIRON(7){R}                    California, USA                    {C2}ENVIRON(7){R}
"""
)

# ──[ Lab ]─────────────────────────────────────────────────────────────────────────────
LAB = (
f"""
{C2}LAB(8){R}                         home.arpa                         {C2}LAB(8){R}

{C2}INFRASTRUCTURE{R}
       {BD}Proxmox VE 9{R}
       {C1}blackwall{R} | ASUS PN51 (Ryzen 7 5700U) | pve.arpatek.dev
              Single-node hypervisor. All VMs run here. No cluster, no HA.

       {BD}k3s — 3-node cluster{R}
       {C1}erebus + sandevistan + kerenzikov{R} | Debian 13
              Traefik ingress, cert-manager wildcard TLS (Let's Encrypt).
              Runs arpatek.dev and proxies all internal service UIs publicly.

{C2}IDENTITY & NETWORK{R}
       {BD}FreeIPA{R}
       {C1}mikoshi{R} | Rocky Linux 9
              Central identity, SSH auth, sudo policy, DNS for home.arpa.

       {BD}Pi-hole — HA pair{R}
       {C1}netrunner + edgerunner{R} | Raspberry Pi | pi.arpatek.dev
              Network-wide DNS, DHCP, content filter. Upstream for FreeIPA.
              edgerunner runs a replica so DNS survives losing netrunner.

       {BD}SMB storage{R}
       {C1}netrunner + edgerunner{R} | Raspberry Pi
              tank — 500GB mdadm RAID1 of two WD Red SA500 SSDs on
              netrunner. nas 500GB and stor 250GB (M.2 SATA) on
              edgerunner, both over USB.

       {BD}WireGuard{R}
       {C1}netrunner{R} | Raspberry Pi
              VPN into 10.33.111.0/24. Clients use Pi-hole for DNS.

{C2}DEV & PRACTICE{R}
       {BD}errata{R}
       {C1}blackwall{R} | RHEL 10.0 | x86_64
              The RHCSA course VM, and the only x86 RHEL in the lab, so
              its minor stays pinned. Rebuilt from scratch whenever the
              course calls for a fresh install.

       {BD}UTM practice fleet{R}
       {C1}mizutani{R} | M1 Mac Mini | bridged
              gort (RHEL 10.2), talos (Debian 13), clank (Ubuntu 26.04),
              hal (Alpine 3.24). Reachable over LAN and WireGuard.

       {BD}Practice VMs{R}
       {C1}darwin{R} | M1 MacBook Air | shared networking
              glados and tars, both RHEL 10.2 on aarch64. For putting
              the course material to use rather than following it, so
              the minor is free to move. Outside FreeIPA — EX200
              assumes local users.

{C2}DEV & OBSERVABILITY{R}
       {BD}Gitea + act_runner{R}
       {C1}soulkiller{R} | Debian 13 | git.arpatek.dev
              Self-hosted Git, container registry, and CI/CD.
              Push-to-deploy pipeline for arpatek.dev.

       {BD}PLG Stack — Prometheus, Loki, Grafana{R}
       {C1}netwatch{R} | Debian 13 | gf.arpatek.dev | pm.arpatek.dev
              Hub-and-spoke observability. node_exporter + cAdvisor + Alloy
              agents ship metrics and logs from every host.

{C2}LAB(8){R}                         home.arpa                         {C2}LAB(8){R}
"""
)

# ──[ Changelog ]───────────────────────────────────────────────────────────────────────
CHANGELOG = (
f"""
{C2}CHANGELOG(7){R}                    arpatek                    {C2}CHANGELOG(7){R}

{C2}2026-09-08{R}
       {BD}site{R}     /uses renamed to /env; /now split into /status and
                /latest — old paths 301 redirect
       {BD}site{R}     /man and /cv resume rewritten — quantified QC
                outcomes, 2025–present lab entry, updated cert roadmap
       {BD}site{R}     /now and /uses refreshed — new reading list, Asahi and
                iTerm2 dropped, UTM drill VMs described
       {BD}lab{R}      Mac Mini repurposed as a dedicated UTM hypervisor;
                MacBook Air is now the main workstation
       {BD}lab{R}      edgerunner documented — Pi-hole replica, plus the
                nas and stor SMB shares alongside netrunner's tank

{C2}2026-06-02{R}
       {BD}lab{R}      All VMs renamed to Cyberpunk 2077 theme —
                blackwall, mikoshi, soulkiller, netwatch,
                erebus, sandevistan, kerenzikov, netrunner
       {BD}site{R}     Updated /uses, /lab, /now with current hostnames

{C2}2026-05-12{R}
       {BD}site{R}     /contact page, /cv PDF download, footer links redesign
       {BD}site{R}     /uses, /lab, /changelog pages; syntax-highlighted terminal,
                λ title, animated favicon, /lambda, screensaver removed
       {BD}lab{R}      Traefik ingresses — pve, gf, pm, pi.arpatek.dev
                publicly exposed via k3s + Cloudflare

{C2}2026-05-10{R}
       {BD}site{R}     Initial launch — terminal animation, ASCII art banner,
                easter eggs (/lambda /boo /xmas), /man resume
       {BD}lab{R}      k3s cluster, arpatek.dev on Kubernetes, wildcard TLS,
                cert-manager + Let's Encrypt, Gitea ingress

{C2}2026-04-30{R}
       {BD}lab{R}      PLG observability stack — Prometheus, Loki, Grafana
                central server + Debian & RHEL agents

{C2}2026-03-28{R}
       {BD}lab{R}      Gitea + act_runner CI/CD pipeline (push-to-deploy)

{C2}2026-03-01{R}
       {BD}lab{R}      FreeIPA — identity, SSH policy, HBAC, DNS for home.arpa

{C2}2026-02-21{R}
       {BD}lab{R}      WireGuard VPN — remote access into 10.33.111.0/24

{C2}2026-01-11{R}
       {BD}lab{R}      Pi-hole — DNS, DHCP, content filter (netrunner)

{C2}CHANGELOG(7){R}                    arpatek                    {C2}CHANGELOG(7){R}
"""
)

# ──[ Status ]──────────────────────────────────────────────────────────────────────────
STATUS = (
f"""
{C2}STATUS(1){R}                       2026-09-08                        {C2}STATUS(1){R}

{C2}CURRENT{R}
       {BD}RHCSA — EX200{R}
              Studying for the exam. The homelab buildout is done — it is a
              practice environment now, not a project.

       {BD}Vim drilling{R}
              EX200 has no GUI, so editing is the one skill that taxes every
              other task until it is automatic. Drill VMs live in UTM on
              Apple Silicon — a mixed-distro fleet bridged on the Mac Mini,
              two aarch64 RHEL VMs on the Air.

{C2}RECENT{R}
       {BD}NAS across both Pis{R}
              tank is a 500GB mdadm RAID1 of two WD Red SA500 SSDs on
              netrunner; nas and stor sit on edgerunner — stor a new 250GB
              M.2 SATA SSD. All three exported over SMB.

       {BD}devkit — WireGuard private key exposure{R}
              devkit pulled the WireGuard private key over SSH on every run.
              wg show all dump prints it as the first field of the first
              line, and a NOPASSWD sudoers rule made that passwordless.
              Dropped the rule, stripped it out of setup.sh, wrote down why.
              codeberg.org/arpatek/devkit/src/branch/main/docs/decisions.md

{C2}STATUS(1){R}                     California, USA                     {C2}STATUS(1){R}
"""
)

# ──[ Latest ]──────────────────────────────────────────────────────────────────────────
LATEST = (
f"""
{C2}LATEST(7){R}                       2026-09-08                        {C2}LATEST(7){R}

{C2}UPDATES{R}
       {BD}Daily driver — back on macOS{R}
              macOS on the M1 MacBook Air is the main workstation again. The
              Mac Mini was repurposed into a dedicated UTM hypervisor: 4
              bridged lab VMs there, 2 aarch64 RHEL VMs on the Air.

       {BD}Editor — VSCodium over VS Code{R}
              Same editor without the Microsoft telemetry and branding.
              Settings and extensions tracked in dotfiles.

       {BD}Terminal — Ghostty, with tmux for splits{R}
              macOS native tabs are exposed as separate AXWindows, so
              AeroSpace tiles each tab and leaves half the screen empty.
              Unbinding super+t forces the single-window path: tmux panes,
              or Ghostty's own splits on super+d.

       {BD}Window management — AeroSpace{R}
              Tiling on macOS, nine persistent workspaces.

{C2}READING{R}
       We — Yevgeny Zamyatin
       The Bible (RSVCE)
       Meditations — Marcus Aurelius
       Discourses and Selected Writings — Epictetus
       Confessions — Saint Augustine
       Beyond Good and Evil — Nietzsche
       Metamorphosis — Kafka
       A Tale of Two Cities — Charles Dickens
       Neuromancer — William Gibson
       Red Rising — Pierce Brown
       Behold a Pale Horse — William Cooper
       The Alchemist — Paulo Coelho
       The Four Agreements — Don Miguel Ruiz

{C2}MANGA{R}
       One Piece — battles and reveals back to back right now
       Boruto: Two Blue Vortex — finally going somewhere
       Vagabond — vol 17, deep in Kojiro's arc
       Goodnight Punpun
       Dr. Stone
       Edens Zero
       Fire Force

{C2}WATCHING{R}
       Bleach: Thousand-Year Blood War — earns the Big 3 title.
       Catholic theology debates.
       Shawn Ryan Show — youtube.com/@ShawnRyanShow
       The Way with Brian Davila — youtube.com/@TheWaywithBrianDavila
       Veronica Explains — youtube.com/@VeronicaExplains
       Switch and Click — youtube.com/@SwitchandClickOfficial
       Caleb Hammer — youtube.com/@CalebHammer

{C2}PLAYING{R}
       Pokemon Champions — Master Ball tier.
       Black Ops 6 — back in rotation, most kills most matches.
       Dead Cells — near-perfect loop. Love this game.

{C2}LATEST(7){R}                     California, USA                     {C2}LATEST(7){R}
"""
)

# ──[ Help ]────────────────────────────────────────────────────────────────────────────
HELP = (
f"""
  {C2}arpatek.dev — available endpoints{R}

  {C1}$ curl arpatek.dev{R}              This page
  {C1}$ curl arpatek.dev/man{R}          Full resume in manpage format
  {C1}$ curl arpatek.dev/env{R}          Hardware & software setup
  {C1}$ curl arpatek.dev/lab{R}          Homelab services (home.arpa)
  {C1}$ curl arpatek.dev/status{R}       What I'm working on
  {C1}$ curl arpatek.dev/latest{R}       Updates, reading, watching, playing
  {C1}$ curl arpatek.dev/changelog{R}    Site and project history
  {C1}$ curl arpatek.dev/help{R}         This list

  {C2}hidden{R}

  {C1}$ curl arpatek.dev/lambda{R}       Trippy circle animation
  {C1}$ curl arpatek.dev/boo{R}          Spooky
  {C1}$ curl arpatek.dev/xmas{R}         Festive
  {C1}$ curl -OJ arpatek.dev/cv{R}       Download resume PDF

"""
)

# ──[ Contact ]─────────────────────────────────────────────────────────────────────────
CONTACT = (
f"""
{C2}CONTACT(7){R}                       arpatek                       {C2}CONTACT(7){R}

{C2}NAME{R}
       {BD}Juan Garcia{R} — Linux technologist & automation engineer

{C2}LOCATION{R}
       California, USA

{C2}CONTACT{R}
       {C1}Email{R}      juang.sh@proton.me

{C2}LINKS{R}
       {C1}Codeberg{R}   codeberg.org/arpatek
       {C1}LinkedIn{R}   linkedin.com/in/arpatek

{C2}RESUME{R}
       {G6}${R} {G2}curl{R} {C1}-OJ arpatek.dev/cv{R}

{C2}CONTACT(7){R}                    California, USA                    {C2}CONTACT(7){R}
"""
)
