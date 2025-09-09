offsec-saas/
│
├── agent/                          # 🚀 Raspberry Pi 4B agent
│   ├── agent.py                    # Main Pi orchestrator
│   ├── scheduler.py                 # Manage scan execution & OLED updates
│   │
│   ├── plugins/                    # Offensive scanning modules (25 total)
│   │   ├── port_scan.py             # Port & Service Scanning
│   │   ├── tech_fingerprint.py      # Tech Stack Fingerprinting
│   │   ├── subdomain_enum.py        # Subdomain Enumeration
│   │   ├── dir_bruteforce.py        # Directory/Endpoint Bruteforce
│   │   ├── sql_injection.py         # SQL Injection Auto-Testing
│   │   ├── xss_check.py             # XSS Injection
│   │   ├── cmd_injection.py         # Command Injection Check
│   │   ├── file_upload.py           # File Upload Exploit Detection
│   │   ├── csrf_check.py            # CSRF Weakness Detection
│   │   ├── ssrf_check.py            # SSRF Checks
│   │   ├── auth_bruteforce.py       # Weak Login Bruteforce
│   │   ├── cred_stuffing.py         # Credential Stuffing
│   │   ├── session_hijack.py        # Session Hijacking
│   │   ├── jwt_check.py             # JWT/Token Weakness Check
│   │   ├── access_control.py        # Broken Access Control
│   │   ├── priv_esc_web.py          # Privilege Escalation in Web Apps
│   │   ├── dir_traversal.py         # Directory Traversal
│   │   ├── idor.py                  # Insecure Direct Object Reference
│   │   ├── debug_panels.py          # Exposed Debug Panels
│   │   ├── tls_ssl_test.py          # TLS/SSL Misconfig Detection
│   │   ├── mixed_content.py         # Mixed Content Detection
│   │   ├── cookie_flags.py          # Session Cookie Flags Check
│   │   ├── cve_replay.py            # Known CVE Replay
│   │   └── poc_exploit.py           # Proof-of-Concept Exploit Simulation
│   │
│   ├── display/
│   │   └── oled_display.py          # 0.96" OLED status/results display
│   │
│   ├── utils/
│   │   ├── logger.py                # Local logging
│   │   ├── notifier.py              # Push results → SaaS
│   │   └── parser.py                # Parse tool outputs
│   │
│   └── results/                     # Local storage on Pi
│       ├── logs/                    # Raw outputs
│       ├── reports/                 # HTML/PDF reports
│       └── db.sqlite3               # Local database
│
├── saas/                           # 🌐 SaaS Web Platform
│   ├── app.py                      # Web entrypoint (Flask/FastAPI)
│   │
│   ├── api/
│   │   ├── scans.py                 # Receive Pi scan results
│   │   └── users.py                 # User accounts & auth
│   │
│   ├── core/
│   │   ├── database.py              # Postgres DB integration
│   │   ├── report_manager.py        # Generate visual reports
│   │   └── scheduler_api.py         # Remote scan triggers (future)
│   │
│   ├── templates/
│   │   ├── index.html               # Landing/Dashboard
│   │   ├── dashboard.html           # Results overview
│   │   └── report.html              # Vulnerability report
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── tests/                       # Web tests
│   └── saas_config.py              # SaaS settings
│
├── common/                         # 🔗 Shared Pi ↔ SaaS
│   ├── config.py                    # Global configs
│   ├── schema.py                    # JSON schema for scan results
│   └── utils.py                     # Common utilities
│
├── deploy/                         # Deployment files
│   ├── docker-compose.yml           # Deploy SaaS stack
│   ├── Dockerfile.agent             # Pi agent container
│   └── Dockerfile.saas              # SaaS container
│
├── tests/                          # Pi agent tests
│
├── README.md
├── requirements.txt
└── setup.sh
