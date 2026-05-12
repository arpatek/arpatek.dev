"""
html.py - HTML content for browser clients
========================================================================================

HTML portfolio and manpage returned when the request comes from a browser.
The portfolio page uses a terminal emulator effect (inspired by ysap.sh) that
types out commands and output to simulate a live shell session.

Author: Juan Garcia (arpatek)
"""

# ──[ Favicon JS ]──────────────────────────────────────────────────────────────────────
_FAVICON_JS = """
(function() {
    var link = document.querySelector("link[rel='icon']");
    var interval = null;
    function startAnim() {
        if (interval) return;
        link.href = '/static/favicon.gif?t=' + Date.now();
        interval = setInterval(function() {
            link.href = '/static/favicon.gif?t=' + Date.now();
        }, 520);
    }
    function stopAnim() {
        clearInterval(interval);
        interval = null;
        link.href = '/static/favicon.ico';
    }
    document.addEventListener('visibilitychange', function() {
        document.hidden ? stopAnim() : startAnim();
    });
    startAnim();
})();
"""

# ──[ Shared Theme ]────────────────────────────────────────────────────────────────────
_STYLES = """
* { margin: 0; padding: 0; box-sizing: border-box; }
ul { list-style-type: none; }

:root {
    --c1: #9db9b2;   /* teal    - links       */
    --c2: #79be9a;   /* green   - accents     */
    --c3: #b9746f;   /* red     - highlights  */
    --c4: #877887;   /* dim purple            */
    --c5: #dcd6d6;   /* light   - body text   */
}

body {
    background: #1c1a16;
    color: var(--c5);
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 13px;
}

#container {
    max-width: 765px;
    margin: 10px auto;
    padding: 0 8px;
    min-height: calc(100vh - 20px);
}

a, a:visited { color: var(--c1); text-decoration: none; }
a:hover { text-decoration: underline; }

h1 { color: var(--c2); margin-bottom: 20px; }
h2 { color: var(--c4); font-size: 0.85rem; text-transform: uppercase;
     letter-spacing: 0.08em; margin: 1.4rem 0 0.4rem; }

/* nav */
#nav { border-bottom: 1px solid #9db9b244; margin-bottom: 20px; overflow: hidden; }
#nav a { display: block; float: left; padding: 12px 14px; color: var(--c5); }
#nav a:hover { background: #332e33; text-decoration: none; }
#nav a.active { color: var(--c1); }
#nav a.right { float: right; }

/* terminal block */
pre.terminal {
    background: #1c1a16;
    border: 1px solid #79be9a33;
    padding: 8px;
    min-height: 640px;
    overflow-x: auto;
    line-height: 16px;
    margin: 16px 0;
}
pre.terminal > code { font-size: 15px; }

/* blinking cursor */
pre.terminal > code::after {
    content: "_";
    color: var(--c5);
    animation: blink 1.5s step-start infinite;
}
.no-cursor::after { animation: none !important; }
@keyframes blink { 50% { opacity: 0; } }

/* mobile */
@media (max-width: 600px) {
    body { font-size: 11px; padding: 0 4px; }
    pre.terminal > code { font-size: 10px; }
    #nav a { padding: 10px 8px; }
}

/* footer */
.footer { text-align: center; font-size: 11px; color: var(--c4);
          margin-top: 16px; padding-bottom: 16px; }
.footer a { color: var(--c4); }

/* button */
.btn { display: inline-block; padding: 5px 16px; border: 1px solid var(--c2);
       color: var(--c2); font-size: 12px; margin-top: 12px; }
.btn:hover { background: var(--c2); color: #1c1a16; text-decoration: none; }

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
const G0 = '<span style="color:#b9746f">';
const G1 = '<span style="color:#cd9b98">';
const G2 = '<span style="color:#c3b283">';
const G3 = '<span style="color:#9db9b2">';
const G4 = '<span style="color:#79be9a">';
const G5 = '<span style="color:#a2d2b9">';
const G6 = '<span style="color:#dcd6d6">';
const C1 = '<span style="color:#9db9b2">';
const C2 = '<span style="color:#79be9a">';
const DM = '<span style="opacity:0.45">';
const BD = '<span style="font-weight:700">';
const R  = '</span>';

const COMMANDS = [
    {
        cmd: 'curl arpatek.dev',
        coloredCmd: `${G2}curl${R} ${C1}arpatek.dev${R}`,
        lines: `

${G0}         :::     :::::::::  :::::::::     ::: ::::::::::: :::::::::: :::    :::${R}
${G1}       :+: :+:   :+:    :+: :+:    :+:  :+: :+:   :+:     :+:        :+:   :+:${R}
${G2}     +:+   +:+  +:+    +:+ +:+    +:+ +:+   +:+  +:+     +:+        +:+  +:+${R}
${G3}   +#++:++#++: +#++:++#:  +#++:++#+ +#++:++#++: +#+     +#++:++#   +#++:++${R}
${G4}  +#+     +#+ +#+    +#+ +#+       +#+     +#+ +#+     +#+        +#+  +#+${R}
${G5} #+#     #+# #+#    #+# #+#       #+#     #+# #+#     #+#        #+#   #+#${R}
${G6}###     ### ###    ### ###       ###     ### ###     ########## ###    ###${R}

  ${BD}Juan Garcia${R} — Linux technologist &amp; automation engineer
  ${C1}https://arpatek.dev${R} | ${DM}"No future. Only uptime."${R}


${C2}┌─About───────────────────────────┐${R} ${C2}┌─Links────┬────────────────────────────────┐${R}
${C2}│${R}                                 ${C2}│${R} ${C2}│${R}          ${C2}│${R}                                ${C2}│${R}
${C2}│${R}  Systems automation engineer    ${C2}│${R} ${C2}│${R} Codeberg ${C2}│${R} ${C1}codeberg.org/arpatek${R}           ${C2}│${R}
${C2}│${R}  based in California. 3 years   ${C2}│${R} ${C2}│${R} LinkedIn ${C2}│${R} ${C1}linkedin.com/in/arpatek${R}        ${C2}│${R}
${C2}│${R}  of hardware &amp; UNIX lab work at ${C2}│${R} ${C2}│${R}          ${C2}│${R}                                ${C2}│${R}
${C2}│${R}  TrueNAS. Now building a        ${C2}│${R} ${C2}└──────────┴────────────────────────────────┘${R}
${C2}│${R}  self-hosted homelab using IaC. ${C2}│${R} ${C2}┌─Latest────────────────────────────────────┐${R}
${C2}│${R}                                 ${C2}│${R} ${C2}│${R}  RHCSA                        ${C1}in progress${R} ${C2}│${R}
${C2}└─────────────────────────────────┘${R} ${C2}└───────────────────────────────────────────┘${R}

  ${C2}Legend${R}

  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev${R}              This page
  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev/man${R}          Full resume in manpage format
  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev/uses${R}         Hardware &amp; software setup
  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev/lab${R}          Homelab services (home.arpa)
  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev/changelog${R}    Site and project history
  ${G6}$${R} ${G2}curl${R} ${C1}arpatek.dev/help${R}         All available endpoints

`.split('\n')
    },
];


"""

# ──[ Terminal JS logic ]───────────────────────────────────────────────────────────────
_TERMINAL_JS = r"""
const SPEED      = 90;
const INIT_DELAY = 1800;
const LOOP_DELAY = 6000;

const term = document.getElementById('term').children[0];

const BLINK_ON      = 1;
const BLINK_OFF     = 2;
const HIGHLIGHT_CMD = 3;

function setCursor(on) {
    if (on) term.classList.remove('no-cursor');
    else    term.classList.add('no-cursor');
}

function runCommand(idx, done) {
    const { cmd, coloredCmd, lines } = COMMANDS[idx];
    const chars = [BLINK_OFF, ...cmd.split(''), HIGHLIGHT_CMD, '\n', ...lines.map(l => l + '\n'), `${G6}$${R} `, BLINK_ON];

    setCursor(true);
    term.innerHTML = `${G6}$${R} `;

    let i = 0;
    function tick() {
        if (i === chars.length) { done(); return; }
        const c = chars[i++];
        if      (c === BLINK_ON)      { setCursor(true);                                          }
        else if (c === BLINK_OFF)     { setCursor(false);                                         }
        else if (c === HIGHLIGHT_CMD) { term.innerHTML = `${G6}$${R} ` + (coloredCmd || cmd);    }
        else                          { term.innerHTML += c;                                       }
        setTimeout(tick, SPEED);
    }
    tick();
}

// ── Boot sequence ─────────────────────────────────────────────────────────────
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
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}
</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/" class="active">home</a>
      <a href="/man">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/now">now</a>
      <a href="/resume" class="right">contact</a>
    </div>

    <h1><a href="/lambda" target="_blank" style="color:inherit;text-decoration:none;font-size:1.3em;vertical-align:middle">λ</a> arpatek.dev</h1>

    <pre class="terminal" id="term"><code></code></pre>

    <div class="footer">
      <code>
        <a href="https://codeberg.org/arpatek/arpatek.dev">source code</a> &nbsp;|&nbsp;
        <a href="https://linkedin.com/in/arpatek">linkedin</a> &nbsp;|&nbsp;
        <a href="/cv" download>resume</a>
      </code>
    </div>
  </div>
  <script>{_COMMANDS_JS}</script>
  <script>{_TERMINAL_JS}</script>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Manpage / Resume ]────────────────────────────────────────────────────────────────
MANPAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>manpage</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man" class="active">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/now">now</a>
      <a href="/resume" class="right">contact</a>
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
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Uses ]────────────────────────────────────────────────────────────────────────────
USES = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>uses — arpatek</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man">manpage</a>
      <a href="/uses" class="active">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/now">now</a>
      <a href="/resume" class="right">contact</a>
    </div>

    <div class="man-header">
      <span>USES(7)</span><span>Hardware &amp; Software</span><span>USES(7)</span>
    </div>

    <div class="section">
      <h2>Hardware</h2>
      <div class="entry">
        <div class="entry-title">M1 Mac Mini</div>
        <div class="entry-org">Main workstation &mdash; macOS</div>
      </div>
      <div class="entry">
        <div class="entry-title">M1 MacBook Air</div>
        <div class="entry-org">Laptop &mdash; Asahi Linux</div>
      </div>
      <div class="entry">
        <div class="entry-title">ASUS PN51 &mdash; Ryzen 7 5700U</div>
        <div class="entry-org">Proxmox hypervisor (devstem)</div>
      </div>
      <div class="entry">
        <div class="entry-title">Raspberry Pi</div>
        <div class="entry-org">DNS / DHCP / VPN (netrunner-rpi)</div>
      </div>
    </div>

    <div class="section">
      <h2>Software</h2>
      <p><span class="label">Shell</span> zsh (Mac, Asahi) &nbsp;&bull;&nbsp; bash (servers)</p>
      <p><span class="label">Editor</span> Neovim + LazyVim (Mac, MacBook) &nbsp;&bull;&nbsp; Vim (RHEL)</p>
      <p><span class="label">Terminal</span> iTerm2 (Mac) &nbsp;&bull;&nbsp; Ghostty (MacBook)</p>
      <p><span class="label">OS</span> macOS &nbsp;&bull;&nbsp; Asahi Linux &nbsp;&bull;&nbsp; Rocky Linux 9 &nbsp;&bull;&nbsp; Debian 13</p>
    </div>

    <div class="man-footer">
      <span>arpatek</span><span>California, USA</span><span>arpatek.dev/uses</span>
    </div>
  </div>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Lab ]─────────────────────────────────────────────────────────────────────────────
LAB = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>lab — arpatek</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab" class="active">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/now">now</a>
      <a href="/resume" class="right">contact</a>
    </div>

    <div class="man-header">
      <span>LAB(8)</span><span>home.arpa</span><span>LAB(8)</span>
    </div>

    <div class="section">
      <h2>Infrastructure</h2>
      <div class="entry">
        <div class="entry-title">Proxmox VE 9</div>
        <div class="entry-org">devstem &nbsp;&bull;&nbsp; ASUS PN51 (Ryzen 7 5700U) &nbsp;&bull;&nbsp; <a href="https://pve.arpatek.dev">pve.arpatek.dev</a></div>
        <ul><li>Single-node hypervisor running all VMs. No cluster, no HA — intentional.</li></ul>
      </div>
      <div class="entry">
        <div class="entry-title">k3s &mdash; 3-node cluster</div>
        <div class="entry-org">prod-k3s-master-0 + 2 workers &nbsp;&bull;&nbsp; Debian 13</div>
        <ul>
          <li>Lightweight Kubernetes for public workloads. Traefik ingress, cert-manager TLS.</li>
          <li>Runs arpatek.dev and proxies git.arpatek.dev, gf.arpatek.dev, pm.arpatek.dev, pi.arpatek.dev, pve.arpatek.dev</li>
        </ul>
      </div>
    </div>

    <div class="section">
      <h2>Identity &amp; Network</h2>
      <div class="entry">
        <div class="entry-title">FreeIPA</div>
        <div class="entry-org">prod-ipa-0 &nbsp;&bull;&nbsp; Rocky Linux 9</div>
        <ul><li>Central identity, SSH auth, sudo policy, and DNS authority for home.arpa. Every VM is an IPA client.</li></ul>
      </div>
      <div class="entry">
        <div class="entry-title">Pi-hole</div>
        <div class="entry-org">netrunner-rpi &nbsp;&bull;&nbsp; Raspberry Pi &nbsp;&bull;&nbsp; <a href="https://pi.arpatek.dev">pi.arpatek.dev</a></div>
        <ul><li>Network-wide DNS resolver, DHCP server, and content filter. Upstream for FreeIPA queries.</li></ul>
      </div>
      <div class="entry">
        <div class="entry-title">WireGuard</div>
        <div class="entry-org">netrunner-rpi &nbsp;&bull;&nbsp; Raspberry Pi</div>
        <ul><li>VPN into the 10.33.111.0/24 network. Connected clients use Pi-hole for DNS, matching LAN behavior.</li></ul>
      </div>
    </div>

    <div class="section">
      <h2>Dev &amp; Observability</h2>
      <div class="entry">
        <div class="entry-title">Gitea + act_runner</div>
        <div class="entry-org">prod-git-0 &nbsp;&bull;&nbsp; Debian 13 &nbsp;&bull;&nbsp; <a href="https://git.arpatek.dev">git.arpatek.dev</a></div>
        <ul><li>Self-hosted Git, container registry, and CI/CD. Pushes built images to k3s on every commit.</li></ul>
      </div>
      <div class="entry">
        <div class="entry-title">PLG Stack &mdash; Prometheus, Loki, Grafana</div>
        <div class="entry-org">prod-mon-0 &nbsp;&bull;&nbsp; Debian 13 &nbsp;&bull;&nbsp; <a href="https://gf.arpatek.dev">gf.arpatek.dev</a> &nbsp;&bull;&nbsp; <a href="https://pm.arpatek.dev">pm.arpatek.dev</a></div>
        <ul><li>Hub-and-spoke observability. node_exporter + cAdvisor + Alloy agents on every host.</li></ul>
      </div>
    </div>

    <div class="man-footer">
      <span>LAB(8)</span><span>home.arpa</span><span>LAB(8)</span>
    </div>
  </div>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Changelog ]───────────────────────────────────────────────────────────────────────
CHANGELOG = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>changelog — arpatek</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog" class="active">changelog</a>
      <a href="/resume" class="right">contact</a>
    </div>

    <div class="man-header">
      <span>CHANGELOG(7)</span><span>arpatek</span><span>CHANGELOG(7)</span>
    </div>

    <div class="section">
      <h2>2026-05-12</h2>
      <div class="entry">
        <div class="entry-title">Site: /contact page, /cv PDF download, footer links redesign</div>
        <div class="entry-org">arpatek.dev &mdash; source code, linkedin, resume in footer</div>
      </div>
      <div class="entry">
        <div class="entry-title">Site: /uses, /lab, /changelog pages; syntax-highlighted terminal</div>
        <div class="entry-org">arpatek.dev &mdash; λ title, animated favicon, /lambda, screensaver removed</div>
      </div>
      <div class="entry">
        <div class="entry-title">Homelab: Traefik ingresses for all internal services</div>
        <div class="entry-org">pve, gf, pm, pi.arpatek.dev publicly exposed via k3s + Cloudflare</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-05-10</h2>
      <div class="entry">
        <div class="entry-title">Site: initial launch &mdash; terminal animation, ASCII art, easter eggs</div>
        <div class="entry-org">arpatek.dev &mdash; /man, /lambda, /boo, /xmas, /help</div>
      </div>
      <div class="entry">
        <div class="entry-title">Homelab: k3s cluster, arpatek.dev on Kubernetes, wildcard TLS</div>
        <div class="entry-org">home.arpa &mdash; cert-manager + Let's Encrypt, Gitea ingress</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-04-30</h2>
      <div class="entry">
        <div class="entry-title">Homelab: PLG observability stack</div>
        <div class="entry-org">Prometheus, Loki, Grafana &mdash; central server + Debian &amp; RHEL agents</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-03-28</h2>
      <div class="entry">
        <div class="entry-title">Homelab: Gitea + act_runner CI/CD</div>
        <div class="entry-org">git.arpatek.dev &mdash; self-hosted Git, container registry, push-to-deploy</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-03-01</h2>
      <div class="entry">
        <div class="entry-title">Homelab: FreeIPA &mdash; identity, auth, DNS</div>
        <div class="entry-org">prod-ipa-0 &mdash; SSH policy, HBAC, BIND for home.arpa</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-02-21</h2>
      <div class="entry">
        <div class="entry-title">Homelab: WireGuard VPN</div>
        <div class="entry-org">netrunner-rpi &mdash; remote access into 10.33.111.0/24</div>
      </div>
    </div>

    <div class="section">
      <h2>2026-01-11</h2>
      <div class="entry">
        <div class="entry-title">Homelab: Pi-hole &mdash; DNS, DHCP, content filter</div>
        <div class="entry-org">netrunner-rpi &mdash; network-wide resolver, upstream for FreeIPA</div>
      </div>
    </div>

    <div class="man-footer">
      <span>CHANGELOG(7)</span><span>arpatek</span><span>CHANGELOG(7)</span>
    </div>
  </div>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Contact ]─────────────────────────────────────────────────────────────────────────
CONTACT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>contact — arpatek</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/resume" class="active right">contact</a>
    </div>

    <div class="man-header">
      <span>CONTACT(7)</span><span>arpatek</span><span>CONTACT(7)</span>
    </div>

    <div class="section">
      <h2>Name</h2>
      <p>Juan Garcia &mdash; Linux technologist &amp; automation engineer</p>
    </div>

    <div class="section">
      <h2>Location</h2>
      <p>California, USA</p>
    </div>

    <div class="section">
      <h2>Contact</h2>
      <p><span class="label">Email</span> <a href="mailto:juang.sh@proton.me">juang.sh@proton.me</a></p>
    </div>

    <div class="section">
      <h2>Links</h2>
      <p><span class="label">Codeberg</span> <a href="https://codeberg.org/arpatek">codeberg.org/arpatek</a></p>
      <p><span class="label">LinkedIn</span> <a href="https://linkedin.com/in/arpatek">linkedin.com/in/arpatek</a></p>
    </div>

    <div class="man-footer">
      <span>CONTACT(7)</span><span>California, USA</span><span>CONTACT(7)</span>
    </div>
  </div>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

# ──[ Now ]─────────────────────────────────────────────────────────────────────────────
NOW = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>now — arpatek</title>
  <link rel="icon" type="image/gif" href="/static/favicon.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>{_STYLES}</style>
</head>
<body>
  <div id="container">
    <div id="nav">
      <a href="/">home</a>
      <a href="/man">manpage</a>
      <a href="/uses">uses</a>
      <a href="/lab">lab</a>
      <a href="/changelog">changelog</a>
      <a href="/now" class="active">now</a>
      <a href="/resume" class="right">contact</a>
    </div>

    <div class="man-header">
      <span>NOW(7)</span><span>2026-05-12</span><span>NOW(7)</span>
    </div>

    <div class="section">
      <h2>Work</h2>
      <p>Building out the homelab &mdash; k3s, IaC, observability. This site.</p>
    </div>

    <div class="section">
      <h2>Reading</h2>
      <ul>
        <li>The Bible (RSVCE)</li>
        <li>Behold a Pale Horse &mdash; William Cooper</li>
        <li>The Alchemist &mdash; Paulo Coelho</li>
        <li>The Four Agreements &mdash; Don Miguel Ruiz</li>
        <li>Metamorphosis &mdash; Kafka</li>
        <li>Crime and Punishment &mdash; Dostoevsky</li>
        <li>The Plague &mdash; Camus</li>
        <li>The Stranger &mdash; Camus</li>
        <li>Learning Modern Linux &mdash; Michael Hausenblas</li>
      </ul>
    </div>

    <div class="section">
      <h2>Watching</h2>
      <ul>
        <li>Catholic theology debates</li>
        <li>Roast of Kevin Hart &mdash; Netflix &nbsp;<span style="color:var(--c4)">pretty funny</span></li>
      </ul>
    </div>

    <div class="section">
      <h2>Playing</h2>
      <p>Pok&eacute;mon Champions &mdash; copying meta teams, not sorry.</p>
    </div>

    <div class="section">
      <h2>Daily Driver</h2>
      <p>Testing Asahi Linux on the M1 MacBook Air. Mostly works.</p>
    </div>

    <div class="man-footer">
      <span>NOW(7)</span><span>California, USA</span><span>NOW(7)</span>
    </div>
  </div>
  <script>{_FAVICON_JS}</script>
</body>
</html>"""

