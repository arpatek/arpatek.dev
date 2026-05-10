"""
ascii.py - Plain-text content for curl clients
========================================================================================

ASCII portfolio and manpage strings returned when the request comes from curl or
from the man.arpatek.dev hostname.

Author: Juan Garcia (arpatek)
"""

# ──[ Portfolio ]───────────────────────────────────────────────────────────────────────
PORTFOLIO = r"""
ARPATEK(1)                      User Commands                      ARPATEK(1)

NAME
       arpatek - Juan Garcia, Linux technologist & automation engineer

SYNOPSIS
       juan [--automate] [--build] [--break-then-fix]

DESCRIPTION
       Self-taught technologist based in California with a strong passion
       for automation, system reliability, and open-source technologies.

       3 years of hardware and UNIX lab work as a Senior Test Technician
       at TrueNAS. Now designing and operating a self-hosted homelab
       using Infrastructure as Code — provisioning, hardening, and
       observing every layer.

       RHCSA in progress. Fluent in English and Spanish.

SKILLS
       Languages       Bash, Python, HCL

       Systems         Linux (Ubuntu, RHEL, Debian, Rocky, TrueNAS),
                       UNIX, TCP/IP, VLAN, LAGG, RAID, PXE Boot

       IaC             Terraform, Ansible, Puppet

       Observability   Prometheus, Loki, Grafana, Alloy, node_exporter

       Services        FreeIPA, Gitea, WireGuard, Pi-hole, Docker, k3s

       Tools           Git, Vim, tmux, SSH, Nginx

PROJECTS
       home.arpa        Self-hosted homelab — IaC, monitoring, identity,
                        DNS, VPN, and container orchestration
       terraform-xo     XCP-ng VM provisioning via Terraform + XO API
       ansible-baseline Post-provisioning automation for Debian VMs
       puppet-modules   Puppet module collection for homelab VM hardening
       snaputil         Modular system snapshot tool
       citadel          Pattern-based password generator
       portal-22        SSH key & config generator from YAML

SEE ALSO
       codeberg.org/arpatek(1), linkedin.com/in/arpatek(1)

NOTES
       if [ "$task" = "manual" ]; then automate; fi

       curl man.arpatek.dev for resume

ARPATEK(1)                    California, USA                    ARPATEK(1)
"""

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = r"""
ARPATEK(1)                    Personal Manual                    ARPATEK(1)

NAME
       arpatek -- Juan Garcia, Linux technologist & automation engineer

SYNOPSIS
       juan [--automate] [--build] [--break-then-fix]

DESCRIPTION
       Systems automation engineer with production experience building
       hardware validation tooling at scale. Strong background in Linux,
       Bash, Python, and infrastructure-as-code. Hands-on with Ansible,
       Terraform, Kubernetes, and self-hosted infrastructure monitoring
       stacks. Pursuing RHCSA cert; roadmap includes RHCE, Terraform
       Associate, CKA, CKS, and AWS.

       Location: California, USA
       Email:    juang.sh@proton.me

EXPERIENCE
       Senior Test Technician
       TrueNAS | 2021 – 2024

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

       Computer Hardware Technician
       EMR CPR/Corovan | 2021

              * Reconfigured and relocated desktop/server systems
                post-migration
              * Troubleshot hardware/software issues and blueprinted
                workstation layouts

       Post Production Specialist
       Freelance | 2016 – 2021

              * Managed AV setup, live audio/video services, and video
                editing
              * Designed and executed digital marketing strategies for SMBs

       Passenger Service Supervisor
       Pacific Aviation | 2019 – 2021

              * Coordinated airline operations and communicated between
                international teams

SKILLS
       Languages       Bash, Python, HCL

       Systems         Linux (RHEL, Ubuntu, TrueNAS/FreeBSD), UNIX,
                       TCP/IP, VLANs, LAGG, RAID, PXE Boot,
                       ZFS, SAS/HBA, BIOS Firmware, IPMI, Redfish API

       IaC             Terraform, Ansible, Puppet

       Containers      Docker, Kubernetes (k3s)

       Observability   Prometheus, Grafana, Loki, Alloy, node_exporter

       Services        FreeIPA, Gitea, WireGuard, Pi-hole

       Tools           Git, Vim, tmux, SSH

PROJECTS
       home.arpa        Self-hosted homelab — IaC, monitoring, identity,
                        DNS, VPN, and container orchestration
       terraform-xo     XCP-ng VM provisioning via Terraform + XO API
       ansible-baseline Post-provisioning automation for Debian VMs
       puppet-modules   Puppet module collection for homelab VM hardening
       snaputil         Modular system snapshot tool
       citadel          Pattern-based password generator
       portal-22        SSH key & config generator from YAML

EDUCATION
       Red Hat Certified System Administrator          In Progress
       Google IT Automation with Python Professional   Completed
       Google IT Support Professional Certificate      Completed
       IT Support & Services / Advanced IT             JobTrain & StreetCode Academy

LANGUAGES
       English   Fluent
       Spanish   Fluent

SEE ALSO
       arpatek.dev(1), codeberg.org/arpatek(1), linkedin.com/in/arpatek(1)

NOTES
       if [ "$task" = "manual" ]; then automate; fi
       01001010 01000111

ARPATEK(1)                    California, USA                    ARPATEK(1)
"""
