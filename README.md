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
| `/env` | Hardware & software setup | Styled page |
| `/lab` | Homelab services (home.arpa) | Styled page |
| `/changelog` | Site and project history | Styled page |
| `/status` | Current and recent technical work | Styled page |
| `/latest` | Updates, reading, watching, playing | Styled page |
| `/resume` | Contact info | Styled contact page |
| `/cv` | — | Downloads resume PDF |
| `/help` | All available endpoints | — |

`/uses` and `/now` 301-redirect to `/env` and `/status` — the indieweb
conventions stay linkable.

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
│   ├── portfolio.py     # /, /man, /env, /lab, /status, /latest, /changelog, /resume, /cv, /help
│   └── animations.py    # /lambda, /boo, /xmas
├── content/
│   ├── ascii.py         # ANSI-colored curl output
│   └── html.py          # Browser templates
└── static/
    ├── favicon.gif
    ├── favicon.ico
    └── jgarcia.cv.pdf
```

## Renaming a route

A route name is duplicated across several files. Changing the handler alone leaves
the rest pointing at a path that no longer exists.

| What | Where |
|------|-------|
| Route handler | `app/routes/portfolio.py` |
| Nav bar — one block per page | `app/content/html.py` |
| Page footer self-reference | `app/content/html.py` |
| Home page legend | `app/content/ascii.py` and `app/content/html.py` |
| `/help` endpoint list | `app/content/ascii.py` |
| Endpoint table and structure tree | `README.md` |

Sweep for stragglers:

```bash
grep -rnE '(arpatek\.dev|href=")/|`/[a-z]+`' app/ README.md --exclude-dir=__pycache__
```

The backtick branch matters — the README endpoint table writes paths as `` `/env` ``
with no `arpatek.dev` prefix and no `href`, so a pattern built only around those two
misses it.

The ASCII and HTML legends read identically but escape differently — `{C2}` against
`${C2}`, the latter inside a JS template literal — so an edit to one does not
transfer verbatim to the other.

Keep the old path as a 301 redirect whenever the name is a convention other sites
link to, as `/uses` and `/now` are.
