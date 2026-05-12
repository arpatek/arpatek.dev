# arpatek.dev

Personal portfolio site that serves ASCII art to `curl` clients and a terminal-emulator HTML page to browsers.

```
curl arpatek.dev
```

## Endpoints

| Endpoint | curl | browser |
|----------|------|---------|
| `/` | ASCII portfolio with banner | Terminal emulator with typing animation |
| `/man` | Manpage-formatted resume | Styled HTML manpage |
| `/uses` | Hardware & software setup | Styled page |
| `/lab` | Homelab services (home.arpa) | Styled page |
| `/changelog` | Site and project history | Styled page |
| `/now` | What I'm up to | Styled page |
| `/resume` | Contact info | Styled contact page |
| `/cv` | — | Downloads resume PDF |
| `/help` | All available endpoints | — |

### Hidden

```bash
curl arpatek.dev/lambda   # Trippy rotating circle animation
curl arpatek.dev/boo      # Morphing ASCII animation
curl arpatek.dev/xmas     # Christmas tree with cycling lights
```

## Stack

- **Python 3.11** + **FastAPI** + **uvicorn**
- Containerized via **Docker**, deployed on **k3s**
- CI/CD via **Gitea Actions** — builds image, pushes to private registry, rolls out deployment
- **Traefik** ingress + **cert-manager** (Let's Encrypt, Cloudflare DNS-01)

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Structure

```
app/
├── main.py
├── routes/
│   ├── portfolio.py     # /, /man, /uses, /lab, /changelog, /now, /resume, /cv, /help
│   └── animations.py    # /lambda, /boo, /xmas
├── content/
│   ├── ascii.py         # ANSI-colored curl output
│   └── html.py          # Browser templates
└── static/
    ├── favicon.gif
    ├── favicon.ico
    └── jgarcia.cv.pdf
```
