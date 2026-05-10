"""
ascii.py - Plain-text content for curl clients
========================================================================================

ASCII portfolio and manpage strings returned when the request comes from curl or
from the man.arpatek.dev hostname. Replace the TODO blocks with actual content.

Author: Juan Garcia (arpatek)
"""

# ──[ Portfolio ]───────────────────────────────────────────────────────────────────────
PORTFOLIO = r"""
  TODO: replace with ASCII art of your name/handle

  Juan Garcia  |  DevOps & Systems Engineer
  -----------------------------------------------
  homelab @ home.arpa   |   arpatek.dev

  SKILLS
  ------
  TODO: list your skills here

  PROJECTS
  --------
  TODO: list your projects here

  LINKS
  -----
  codeberg  https://codeberg.org/arpatek
  gitea     http://prod-git-0.home.arpa:3000

  curl man.arpatek.dev for resume
"""

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = r"""
ARPATEK(1)                    Personal Manual                    ARPATEK(1)

NAME
       arpatek -- Juan Garcia, DevOps & Systems Engineer

SYNOPSIS
       arpatek [--hire] [--contact] [--projects]

DESCRIPTION
       TODO: short bio paragraph

EXPERIENCE
       TODO: work experience entries

              Company Name                             YYYY-MM – YYYY-MM
              Job Title
              * accomplishment
              * accomplishment

SKILLS
       TODO: grouped skill list

              Systems    Linux, RHEL, Debian, Proxmox
              Containers Docker, Kubernetes, k3s
              IaC        Terraform, Ansible, Puppet

CERTIFICATIONS
       TODO: certifications

EDUCATION
       TODO: education

PROJECTS
       TODO: notable projects

SEE ALSO
       arpatek.dev, codeberg.org/arpatek

AUTHOR
       Juan Garcia <juang.dev@proton.me>

                              2026                             ARPATEK(1)
"""
