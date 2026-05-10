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
from fastapi import APIRouter
from fastapi.requests  import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

# ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
from app.content.ascii import PORTFOLIO as ASCII_PORTFOLIO, MANPAGE as ASCII_MANPAGE
from app.content.html  import PORTFOLIO as HTML_PORTFOLIO,  MANPAGE as HTML_MANPAGE


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()


# ──[ Route Handlers ]──────────────────────────────────────────────────────────────────
@router.get("/")
async def root(request: Request) -> Response:
    """Serve the portfolio based on User-Agent.

    Args:
        request (Request): Incoming HTTP request.

    Returns:
        Response: PlainTextResponse for curl, HTMLResponse for browsers.
    """
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_PORTFOLIO)
    return HTMLResponse(HTML_PORTFOLIO)


@router.get("/man")
async def manpage(request: Request) -> Response:
    """Serve the resume based on User-Agent.

    Args:
        request (Request): Incoming HTTP request.

    Returns:
        Response: PlainTextResponse for curl, HTMLResponse for browsers.
    """
    ua = request.headers.get("user-agent", "")
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_MANPAGE)
    return HTMLResponse(HTML_MANPAGE)
