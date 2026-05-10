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
CLEAR       = '\033[2J\033[H'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
RESET       = '\033[0m'

def _c(code: str, text: str) -> str:
    return '\033[' + code + 'm' + text + RESET

def _rgb(r: int, g: int, b: int, text: str) -> str:
    return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm' + text + RESET


# ──[ /gif — Trippy rotating circle ]──────────────────────────────────────────────────
_GIF_CHARS = ' .:-=+*#%@'
_GIF_W     = 60
_GIF_H     = 28

async def _gif_stream():
    yield HIDE_CURSOR
    t = 0.0
    try:
        while True:
            rows = [CLEAR]
            cx, cy = _GIF_W, _GIF_H / 2
            for y in range(_GIF_H):
                line = ''
                for x in range(_GIF_W * 2):
                    dx = (x / 2 - cx) * 0.6
                    dy = y - cy
                    r  = math.sqrt(dx * dx + dy * dy)
                    th = math.atan2(dy, dx)
                    v  = math.sin(r * 0.7 - t) + math.cos(th * 4 + t * 0.8)
                    idx = int((v + 2) / 4 * (len(_GIF_CHARS) - 1))
                    idx = max(0, min(len(_GIF_CHARS) - 1, idx))
                    ch  = _GIF_CHARS[idx]
                    hue = (th + math.pi) / (2 * math.pi) + t * 0.05
                    ri  = int(127 + 127 * math.sin(hue * 6.28))
                    gi  = int(127 + 127 * math.sin(hue * 6.28 + 2.09))
                    bi  = int(127 + 127 * math.sin(hue * 6.28 + 4.19))
                    line += _rgb(ri, gi, bi, ch)
                rows.append(line)
            yield '\n'.join(rows) + '\n'
            await asyncio.sleep(0.07)
            t += 0.22
    finally:
        yield SHOW_CURSOR + CLEAR


@router.get('/gif')
async def gif():
    return StreamingResponse(_gif_stream(), media_type='text/plain')


# ──[ /boo — Ghost ]───────────────────────────────────────────────────────────────────
_TEAL = '38;5;109'
_RED  = '38;5;138'

def _ghost(eyes: str, mouth: list, extra: str = '') -> str:
    bs = '\\'
    lines = [
        '',
        _c(_TEAL, '       .---.'),
        _c(_TEAL, '      /     ' + bs),
        _c(_TEAL, '     | ' + eyes + ' |'),
    ] + [_c(_TEAL, '     ' + m) for m in mouth] + [
        _c(_TEAL, '      ' + bs + '_____/'),
        _c(_TEAL, '      /|   |' + bs),
        _c(_TEAL, '     / |   | ' + bs),
        extra,
        '',
    ]
    return '\n'.join(lines)

_BOO_FRAMES = [
    (_ghost('- . -', ['|   ^   |', '|  ___  |']),            1.2),
    (_ghost('o . o', ['|   ^   |', '|  ___  |']),            0.4),
    (_ghost('O . O', ['|  ___  |', '| |   | |'], _c(_RED, '      BOO!')), 1.5),
    (_ghost('- . -', ['|   v   |', '|  ___  |']),            0.8),
]

async def _boo_stream():
    yield HIDE_CURSOR
    try:
        while True:
            for frame, delay in _BOO_FRAMES:
                yield CLEAR + frame
                await asyncio.sleep(delay)
    finally:
        yield SHOW_CURSOR + CLEAR


@router.get('/boo')
async def boo():
    return StreamingResponse(_boo_stream(), media_type='text/plain')


# ──[ /xmas — Christmas tree ]─────────────────────────────────────────────────────────
_STAR  = '38;5;221'
_GREEN = '38;5;115'
_TRUNK = '38;5;138'
_LIGHTS = ['38;5;204', '38;5;109', '38;5;221']

def _xmas_frame(tick: int) -> str:
    def L(i: int) -> str:
        return _c(_LIGHTS[(i + tick) % 3], '*')

    sl = '\\'
    rows = [
        '',
        '          ' + _c(_STAR,  'star'),
        '          ' + _c(_GREEN, '/') + _c(_STAR, '*') + _c(_GREEN, sl),
        '         ' + _c(_GREEN, '/   ' + sl),
        '        ' + _c(_GREEN, '/ ') + L(0) + _c(_GREEN, '  ' + sl),
        '       ' + _c(_GREEN, '/      ' + sl),
        '      ' + _c(_GREEN, '/ ') + L(1) + _c(_GREEN, '  ') + L(2) + _c(_GREEN, '  ' + sl),
        '     ' + _c(_GREEN, '/          ' + sl),
        '    ' + _c(_GREEN, '/ ') + L(2) + _c(_GREEN, '    ') + L(0) + _c(_GREEN, '   ' + sl),
        '   ' + _c(_GREEN, '/              ' + sl),
        '  ' + _c(_GREEN, '/ ') + L(1) + _c(_GREEN, '  ') + L(2) + _c(_GREEN, '   ') + L(0) + _c(_GREEN, '  ' + sl),
        ' ' + _c(_GREEN, '/____________________' + sl),
        '         ' + _c(_TRUNK, '||||'),
        '         ' + _c(_TRUNK, '||||'),
        '       ' + _c(_TRUNK, '[______]'),
        '',
        '     ' + _c(_STAR, 'Happy Holidays!'),
        '',
    ]
    return '\n'.join(rows)

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
