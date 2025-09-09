# 🗓️ 20-Day Roadmap — OffSec-SaaS
## Phase 1 – Foundations (Day 1–4)
Day 1 → Project Setup

Initialize GitHub repo with final file structure.

Add README.md, requirements.txt, setup.sh.

Setup virtual environments on both Pi & Laptop.

Test OLED with “Hello World” display script.

Day 2 → Core Agent Skeleton

Implement agent.py with plugin loader.

Add logger.py + db.sqlite3 for local results.

Display scan status on OLED.

Day 3 → First Plugin (Port Scan)

Code port_scan.py with nmap.

Store results in SQLite.

Show count of open ports on OLED.

Day 4 → SaaS Backend Skeleton

Flask/FastAPI setup (saas/app.py).

Create users.py (basic login/register).

Create scans.py (dummy API → accepts JSON).

Deploy locally with Docker.

## Phase 2 – Offensive Core (Day 5–10)
Day 5 → Tech Fingerprint & Subdomains

Implement tech_fingerprint.py (WhatWeb).

Implement subdomain_enum.py (subfinder).

Push JSON → SaaS API.

Day 6 → Directory Bruteforce

Add dir_bruteforce.py (Gobuster).

OLED shows “hidden dirs: X”.

SaaS shows table in dashboard.

Day 7 → SQLi & XSS

Add sql_injection.py (sqlmap).

Add xss_check.py (XSStrike).

Both lightweight → heavy scan mode offloaded to laptop if needed.

Day 8 → Command Injection & File Upload

Implement cmd_injection.py (Commix).

Add file_upload.py with payload bypass check.

Push all results to reports/.

Day 9 → CSRF & SSRF

Implement csrf_check.py.

Implement ssrf_check.py with crafted URLs.

OLED: ✅/❌ indicators for these.

Day 10 → Auth Weakness

Add auth_bruteforce.py (Hydra).

Add cred_stuffing.py (requires breach list → keep lightweight).

Push progress updates to OLED.

## Phase 3 – Advanced Exploits (Day 11–15)
Day 11 → Session & JWT

Implement session_hijack.py.

Implement jwt_check.py.

Store captured tokens in encrypted DB.

Day 12 → Access Control & Priv Esc

Add access_control.py.

Add priv_esc_web.py.

OLED: highlight CRITICAL if found.

Day 13 → Directory Traversal & IDOR

Add dir_traversal.py.

Add idor.py.

Auto-generate exploit PoC (curl request) into reports/.

Day 14 → Debug Panels

Add debug_panels.py scanning /debug, /phpinfo.

OLED shows “Debug: FOUND”.

Day 15 → Crypto / Config Checks

Add tls_ssl_test.py (testssl.sh).

Add mixed_content.py.

Add cookie_flags.py.

## Phase 4 – Finishing Offensive Pack (Day 16–18)
Day 16 → CVE Replay

Add cve_replay.py.

Auto-detect version from fingerprint → pull matching CVE exploits.

Day 17 → PoC Simulation

Implement poc_exploit.py → simulates exploit success.

Store fake reverse shell message → report.

Day 18 → SaaS Dashboard

Create dashboard.html → list scans.

Create report.html → view individual findings.

Generate PDF report option.

## Phase 5 – Integration & Polish (Day 19–20)
Day 19 → Integration

Finalize Pi → SaaS sync via notifier.py.

Test continuous 24/7 scans with scheduler.py.

Add OLED live updates for all 25 features.

Day 20 → Final Demo-Ready Build

Full system test.

Generate sample target scan → full report.

Create Pitch Deck + Live Demo flow.

Push polished README with file structure + flow diagram.

✅ End Goal (Day 20)

Pi agent runs all 25 offensive features.

OLED shows live scan status/results.

SaaS web portal receives results → shows dashboard + reports.

Supports 24/7 background scanning with logs, SQLite, PDF reports.