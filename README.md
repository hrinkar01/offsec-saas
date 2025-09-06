# OffSec-SaaS (MVP)

Offensive Security as a Service (OSaaS) – An automated red-team style platform that continuously simulates hacker attacks, runs recon, and reports vulnerabilities in real time.
This is a Day 1 MVP skeleton with FastAPI backend, React frontend, and PostgreSQL database.

# Features (Day 1)

 FastAPI backend running at http://127.0.0.1:8000

 React frontend running at http://localhost:3000

 Connected FE ↔ BE (displays API message)

 PostgreSQL container (ready for later models)

✅ Day 1 Deliverable

Add a target project skeleton.

FE fetches message from BE:

"OffSec SaaS API is running 🚀"

# Next Steps
## WEEK 1 – Recon + Core Foundation

Day 1 – Project Bootstrapping

Setup GitHub repo.

Backend: FastAPI (Python) (super lightweight).

DB: Postgres (free).

Frontend: React (scaffold with Vite or CRA).

Setup a dummy “add target” form.

Day 2 – Subdomain Recon (Free Tools)

Integrate Sublist3r or Amass → discover subdomains.

Command → Python wrapper → return JSON.

Store results in DB.

Day 3 – Port & Service Scan

Integrate Nmap (python-nmap).

Scan top 1000 ports for a given domain.

Parse into JSON.

Day 4 – Banner Grabbing

Extend Nmap: capture service/version banners.

Add “Tech stack detected” (Apache, nginx, MySQL, etc).

Day 5 – Dashboard Basics

React: Show subdomains + ports + banners in table.

Add “Risk badge” → (open RDP port = Red, HTTPS = Green).

Day 6 – GitHub Exposure Scan

Use GitHub dorks via free search API (rate limited but free).

Parse if API keys, passwords, or “.env” files show up.

Day 7 – Buffer/Testing

Polish API routes.

Fix bugs.

👉 End of Week 1 Deliverable: Enter domain → see subdomains, open ports, services, and possible exposed keys in a clean dashboard.

## WEEK 2 – Offensive Simulation (Free Tools)

Day 8 – Add Weak Password Check

Use hydra (offline tool) → brute force weak creds on SSH/FTP (just a few tries, not DoS).

Wrap output in JSON.

Day 9 – Vulnerability Scanner Integration

Use Nmap NSE scripts (free vulns detection).

Example: SSL vulns, SMB vulns.

Parse results into “Critical/High/Medium/Low.”

Day 10 – Web Vuln Checks

Add Nikto (open-source web vuln scanner).

Run basic checks → parse into DB.

Day 11 – Parser & Risk Score

Convert raw tool outputs → findings format:

Title

Severity

Description

Suggested Fix

Assign scores manually (no AI).

Day 12 – PDF Reports

Generate reports via ReportLab or wkhtmltopdf.

Include project name, summary, findings, fixes.

Day 13 – Dashboard Upgrade

Add charts (React chart.js): severity pie chart.

Add timeline (“scan run at 2 PM”).

Day 14 – Buffer

Debug multiple targets flow.

👉 End of Week 2 Deliverable: Recon + simulated attacks → dashboard + PDF report.

## WEEK 3 – Notifications & Multi-Project

Day 15 – Email Alerts

Use free SMTP (Gmail/Yahoo).

Send “⚠️ Critical vuln found on example.com.”

Day 16 – Multi-Project Support

User can add multiple domains.

Separate results by project ID.

Day 17 – User Auth

Basic JWT auth (fastapi-users).

Signup/Login/Logout.

Day 18 – Dashboard Polish

Add filters (Critical only, Web vulns only).

Severity badges (red/orange/yellow/green).

Day 19 – Scan History

Store multiple scan runs → compare results over time.

Day 20 – Mock Jira Integration

Add “Send to Jira” button (just saves in DB as ‘ticket created’).

Day 21 – Buffer

Test end-to-end flow.

👉 End of Week 3 Deliverable: Multi-project, email alerts, dashboard with history, login system.

## WEEK 4 – Deployment & Final Demo Prep

Day 22 – Deployment Setup

Use Heroku (free tier) or Render.com free plan.

Push FastAPI backend.

Deploy frontend to Netlify/Vercel.

Day 23 – Orchestration

Add background job queue → Celery + Redis (run scans async).

Prevent UI from freezing.

Day 24 – Demo Flow Polish

Create smooth flow:

Add target → scan starts.

Recon + vulns show on dashboard.

Email alert triggered.

PDF report downloadable.

Day 25 – Final Dry Run + Backup

Backup DB.

Take screenshots/video of workflow.

Practice pitch.

👉 End of Week 4 Deliverable: A live MVP platform deployed online that:

Runs recon + vulns scan.

Simulates weak attacks.

Generates PDF reports.

Sends alerts.

Has dashboard + history.
