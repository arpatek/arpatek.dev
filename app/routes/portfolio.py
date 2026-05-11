"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET / and GET /man for arpatek.dev.

  GET /      curl → ASCII portfolio  | browser → HTML portfolio
  GET /man   curl → ASCII manpage    | browser → HTML manpage

Author: Juan Garcia (arpatek)
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
import asyncio
import json
import random
import time
import urllib.request

from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import get_portfolio, QUOTES, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO, MANPAGE as HTML_MANPAGE


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()


# ──[ Quote Fetcher ]───────────────────────────────────────────────────────────────────
_quote_cache: tuple[str, float] | None = None
_CACHE_TTL = 30  # seconds


def _fetch_from_api() -> str:
    url = "https://zenquotes.io/api/random"
    with urllib.request.urlopen(url, timeout=2) as resp:
        data = json.loads(resp.read())
    q, a = data[0]["q"], data[0]["a"]
    return f'"{q}" — {a}'


async def fetch_quote() -> str:
    global _quote_cache
    if _quote_cache and time.monotonic() - _quote_cache[1] < _CACHE_TTL:
        return _quote_cache[0]
    try:
        quote = await asyncio.wait_for(asyncio.to_thread(_fetch_from_api), timeout=3.0)
        _quote_cache = (quote, time.monotonic())
        return quote
    except Exception:
        return random.choice(QUOTES)


# ──[ Route Handlers ]──────────────────────────────────────────────────────────────────
@router.get("/")
async def root(request: Request) -> Response:
    ua    = request.headers.get("user-agent", "")
    quote = await fetch_quote()
    if ua.lower().startswith("curl"):
        return PlainTextResponse(get_portfolio(quote))
    html = HTML_PORTFOLIO.replace("'__QUOTE__'", json.dumps(quote))
    return HTMLResponse(html)


@router.get("/help")
async def help(request: Request) -> Response:
    return PlainTextResponse(ASCII_HELP)


@router.get("/man")
async def manpage(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_MANPAGE)
    return HTMLResponse(HTML_MANPAGE)
