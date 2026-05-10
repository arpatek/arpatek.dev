"""
portfolio.py - Portfolio route handlers
========================================================================================

Handles GET / and GET /man for arpatek.dev.

  GET /      arpatek.dev      → curl: ASCII portfolio  | browser: HTML portfolio
             man.arpatek.dev  → plain-text manpage (always)
  GET /man   arpatek.dev/man  → HTML manpage (always)

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
    """Serve the portfolio or manpage depending on hostname and User-Agent.

    - Requests to man.arpatek.dev always return the plain-text manpage.
    - Requests from curl return the ASCII portfolio.
    - All other requests return the HTML portfolio.

    Args:
        request (Request): Incoming HTTP request.

    Returns:
        Response: PlainTextResponse or HTMLResponse.
    """
    host = request.headers.get("host", "")
    ua   = request.headers.get("user-agent", "")

    if host.startswith("man."):
        return PlainTextResponse(ASCII_MANPAGE)
    if ua.lower().startswith("curl"):
        return PlainTextResponse(ASCII_PORTFOLIO)
    return HTMLResponse(HTML_PORTFOLIO)


@router.get("/man")
async def manpage(request: Request) -> Response:
    """Serve the HTML manpage resume for browser clients at arpatek.dev/man.

    Args:
        request (Request): Incoming HTTP request.

    Returns:
        HTMLResponse: Rendered HTML manpage.
    """
    return HTMLResponse(HTML_MANPAGE)
