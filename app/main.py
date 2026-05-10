#!/usr/bin/env python3
"""
main.py - arpatek.dev Portfolio API
========================================================================================

FastAPI application serving arpatek.dev. Returns an ASCII portfolio for curl clients
and an HTML portfolio for browser clients. The /man route serves a manpage-formatted
resume for man.arpatek.dev (curl) and a styled HTML manpage for arpatek.dev/man.

Author: Juan Garcia (arpatek)

Dependencies:
-------------
- Python 3.11+
- `fastapi`  for the web framework
- `uvicorn`  for the ASGI server

Sample Usage:
-------------
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
$ curl arpatek.dev              # ASCII portfolio
$ curl man.arpatek.dev          # ASCII manpage resume
$ open https://arpatek.dev      # HTML portfolio
$ open https://arpatek.dev/man  # HTML manpage resume
"""

__version__ = "0.1.0"

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.routes.portfolio  import router as portfolio_router
from app.routes.animations import router as animations_router


# ──[ App ]─────────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title       = "arpatek.dev",
    description = "Portfolio — curl arpatek.dev or visit in a browser",
    version     = __version__,
    docs_url    = None,
    redoc_url   = None,
)


# ──[ Static Files ]────────────────────────────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ──[ Routers ]─────────────────────────────────────────────────────────────────────────
app.include_router(portfolio_router)
app.include_router(animations_router)
