"""
html.py - HTML content for browser clients
========================================================================================

HTML portfolio and manpage returned when the request comes from a browser.
The portfolio page uses a terminal emulator effect (inspired by ysap.sh) that
types out commands and output to simulate a live shell session.

Author: Juan Garcia (arpatek)
"""

# ──[ Shared Theme ]────────────────────────────────────────────────────────────────────
_STYLES = """
* { margin: 0; padding: 0; box-sizing: border-box; }
ul { list-style-type: none; }

:root {
    --c1: #5fffff;   /* cyan  - links          */
    --c2: #ff87af;   /* pink  - accents        */
    --c3: #87ff87;   /* green - highlights     */
    --c4: #666;      /* dim                   */
    --c5: #ffd7af;   /* cream - body text      */
}

body {
    background: #000;
    color: var(--c5);
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 13px;
}

#container {
    max-width: 800px;
    margin: 10px auto;
    padding: 0 8px;
}

a, a:visited { color: var(--c1); text-decoration: none; }
a:hover { text-decoration: underline; }

h1 { color: var(--c3); margin-bottom: 20px; }
h2 { color: var(--c4); font-size: 0.85rem; text-transform: uppercase;
     letter-spacing: 0.08em; margin: 1.4rem 0 0.4rem; }

/* nav */
#nav { border-bottom: 1px solid #87ff8740; margin-bottom: 20px; overflow: hidden; }
#nav a { display: block; float: left; padding: 12px 14px; color: var(--c5); }
#nav a:hover { background: #1a1a1a; text-decoration: none; }
#nav a.active { color: var(--c3); }
#nav a.right { float: right; }

/* terminal block */
pre.terminal {
    background: #0a0a0a;
    border: 1px solid #87ff8730;
    box-shadow: 0 0 160px #87ff8718;
    padding: 8px;
    min-height: 380px;
    overflow-x: auto;
    line-height: 16px;
    margin: 16px 0;
}
pre.terminal > code { font-size: 13px; }

/* blinking cursor */
pre.terminal > code::after {
    content: "";
    width: 6px;
    height: 12px;
    background: var(--c5);
    display: inline-block;
    animation: blink 1.5s step-start infinite;
}
.no-cursor::after { animation: none !important; }
@keyframes blink { 50% { opacity: 0; } }

/* footer */
.footer { text-align: center; font-size: 11px; color: var(--c4);
          margin-top: 16px; padding-bottom: 16px; }
.footer a { color: var(--c4); }

/* manpage styles */
.man-header { display: flex; justify-content: space-between;
              color: var(--c4); margin-bottom: 20px; }
.man-footer { display: flex; justify-content: space-between;
              color: var(--c4); margin-top: 24px; }
.section { margin-bottom: 12px; }
.section p, .section li { padding-left: 7ch; color: var(--c5); }
.section ul { padding-left: 7ch; }
.section li::before { content: "* "; color: var(--c4); }
.label { color: var(--c1); display: inline-block; min-width: 20ch; }
.entry { margin-bottom: 12px; padding-left: 7ch; }
.entry-title { color: var(--c5); }
.entry-org  { color: var(--c1); font-size: 0.9rem; }
"""

# ──[ Terminal commands shown in the browser ]───────────────────────────────────────────
_COMMANDS_JS = r"""
const G0 = '<span style="color:#5fffff">';
const G1 = '<span style="color:#00ffd7">';
const G2 = '<span style="color:#00ffaf">';
const G3 = '<span style="color:#00ff87">';
const G4 = '<span style="color:#00ff5f">';
const G5 = '<span style="color:#00ff00">';
const G6 = '<span style="color:#87ff87">';
const C1 = '<span style="color:#5fffff">';
const C2 = '<span style="color:#87ff87">';
const DM = '<span style="opacity:0.45">';
const BD = '<span style="font-weight:700">';
const R  = '</span>';

const COMMANDS = [
    {
        cmd: 'curl arpatek.dev',
        lines: `

${G0}         :::     :::::::::  :::::::::     ::: ::::::::::: :::::::::: :::    :::${R}
${G1}       :+: :+:   :+:    :+: :+:    :+:  :+: :+:   :+:     :+:        :+:   :+:${R}
${G2}     +:+   +:+  +:+    +:+ +:+    +:+ +:+   +:+  +:+     +:+        +:+  +:+${R}
${G3}   +#++:++#++: +#++:++#:  +#++:++#+ +#++:++#++: +#+     +#++:++#   +#++:++${R}
${G4}  +#+     +#+ +#+    +#+ +#+       +#+     +#+ +#+     +#+        +#+  +#+${R}
${G5} #+#     #+# #+#    #+# #+#       #+#     #+# #+#     #+#        #+#   #+#${R}
${G6}###     ### ###    ### ###       ###     ### ###     ########## ###    ###${R}

  ${BD}Juan Garcia${R} — Linux technologist &amp; automation engineer
  ${C1}https://arpatek.dev${R} | ${C1}https://codeberg.org/arpatek${R}


${C2}┌─About───────────────────────────┐${R} ${C2}┌─Links────┬────────────────────────────────┐${R}
${C2}│${R}                                 ${C2}│${R} ${C2}│${R}          ${C2}│${R}                                ${C2}│${R}
${C2}│${R}  Systems automation engineer    ${C2}│${R} ${C2}│${R} Codeberg ${C2}│${R} ${C1}codeberg.org/arpatek${R}           ${C2}│${R}
${C2}│${R}  based in California. 3 years   ${C2}│${R} ${C2}│${R} LinkedIn ${C2}│${R} ${C1}linkedin.com/in/arpatek${R}        ${C2}│${R}
${C2}│${R}  of hardware &amp; UNIX lab work at ${C2}│${R} ${C2}│${R}          ${C2}│${R}                                ${C2}│${R}
${C2}│${R}  TrueNAS. Now building a        ${C2}│${R} ${C2}└──────────┴────────────────────────────────┘${R}
${C2}│${R}  self-hosted homelab using IaC. ${C2}│${R}
${C2}│${R}  RHCSA in progress.             ${C2}│${R}
${C2}│${R}                                 ${C2}│${R}
${C2}└─────────────────────────────────┘${R}

  ${C2}Legend${R}

  ${C1}$ curl arpatek.dev${R}        Get this page
  ${C1}$ curl arpatek.dev/man${R}    Full resume in manpage format

`.split('\n')
    },
];


"""

# ──[ Terminal JS logic ]───────────────────────────────────────────────────────────────
_TERMINAL_JS = r"""
const SPEED = 90;
const INIT_DELAY = 1800;
const LOOP_DELAY = 6000;

const term = document.getElementById('term').children[0];

const BLINK_ON  = 1;
const BLINK_OFF = 2;

function setCursor(on) {
    if (on) term.classList.remove('no-cursor');
    else    term.classList.add('no-cursor');
}

function runCommand(idx, done) {
    const { cmd, lines } = COMMANDS[idx];
    const chars = [BLINK_OFF, ...cmd.split(''), '\n', ...lines.map(l => l + '\n'), '$ ', BLINK_ON];

    setCursor(true);
    term.innerHTML = '$ ';

    let i = 0;
    function tick() {
        if (i === chars.length) { done(); return; }
        const c = chars[i++];
        if      (c === BLINK_ON)  setCursor(true);
        else if (c === BLINK_OFF) setCursor(false);
        else                      term.innerHTML += c;
        setTimeout(tick, SPEED);
    }
    tick();
}

setTimeout(function () {
    const cb = COMMANDS.length === 1 ? () => {} : function() {
        setTimeout(() => {
            let i = 1 % COMMANDS.length;
            (function loop(i) {
                setTimeout(() => { runCommand(i, () => loop((i + 1) % COMMANDS.length)); }, LOOP_DELAY);
            })(i);
        }, LOOP_DELAY);
    };
    runCommand(0, cb);
}, INIT_DELAY);
"""

# ──[ Portfolio ]───────────────────────────────────────────────────────────────────────
PORTFOLIO = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>arpatek</title>
  <link rel="icon" href="/static/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}
img.profile {{
  float: right;
  width: 96px;
  height: 96px;
  margin: 0 0 12px 16px;
  image-rendering: pixelated;
}}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/" class="active">~</a>
      <a href="/man">man arpatek(1)</a>
      <a href="https://codeberg.org/arpatek" class="right">codeberg</a>
    </div>

    <img src="/static/profile.png" class="profile" alt="arpatek">
    <h1>&gt; arpatek.dev</h1>

    <pre class="terminal" id="term"><code></code></pre>

    <div class="footer">
      <code>
        <a href="https://codeberg.org/arpatek">codeberg.org/arpatek</a> &nbsp;|&nbsp;
        <a href="https://linkedin.com/in/arpatek">linkedin.com/in/arpatek</a>
      </code>
    </div>
  </div>
  <script>{_COMMANDS_JS}</script>
  <script>{_TERMINAL_JS}</script>
</body>
</html>"""

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>arpatek(1)</title>
  <link rel="icon" href="/static/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">~</a>
      <a href="/man" class="active">man arpatek</a>
      <a href="https://codeberg.org/arpatek" class="right">codeberg</a>
    </div>

    <div class="man-header">
      <span>ARPATEK(1)</span><span>Personal Manual</span><span>ARPATEK(1)</span>
    </div>

    <div class="section">
      <h2>Name</h2>
      <p>arpatek &mdash; Juan Garcia, Linux technologist &amp; automation engineer</p>
    </div>

    <div class="section">
      <h2>Description</h2>
      <p>Systems automation engineer with production experience building hardware validation
      tooling at scale. Strong background in Linux, Bash, Python, and infrastructure-as-code.
      Pursuing RHCSA; roadmap includes RHCE, Terraform Associate, CKA, CKS, and AWS.</p>
      <br>
      <p><span class="label">Email</span> <a href="mailto:juang.sh@proton.me">juang.sh@proton.me</a></p>
      <p><span class="label">Location</span> California, USA</p>
    </div>

    <div class="section">
      <h2>Experience</h2>

      <div class="entry">
        <div class="entry-title">Senior Test Technician</div>
        <div class="entry-org">TrueNAS &nbsp;&bull;&nbsp; 2021 &ndash; 2024</div>
        <ul>
          <li>Built a 22,000+ line Bash/Python automation suite (CC &amp; SWQC) for manufacturing QC</li>
          <li>Automated BIOS, firmware, and HW validation via IPMI and Redfish API for 16+ systems</li>
          <li>Developed Python Redfish API clients for BIOS push/export on liquid immersion platforms</li>
          <li>Integrated with PBS archive servers and PostgreSQL for burn-in parsing and reporting</li>
          <li>Validated firmware compliance against Redbook specs: ZFS, HBA firmware, SMART health</li>
          <li>Automated multi-node HA pair diffing and generated diff sheets for QC traceability</li>
        </ul>
      </div>

      <div class="entry">
        <div class="entry-title">Computer Hardware Technician</div>
        <div class="entry-org">EMR CPR/Corovan &nbsp;&bull;&nbsp; 2021</div>
        <ul>
          <li>Reconfigured and relocated desktop/server systems post-migration</li>
          <li>Troubleshot hardware/software issues and blueprinted workstation layouts</li>
        </ul>
      </div>

      <div class="entry">
        <div class="entry-title">Post Production Specialist</div>
        <div class="entry-org">Freelance &nbsp;&bull;&nbsp; 2016 &ndash; 2021</div>
        <ul>
          <li>Managed AV setup, live audio/video services, and video editing</li>
          <li>Designed and executed digital marketing strategies for SMBs</li>
        </ul>
      </div>

      <div class="entry">
        <div class="entry-title">Passenger Service Supervisor</div>
        <div class="entry-org">Pacific Aviation &nbsp;&bull;&nbsp; 2019 &ndash; 2021</div>
        <ul>
          <li>Coordinated airline operations and communicated between international teams</li>
        </ul>
      </div>
    </div>

    <div class="section">
      <h2>Skills</h2>
      <p><span class="label">Languages</span> Bash, Python, HCL</p>
      <p><span class="label">Systems</span> RHEL, Ubuntu, Debian, TrueNAS, TCP/IP, VLANs, ZFS, IPMI, Redfish</p>
      <p><span class="label">IaC</span> Terraform, Ansible, Puppet</p>
      <p><span class="label">Containers</span> Docker, Kubernetes (k3s)</p>
      <p><span class="label">Observability</span> Prometheus, Grafana, Loki, Alloy, node_exporter</p>
      <p><span class="label">Tools</span> Git, Vim, tmux, SSH</p>
    </div>

    <div class="section">
      <h2>Projects</h2>
      <p><span class="label">home.arpa</span> Self-hosted homelab &mdash; IaC, monitoring, identity, DNS, VPN, k3s</p>
      <p><span class="label">terraform-xo</span> XCP-ng VM provisioning via Terraform + XO API</p>
      <p><span class="label">ansible-baseline</span> Post-provisioning automation for Debian VMs</p>
      <p><span class="label">puppet-modules</span> Puppet module collection for homelab VM hardening</p>
      <p><span class="label">snaputil</span> Modular system snapshot tool</p>
      <p><span class="label">citadel</span> Pattern-based password generator</p>
      <p><span class="label">portal-22</span> SSH key &amp; config generator from YAML</p>
    </div>

    <div class="section">
      <h2>Education</h2>
      <p><span class="label">RHCSA</span> In Progress</p>
      <p><span class="label">Google IT Automation</span> Completed</p>
      <p><span class="label">Google IT Support</span> Completed</p>
      <p><span class="label">IT Support &amp; Advanced IT</span> JobTrain &amp; StreetCode Academy</p>
    </div>

    <div class="section">
      <h2>Languages</h2>
      <p><span class="label">English</span> Fluent</p>
      <p><span class="label">Spanish</span> Fluent</p>
    </div>

    <div class="section">
      <h2>See Also</h2>
      <p>
        <a href="/">arpatek.dev</a> &nbsp;&bull;&nbsp;
        <a href="https://codeberg.org/arpatek">codeberg.org/arpatek</a> &nbsp;&bull;&nbsp;
        <a href="https://linkedin.com/in/arpatek">linkedin.com/in/arpatek</a>
      </p>
    </div>

    <div class="man-footer">
      <span>ARPATEK(1)</span><span>California, USA</span><span>ARPATEK(1)</span>
    </div>
  </div>
</body>
</html>"""
