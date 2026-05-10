"""
html.py - HTML content for browser clients
========================================================================================

HTML portfolio and manpage strings returned when the request comes from a browser.
Replace the TODO blocks with actual content and styles.

Author: Juan Garcia (arpatek)
"""

# ──[ Portfolio ]───────────────────────────────────────────────────────────────────────
PORTFOLIO = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>arpatek</title>
  <style>
    /* TODO: add styles */
    body { font-family: monospace; background: #0d0d0d; color: #e0e0e0; max-width: 800px; margin: 0 auto; padding: 2rem; }
  </style>
</head>
<body>
  <h1>TODO: name / handle</h1>
  <p>TODO: tagline</p>

  <h2>Skills</h2>
  <p>TODO</p>

  <h2>Projects</h2>
  <p>TODO</p>

  <h2>Links</h2>
  <ul>
    <li><a href="https://codeberg.org/arpatek">Codeberg</a></li>
  </ul>

  <p><small>curl arpatek.dev for the terminal version &bull; <a href="/man">resume</a></small></p>
</body>
</html>"""

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>arpatek(1)</title>
  <style>
    /* TODO: style to look like a manpage */
    body { font-family: monospace; background: #0d0d0d; color: #e0e0e0; max-width: 900px; margin: 0 auto; padding: 2rem; }
    h1   { font-size: 1rem; }
    h2   { color: #aaa; margin-top: 1.5rem; }
  </style>
</head>
<body>
  <pre>ARPATEK(1)                    Personal Manual                    ARPATEK(1)</pre>

  <h2>NAME</h2>
  <p>arpatek &mdash; Juan Garcia, DevOps &amp; Systems Engineer</p>

  <h2>SYNOPSIS</h2>
  <p><code>arpatek [--hire] [--contact] [--projects]</code></p>

  <h2>DESCRIPTION</h2>
  <p>TODO: bio</p>

  <h2>EXPERIENCE</h2>
  <p>TODO</p>

  <h2>SKILLS</h2>
  <p>TODO</p>

  <h2>SEE ALSO</h2>
  <p><a href="/">arpatek.dev</a>, <a href="https://codeberg.org/arpatek">codeberg.org/arpatek</a></p>

  <pre>                              2026                             ARPATEK(1)</pre>
</body>
</html>"""
