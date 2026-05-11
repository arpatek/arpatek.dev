"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET /, GET /man for arpatek.dev.

Author: Juan Garcia (arpatek)
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import PORTFOLIO as ASCII_PORTFOLIO, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO,  MANPAGE as HTML_MANPAGE


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()


# ──[ Route Handlers ]──────────────────────────────────────────────────────────────────
@router.get("/")
async def root(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_PORTFOLIO)
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
