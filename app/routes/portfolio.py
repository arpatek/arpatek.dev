"""
portfolio.py - Portfolio route handlers
========================================================================================

Serves every content page twice from one route: ANSI text to curl, HTML to browsers.
Pages are registered from a table rather than one decorator each, so adding a page is
a row in PAGES plus the two content blocks.

Author: Juan Garcia (arpatek)
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, RedirectResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import PORTFOLIO as ASCII_PORTFOLIO, MANPAGE as ASCII_MANPAGE, HELP as ASCII_HELP, ENV as ASCII_ENV, LAB as ASCII_LAB, CHANGELOG as ASCII_CHANGELOG, CONTACT as ASCII_CONTACT, STATUS as ASCII_STATUS, LATEST as ASCII_LATEST, PROJECTS as ASCII_PROJECTS
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO,  MANPAGE as HTML_MANPAGE, ENV as HTML_ENV, LAB as HTML_LAB, CHANGELOG as HTML_CHANGELOG, CONTACT as HTML_CONTACT, STATUS as HTML_STATUS, LATEST as HTML_LATEST, PROJECTS as HTML_PROJECTS


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()

# Starlette's own Route adds HEAD whenever GET is registered; FastAPI's APIRoute takes
# the method list verbatim and does not. Without HEAD spelled out here, `curl -I` and
# any uptime monitor that probes with HEAD get a 405 on a page that plainly exists.
METHODS = ["GET", "HEAD"]


# ──[ Dual-rendered Pages ]─────────────────────────────────────────────────────────────
# path -> (curl body, browser body). A new page also needs a nav entry, a legend line,
# and a /help line — see the README's rename checklist for every place a path appears.
PAGES: dict[str, tuple[str, str]] = {
    "/":          (ASCII_PORTFOLIO, HTML_PORTFOLIO),
    "/man":       (ASCII_MANPAGE,   HTML_MANPAGE),
    "/env":       (ASCII_ENV,       HTML_ENV),
    "/lab":       (ASCII_LAB,       HTML_LAB),
    "/projects":  (ASCII_PROJECTS,  HTML_PROJECTS),
    "/status":    (ASCII_STATUS,    HTML_STATUS),
    "/latest":    (ASCII_LATEST,    HTML_LATEST),
    "/changelog": (ASCII_CHANGELOG, HTML_CHANGELOG),
    "/contact":   (ASCII_CONTACT,   HTML_CONTACT),
}


def _register_page(path: str, ascii_body: str, html_body: str) -> None:
    # Each page is registered through its own call, so ascii_body and html_body are
    # bound per handler. Closing over the loop variables directly would leave every
    # handler pointing at the last pair in the table.
    async def handler(request: Request) -> Response:
        ua = request.headers.get("user-agent", "")
        if ua.lower().startswith("curl"):
            return PlainTextResponse(ascii_body)
        return HTMLResponse(html_body)

    handler.__name__ = path.strip("/").replace("-", "_") or "root"
    router.add_api_route(path, handler, methods=METHODS)


for _path, (_ascii, _html) in PAGES.items():
    _register_page(_path, _ascii, _html)


# ──[ Legacy Redirects ]────────────────────────────────────────────────────────────────
# old path -> current path. /uses and /now are the indieweb conventions and are linked
# by uses.tech and nownownow.com; /resume served the contact page for four months before
# the rename. All three were live and linked, so they redirect rather than 404.
REDIRECTS: dict[str, str] = {
    "/uses":   "/env",
    "/now":    "/status",
    "/resume": "/contact",
}


def _register_redirect(path: str, target: str) -> None:
    async def handler() -> Response:
        return RedirectResponse(target, status_code=301)

    handler.__name__ = f"{path.strip('/')}_legacy"
    router.add_api_route(path, handler, methods=METHODS)


for _path, _target in REDIRECTS.items():
    _register_redirect(_path, _target)


# ──[ Single-format Routes ]────────────────────────────────────────────────────────────
# /help is plain text to everyone. It is a list of curl commands, so an HTML rendering
# would only wrap the nav around text that already reads correctly in a terminal.
@router.api_route("/help", methods=METHODS)
async def help(request: Request) -> Response:
    return PlainTextResponse(ASCII_HELP)


@router.api_route("/cv", methods=METHODS)
async def cv() -> Response:
    return FileResponse(
        "app/static/jgarcia.cv.pdf",
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="jgarcia.cv.pdf"'},
    )
