# OffSec-SaaS (MVP)

Offensive Security as a Service (OSaaS) – An automated red-team style platform that continuously simulates hacker attacks, runs recon, and reports vulnerabilities in real time.
This is a Day 1 MVP skeleton with FastAPI backend, React frontend, and PostgreSQL database.

# ⚡ Offensive Web App Features (Hackathon-Ready)
## 🌐 Recon & Discovery

Port & Service Scanning → nmap -sV target.com to enumerate open ports and service versions.

Tech Stack Fingerprinting → whatweb target.com to detect CMS, frameworks, and languages.

Subdomain Enumeration → subfinder -d target.com to uncover hidden subdomains.

Directory/Endpoint Bruteforce → gobuster dir -u target.com -w wordlist.txt to find hidden paths.

## 💉 Input Attacks

SQL Injection Auto-Testing → sqlmap -u "http://target.com/page?id=1" to detect and exploit SQLi.

XSS Injection → xsstrike -u target.com/page to test reflected and stored XSS payloads.

Command Injection Check → commix --url="http://target.com/page?cmd=ls" to detect OS injections.

File Upload Exploit Detection → Upload shell.php.jpg and request it back to bypass filters.

CSRF Weakness Detection → Analyze POST forms; missing/constant token = vulnerable.

SSRF Checks → Inject http://127.0.0.1:22 or file:///etc/passwd into URL params and observe response.

## 🔒 Authentication / Session Attacks

Weak Login Bruteforce → hydra -l admin -P passwords.txt target.com http-post-form.

Credential Stuffing → Replay breached creds (e.g., from RockYou) against login endpoint.

Session Hijacking → Reuse stolen session cookies (document.cookie) to bypass login.

JWT/Token Weakness Check → jwt_tool <token> to brute-force or forge weak JWTs.

## 📡 App Logic & Config Attacks

Broken Access Control → Directly visit /admin or modify POST roles to escalate privileges.

Privilege Escalation in Web App → Change numeric IDs in requests to access restricted data.

Directory Traversal → Replace params with ../../etc/passwd to read system files.

IDOR (Insecure Direct Object Ref.) → Change user_id=123 → 124 to view other users’ data.

Exposed Debug Panels → Access /phpinfo, /swagger, /debug for sensitive config leaks.

## 🔑 Encryption & Network Layer

TLS/SSL Misconfig → testssl.sh target.com to check weak ciphers and expired certs.

Mixed Content Detection → Look for HTTPS pages loading http:// scripts.

Session Cookie Flags Check → Inspect Set-Cookie headers for missing HttpOnly/Secure.

## 🐍 Exploit Replay & PoC

Known CVE Replay → searchsploit <service version> or msfconsole for public exploits.

PoC Exploit Simulation → Replace real RCE with fake “Exploit Succeeded” message in report (safe demo).

# Features (Day 1)

 FastAPI backend running at http://127.0.0.1:8000

 React frontend running at http://localhost:3000

 Connected FE ↔ BE (displays API message)

 PostgreSQL container (ready for later models)

✅ Day 1 Deliverable

Add a target project skeleton.

FE fetches message from BE:

"OffSec SaaS API is running 🚀"

