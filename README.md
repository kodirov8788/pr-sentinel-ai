# 🛡️ PR Sentinel AI: The AI-Native Code Auditor

[![Automation: n8n](https://img.shields.io/badge/Automation-n8n-FF6C37?style=flat-square&logo=n8n)](https://n8n.io/)
[![Self-Hosted: Codex CLI](https://img.shields.io/badge/AI-Codex%20CLI-blue?style=flat-square)](https://docs.codex.storage)
[![Infrastructure: Docker](https://img.shields.io/badge/Infrastructure-Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

**PR Sentinel AI** is an intelligent, self-hosted code review agent that acts as your team's "First Line of Defense." It uses **n8n** and your private **Codex CLI** subscription to audit every Pull Request *before* it reaches a human reviewer, catching expensive architectural, performance, and security flaws in seconds.

---

### 🏛️ Architecture: Why Codex CLI?
Unlike standard AI automations that send your code to a middleman's API, **PR Sentinel AI** uses the **Codex CLI** directly on your host machine.
*   **Data Sovereignty:** Your code never leaves your private environment for storage or training.
*   **Subscription Power:** It leverages your existing **Codex / Antigravity** subscription tokens for high-level "Senior Engineer" reasoning.
*   **Operational Security:** It runs within an n8n **Execute Command** node, allowing it to act on your filesystem securely.

### 🚩 The Problem: The "Senior Review Bottleneck"
*   **The Issue:** Senior Engineers are the single biggest bottleneck for shipping code. They spend **30–40% of their day** on low-complexity code reviews (syntax, nitpicks) instead of building core architecture.
*   **The Result:** Human reviews take 6–24 hours, causing "Lead Time to Production" targets to fail.

---

### 🚀 How it Works (The Workflow)

1.  **Trigger:** A new `Pull Request` is opened in GitHub (Webhook).
2.  **Fetch Diff:** n8n calls the GitHub API to fetch the `.diff` changes.
3.  **Audit (The Brain):** n8n executes the `codex` CLI command on the diff data using a "Senior Tech Lead" persona.
4.  **Feedback:** The AI sentinel posts its audit findings directly back to the GitHub PR as a comment.

### 🛠️ Getting Started

#### 1. Start n8n locally
Use Docker to run n8n with access to your system's `codex` binary:
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v /usr/local/bin/codex:/usr/local/bin/codex \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

#### 2. Import the Workflow
Import [**`workflows/pr-sentinel-v1.json`**](workflows/pr-sentinel-v1.json) into your n8n instance.

#### 3. Set up the GitHub Webhook
- **URL:** `http://your-server-ip:5678/webhook/github-webhook-pr`
- **Events:** Select `Pull requests`.

---

Developed by **@kodirov8788** | [LinkedIn](https://www.linkedin.com/in/mukhammadalikodirov/)
