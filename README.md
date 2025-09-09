offsec-saas/
│
├── agent/                          # 🚀 Runs on Raspberry Pi 4B
│   ├── agent.py                    # Main Pi orchestrator
│   ├── scheduler.py                 # Manages plugin execution & OLED updates
│   │
│   ├── plugins/                    # Offensive features (Pi-side scans)
│   │   ├── port_scan.py             # [Pi] Port & Service Scanning
│   │   ├── tech_fingerprint.py      # [Pi] Tech Stack Fingerprinting
│   │   ├── subdomain_enum.py        # [Pi] Subdomain Enumeration
│   │   ├── dir_bruteforce.py        # [Pi] Directory/Endpoint Bruteforce
│   │   ├── sql_injection.py         # [Pi] SQL Injection Auto-Testing
│   │   ├── xss_check.py             # [Pi] XSS Injection
│   │   ├── cmd_injection.py         # [Pi] Command Injection Check
│   │   ├── file_upload.py           # [Pi] File Upload Exploit Detection
│   │   ├── csrf_check.py            # [Pi] CSRF Weakness Detection
│   │   ├── ssrf_check.py            # [Pi] SSRF Checks
│   │   ├── auth_bruteforce.py       # [Pi] Weak Login Bruteforce
│   │   ├── cred_stuffing.py         # [Pi] Credential Stuffing
│   │   ├── session_hijack.py        # [Pi] Session Hijacking
│   │   ├── jwt_check.py             # [Pi] JWT/Token Weakness Check
│   │   ├── access_control.py        # [Pi] Broken Access Control
│   │   ├── priv_esc_web.py          # [Pi] Privilege Escalation in Web App
│   │   ├── dir_traversal.py         # [Pi] Directory Traversal
│   │   ├── idor.py                  # [Pi] IDOR Exploitation
│   │   ├── debug_panels.py          # [Pi] Exposed Debug Panels
│   │   ├── tls_ssl_test.py          # [Pi] TLS/SSL Misconfig
│   │   ├── mixed_content.py         # [Pi] Mixed Content Detection
│   │   ├── cookie_flags.py          # [Pi] Session Cookie Flags Check
│   │   ├── cve_replay.py            # [Pi/SaaS] Known CVE Replay
│   │   └── poc_exploit.py           # [Pi] PoC Exploit Simulation
│   │
│   ├── display/                    # OLED display integration
│   │   └── oled_display.py          # [Pi] Show scan status/results
│   │
│   ├── utils/                      # Helper scripts
│   │   ├── logger.py                # [Pi] Log results locally
│   │   ├── notifier.py              # [Pi → SaaS] Push alerts
│   │   └── parser.py                # [Shared] Parse scan outputs
│   │
│   └── results/                    # Local Pi results storage
│       ├── logs/                    # raw scan outputs
│       ├── reports/                 # HTML/PDF reports
│       └── db.sqlite3               # local scan database
│
├── saas/                           # 🌐 Runs on Cloud / Server
│   ├── app.py                      # Web server entrypoint (Flask/FastAPI)
│   │
│   ├── api/                        # REST APIs
│   │   ├── scans.py                 # [SaaS] Receive/upload Pi scan results
│   │   └── users.py                 # [SaaS] User accounts, auth (future)
│   │
│   ├── core/                       # Core business logic
│   │   ├── database.py              # [SaaS] Store results in Postgres
│   │   ├── report_manager.py        # [SaaS] Render reports & analytics
│   │   └── scheduler_api.py         # [SaaS → Pi] Remote scan trigger (future)
│   │
│   ├── templates/                  # Web pages
│   │   ├── index.html               # Landing/dashboard
│   │   ├── dashboard.html           # Show results visually
│   │   └── report.html              # Detailed vulnerability report
│   │
│   ├── static/                     # Frontend assets
│   │   ├── css/
│   │   └── js/
│   │
│   ├── tests/                      # Web/SaaS tests
│   └── saas_config.py              # SaaS settings
│
├── common/                         # 🔗 Shared across Pi + SaaS
│   ├── config.py                    # global configs
│   ├── schema.py                    # JSON schema for Pi ↔ SaaS results
│   └── utils.py                     # shared utilities
│
├── deploy/                         # Deployment configs
│   ├── docker-compose.yml           # deploy full SaaS stack
│   ├── Dockerfile.agent             # container for Pi agent
│   └── Dockerfile.saas              # container for SaaS web
│
├── tests/                          # Tests for Pi agent
│
├── README.md
├── requirements.txt
└── setup.sh
