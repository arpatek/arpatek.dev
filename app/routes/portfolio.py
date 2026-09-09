"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET /, GET /man, GET /resume for arpatek.dev.

Author: Juan Garcia (arpatek)
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, RedirectResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import PORTFOLIO as ASCII_PORTFOLIO, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP, ENV as ASCII_ENV, LAB as ASCII_LAB, CHANGELOG as ASCII_CHANGELOG, CONTACT as ASCII_CONTACT, STATUS as ASCII_STATUS, LATEST as ASCII_LATEST
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO,  MANPAGE as HTML_MANPAGE, ENV as HTML_ENV, LAB as HTML_LAB, CHANGELOG as HTML_CHANGELOG, CONTACT as HTML_CONTACT, STATUS as HTML_STATUS, LATEST as HTML_LATEST


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


@router.get("/env")
async def env(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_ENV)
    return HTMLResponse(HTML_ENV)


@router.get("/lab")
async def lab(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_LAB)
    return HTMLResponse(HTML_LAB)


@router.get("/changelog")
async def changelog(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_CHANGELOG)
    return HTMLResponse(HTML_CHANGELOG)


@router.get("/status")
async def status(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_STATUS)
    return HTMLResponse(HTML_STATUS)


@router.get("/latest")
async def latest(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_LATEST)
    return HTMLResponse(HTML_LATEST)


# ──[ Legacy Redirects ]────────────────────────────────────────────────────────────────
# /uses and /now are the indieweb conventions and are linked by uses.tech and
# nownownow.com, so the old paths keep working rather than 404ing.
@router.get("/uses")
async def uses_legacy() -> Response:
    return RedirectResponse("/env", status_code=301)


@router.get("/now")
async def now_legacy() -> Response:
    return RedirectResponse("/status", status_code=301)


@router.get("/resume")
async def resume(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_CONTACT)
    return HTMLResponse(HTML_CONTACT)


@router.get("/cv")
async def cv() -> Response:
    return FileResponse(
        "app/static/jgarcia.cv.pdf",
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="jgarcia.cv.pdf"'},
    )
