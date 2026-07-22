 <div align="center">

# 🏙️ CivicIQ
### Autonomous Civic Incident Intelligence System

**"Different complaints. One hidden signal."**

*Cities don't have a shortage of complaints. They have a shortage of intelligence connecting those complaints.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-frontend-61DAFB?logo=react&logoColor=black)
![Status](https://img.shields.io/badge/status-demo--ready-brightgreen)
![License](https://img.shields.io/badge/license-fictional--demo-lightgrey)

</div>

---

## 🎯 What It Does

CivicIQ is a multi-agent system for municipal operators and citizens to **detect, analyze, prioritize, and verify** civic infrastructure incidents — automatically.

By correlating the geographic and temporal proximity of independent citizen reports, CivicIQ uncovers **cascading root-cause failures** that no single complaint would reveal on its own.

> **Example:** A water pipe burst weakens a road base → potholes form → potholes pool water → traffic-blocking waterlogging. Four separate complaints, one root cause. CivicIQ connects the dots, assigns the right departments in the right order, and verifies the fix with photo + GPS validation.

---

## 🛠️ Multi-Agent Architecture

CivicIQ runs a coordinated pipeline of **ten specialized backend agents**, each with a narrow, auditable responsibility.

| # | Agent | Responsibility | Core Logic |
| :-: | :--- | :--- | :--- |
| 1 | 👁️ **Perception** | Detects issue type, severity, confidence from photo + text | Deterministic image lookup + LLM evidence synthesis |
| 2 | 📍 **Clustering** | Finds geographically/temporally related reports | Haversine distance (<180m) + time window (<7 days) |
| 3 | 🔍 **Incident Detection** | Classifies the cluster | `INDEPENDENT` / `DUPLICATE` / `POSSIBLE_CONNECTED` / `HIGH_CONFIDENCE_CONNECTED` + LLM reasoning |
| 4 | 🕸️ **Root-Cause** | Traces causal chains between issues | Dependency graph walk (`civic_dependencies.json`) + LLM cascade hypothesis |
| 5 | ⚠️ **Civic Impact** | Scores public threat severity (0–100) | Weighted formula: Severity 30% · Proximity 20% · Impacted 15% · Duration 10% · Repeats 10% · Risks 15% |
| 6 | 🏛️ **Response** | Sequences multi-department resolution | Topological sort over roles/dependencies (`departments.json`) |
| 7 | 📄 **Filing** | Generates formal, traceable municipal filings | `FILE-[INC_ID]` records, clearly marked simulated |
| 8 | ⏰ **Escalation** | Tracks SLA deadlines, alerts management | State machine + demo time-travel |
| 9 | ✅ **Verification** | Validates resolution via photo/GPS proof | Location threshold (<100m) + new-complaint monitor |
| 10 | 🧭 **Orchestrator** | Coordinates state across all agents | Persists shared state to `incidents.json` |

<details>
<summary><strong>💡 Why ten agents instead of one big model?</strong></summary>

<br>

Each agent is small, deterministic where possible, and independently testable. This means:
- **Zero demo latency** — no waiting on flaky vision models mid-presentation
- **Auditability** — every decision traces back to explicit rules or a specific LLM call
- **Graceful degradation** — no API key? The system falls back to deterministic mock narratives automatically

</details>

---

## 🚀 Setup & Execution

### Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.10+ | Backend runtime |
| Node.js | 18+ | Frontend runtime |
| Groq API Key | Optional | Falls back to deterministic mock narratives — 100% stable offline demo mode |

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the root or `backend/` folder:

```env
GROQ_API_KEY=your_api_key_here
```

Seed the demo data and launch the API:

```bash
python -m backend.scripts.seed_data
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Then open **http://localhost:5173** 🎉

---

## 🎬 Rehearsed Live Demo Script

A step-by-step walkthrough for a smooth, reliable presentation.

| Step | Action | Expected Result |
|:-:|---|---|
| **1** | Go to **Submit Report** → select seed image `leak_01.jpg` (Water Leakage, Chakala Junction) → **Submit Complaint Report** | Report `CIV-2026-1001` created |
| **2** | Click **Go to Dashboard and Analyze** | Dashboard loads with new report visible |
| **3** | Find `CIV-2026-1001` in the *Citizen Reports Feed* → click **Run Agentic AI** | Live pipeline animates through 7 stages: perception → clustering (6 related complaints found) → detection → root cause → impact → response → filing |
| **4** | Inspect **Root Cause** card | Cascade hypothesis shown with disclaimer: *"AI-generated civic incident hypothesis. Physical inspection recommended."* |
| | Inspect **Civic Impact** gauge | Shows **CRITICAL (88/100)** |
| **5** | Scroll to **Response Plan** → review sequence (Water Board → Drainage → Roads) → **Approve Multi-Department Plan** | Status transitions to `ACTION_IN_PROGRESS` |
| **6** | *(Beat 1)* In **Resolution Verification**, submit `resolved_leak_wrong.jpg` (garbage overflow photo) | Verification Agent returns `LOCATION_MISMATCH` — ticket stays open |
| **7** | *(Beat 2)* Submit `resolved_leak_correct.jpg` (dry patched road, Chakala) | Verification Agent returns `RESOLUTION_VERIFIED` → status becomes **RESOLVED**, impact drops to **LOW** |
| **8** | On another scenario, click **Advance Time (+3 Days)** | SLA monitor triggers → status changes to **ESCALATED** with breach notification |

> 🎥 **Presenter tip:** Beats 6–7 are the emotional core of the demo — the system *refuses* a wrong photo before accepting the right one. Let that moment breathe.

---

## ⚖️ MVP vs. Stretch Scope

| Feature | Status | Rationale |
|---|:-:|---|
| Vision Core | ✅ **MVP (shipped)** | Swapped live vision models for deterministic lookups to guarantee zero demo latency and 100% stable presentation, while Groq LLM synthesizes the evidence narrative on top |
| Hindi Localization | ✂️ **Cut** | Deprioritized to focus engineering time on solid multi-agent coordination visuals |
| Full Escalation Ladder | 🔻 **Reduced** | Replaced with a single-tier manager alert system for MVP scope |

---

<div align="center">

*Fictional demonstration system · Fictional city wards · Synthetic citizen data*

</div>
