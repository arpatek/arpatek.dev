"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET /, GET /man, GET /resume for arpatek.dev.

Author: Juan Garcia (arpatek)
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import PORTFOLIO as ASCII_PORTFOLIO, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP, USES as ASCII_USES, LAB as ASCII_LAB, CHANGELOG as ASCII_CHANGELOG
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO,  MANPAGE as HTML_MANPAGE, USES as HTML_USES, LAB as HTML_LAB, CHANGELOG as HTML_CHANGELOG


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


@router.get("/uses")
async def uses(request: Request) -> Response:
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_USES)
    return HTMLResponse(HTML_USES)


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


@router.get("/resume")
async def resume() -> Response:
    return FileResponse(
        "app/static/jgarcia.cv.pdf",
        media_type="application/pdf",
        headers={"Content-Disposition": 'inline; filename="jgarcia.cv.pdf"'},
    )
