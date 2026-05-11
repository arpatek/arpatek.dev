"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET / and GET /man for arpatek.dev.

  GET /      curl → ASCII portfolio  | browser → HTML portfolio
  GET /man   curl → ASCII manpage    | browser → HTML manpage

Author: Juan Garcia (arpatek)

Dependencies:
-------------
- `fastapi` for routing and request/response types
- `app.content.ascii` for plain-text content
- `app.content.html`  for HTML content
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
import random

from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import get_portfolio, QUOTES, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO, MANPAGE as HTML_MANPAGE


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()


# ──[ Route Handlers ]──────────────────────────────────────────────────────────────────
@router.get("/")
async def root(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(get_portfolio(random.choice(QUOTES)))
    return HTMLResponse(HTML_PORTFOLIO)


@router.get("/help")
async def help(request: Request) -> Response:
    return PlainTextResponse(ASCII_HELP)


@router.get("/man")
async def manpage(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_MANPAGE)
    return HTMLResponse(HTML_MANPAGE)
