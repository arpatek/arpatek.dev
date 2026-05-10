"""
animations.py - Streaming ASCII animation route handlers
========================================================================================

Handles GET /gif, /boo, /xmas — streaming ASCII animations for curl clients.
Each route streams ANSI-coded frames until the client disconnects (Ctrl+C).

Author: Juan Garcia (arpatek)

Dependencies:
-------------
- `fastapi` for routing and streaming responses
- `asyncio` for frame timing
- `math`    for trippy circle generation
"""

# ──[ Imports ]─────────────────────────────────────────────────────────────────────────
import asyncio
import math

from fastapi import APIRouter
from fastapi.responses import StreamingResponse


# ──[ Router ]──────────────────────────────────────────────────────────────────────────
router = APIRouter()


# ──[ ANSI Helpers ]────────────────────────────────────────────────────────────────────
CLEAR        = '\033[2J\033[H'
HIDE_CURSOR  = '\033[?25l'
SHOW_CURSOR  = '\033[?25h'
RESET        = '\033[0m'

def _color(code: str, text: str) -> str:
    return f'\033[{code}m{text}{RESET}'

def _rgb(r: int, g: int, b: int, text: str) -> str:
    return f'\033[38;2;{r};{g};{b}m{text}{RESET}'


# ──[ /gif — Trippy rotating circle ]──────────────────────────────────────────────────
_GIF_CHARS  = ' .:-=+*#%@'
_GIF_W      = 60
_GIF_H      = 28

async def _gif_stream():
    yield HIDE_CURSOR
    t = 0.0
    try:
        while True:
            buf = [CLEAR]
            cx, cy = _GIF_W, _GIF_H / 2
            for y in range(_GIF_H):
                line = ''
                for x in range(_GIF_W * 2):
                    dx = (x / 2 - cx) * 0.6
                    dy =  y    - cy
                    r  = math.sqrt(dx * dx + dy * dy)
                    th = math.atan2(dy, dx)
                    v  = math.sin(r * 0.7 - t) + math.cos(th * 4 + t * 0.8)
                    idx = int((v + 2) / 4 * (len(_GIF_CHARS) - 1))
                    idx = max(0, min(len(_GIF_CHARS) - 1, idx))
                    c   = _GIF_CHARS[idx]
                    # colour based on angle + time
                    hue = (th + math.pi) / (2 * math.pi) + t * 0.05
                    ri  = int(127 + 127 * math.sin(hue * 6.28))
                    gi  = int(127 + 127 * math.sin(hue * 6.28 + 2.09))
                    bi  = int(127 + 127 * math.sin(hue * 6.28 + 4.19))
                    line += _rgb(ri, gi, bi, c)
                buf.append(line)
            yield '\n'.join(buf) + '\n'
            await asyncio.sleep(0.07)
            t += 0.22
    finally:
        yield SHOW_CURSOR + CLEAR


@router.get('/gif')
async def gif():
    return StreamingResponse(_gif_stream(), media_type='text/plain')


# ──[ /boo — Ghost ]───────────────────────────────────────────────────────────────────
_TEAL  = '38;5;109'
_GREEN = '38;5;115'
_RED   = '38;5;138'
_DIM   = '2'

_BOO_FRAMES = [
    # frame 0 — quiet
    f"""
{_color(_TEAL, '       .---.')}
{_color(_TEAL, '      /     \\')}
{_color(_TEAL, '     | -   - |')}
{_color(_TEAL, '     |   ^   |')}
{_color(_TEAL, '     |  ___  |')}
{_color(_TEAL, '      \\_____/')}
{_color(_TEAL, '      /|   |\\')}
{_color(_TEAL, '     / |   | \\')}
    """,
    # frame 1 — eyes widen
    f"""
{_color(_TEAL, '       .---.')}
{_color(_TEAL, '      /     \\')}
{_color(_TEAL, '     | o   o |')}
{_color(_TEAL, '     |   ^   |')}
{_color(_TEAL, '     |  ___  |')}
{_color(_TEAL, '      \\_____/')}
{_color(_TEAL, '      /|   |\\')}
{_color(_TEAL, '     / |   | \\')}
    """,
    # frame 2 — BOO!
    f"""
{_color(_TEAL, '       .---.')}
{_color(_TEAL, '      /     \\')}
{_color(_TEAL, '     | O   O |')}
{_color(_TEAL, '     |  ___  |')}
{_color(_TEAL, '     | |   | |')}
{_color(_TEAL, '      \\_____/')}
{_color(_TEAL, '      /|   |\\')}
{_color(_TEAL, '     / |   | \\')}

{_color(_RED,   '         BOO!')}
    """,
    # frame 3 — back to quiet
    f"""
{_color(_TEAL, '       .---.')}
{_color(_TEAL, '      /     \\')}
{_color(_TEAL, '     | -   - |')}
{_color(_TEAL, '     |   v   |')}
{_color(_TEAL, '     |  ___  |')}
{_color(_TEAL, '      \\_____/')}
{_color(_TEAL, '      /|   |\\')}
{_color(_TEAL, '     / |   | \\')}
    """,
]

_BOO_DELAYS = [1.2, 0.4, 1.5, 0.8]

async def _boo_stream():
    yield HIDE_CURSOR
    try:
        while True:
            for frame, delay in zip(_BOO_FRAMES, _BOO_DELAYS):
                yield CLEAR + frame
                await asyncio.sleep(delay)
    finally:
        yield SHOW_CURSOR + CLEAR


@router.get('/boo')
async def boo():
    return StreamingResponse(_boo_stream(), media_type='text/plain')


# ──[ /xmas — Christmas tree ]─────────────────────────────────────────────────────────
_STAR   = '38;5;221'  # yellow
_TREE   = '38;5;115'  # sage green
_TRUNK  = '38;5;138'  # muted brown
_L1     = '38;5;204'  # pink/red light
_L2     = '38;5;109'  # teal light
_L3     = '38;5;221'  # yellow light

def _xmas_frame(tick: int) -> str:
    lights = [_L1, _L2, _L3]
    def L(i: int) -> str:
        return _color(lights[(i + tick) % 3], '*')

    return f"""
{_color(_STAR,  '          ★')}
{_color(_TREE,  '          /\\')}
{_color(_TREE,  '         /  \\')}
{_color(_TREE,  '        / ') + L(0) + _color(_TREE, '  \\')}
{_color(_TREE,  '       /      \\')}
{_color(_TREE,  '      / ') + L(1) + _color(_TREE, '  ') + L(2) + _color(_TREE, '  \\')}
{_color(_TREE,  '     /          \\')}
{_color(_TREE,  '    / ') + L(2) + _color(_TREE, '    ') + L(0) + _color(_TREE, '   \\')}
{_color(_TREE,  '   /              \\')}
{_color(_TREE,  '  / ') + L(1) + _color(_TREE, '  ') + L(2) + _color(_TREE, '   ') + L(0) + _color(_TREE, '  \\')}
{_color(_TREE,  ' /                  \\')}
{_color(_TREE,  '/____________________\\')}
{_color(_TRUNK, '         ||||')}
{_color(_TRUNK, '         ||||')}
{_color(_TRUNK, '       [______]')}

{_color(_STAR,  '     Happy Holidays! 🎄')}
    """

async def _xmas_stream():
    yield HIDE_CURSOR
    tick = 0
    try:
        while True:
            yield CLEAR + _xmas_frame(tick)
            await asyncio.sleep(0.6)
            tick += 1
    finally:
        yield SHOW_CURSOR + CLEAR


@router.get('/xmas')
async def xmas():
    return StreamingResponse(_xmas_stream(), media_type='text/plain')
