<div align="center">🏙️ CivicIQ

Autonomous Civic Incident Intelligence System

Different Complaints. One Hidden Signal.

Cities don't have a shortage of complaints. They have a shortage of intelligence connecting those complaints.

<br>""Python" (https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)" (https://www.python.org/)
""FastAPI" (https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)" (https://fastapi.tiangolo.com/)
""React" (https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)" (https://react.dev/)
""Node.js" (https://img.shields.io/badge/Node.js-18+-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)" (https://nodejs.org/)
""AI Architecture" (https://img.shields.io/badge/Architecture-Multi--Agent-8A2BE2?style=for-the-badge)" (#-multi-agent-architecture)
""Demo" (https://img.shields.io/badge/Status-Demo--Ready-brightgreen?style=for-the-badge)" (#-live-demo-walkthrough)
""License" (https://img.shields.io/badge/License-Demo--Only-lightgrey?style=for-the-badge)" (#-project-scope-and-limitations)

An AI-powered civic intelligence platform that transforms isolated citizen complaints into connected incidents, prioritized response plans, and evidence-based resolution workflows.

</div>---

📌 Table of Contents

- "Overview" (#-overview)
- "The Problem" (#-the-problem)
- "The Solution" (#-the-solution)
- "Key Features" (#-key-features)
- "Multi-Agent Architecture" (#-multi-agent-architecture)
- "Incident Intelligence Workflow" (#-incident-intelligence-workflow)
- "Technology Stack" (#-technology-stack)
- "Project Structure" (#-project-structure)
- "Getting Started" (#-getting-started)
- "Live Demo Walkthrough" (#-live-demo-walkthrough)
- "MVP vs. Future Scope" (#-mvp-vs-future-scope)
- "Limitations and Safety" (#-limitations-and-safety)
- "Future Enhancements" (#-future-enhancements)
- "Contributing" (#-contributing)
- "Project Disclaimer" (#-project-disclaimer)

---

🎯 Overview

CivicIQ is a multi-agent civic incident intelligence system designed to help municipal operators identify related infrastructure problems, understand potential root causes, prioritize public impact, coordinate departmental responses, and verify reported resolutions.

Traditional complaint management systems often treat every report as an isolated ticket. CivicIQ takes a different approach: it analyzes the relationships between complaints across location, time, issue type, and infrastructure dependencies.

The result is a unified incident view that helps operators move beyond ticket management toward evidence-driven civic incident response.

🔎 The Core Idea

«Multiple complaints may describe different symptoms of the same underlying infrastructure failure.»

For example, a damaged underground water pipe may weaken a road foundation, contribute to pothole formation, and create localized waterlogging.

CivicIQ connects these reports into a potential incident chain, evaluates the resulting public risk, and proposes an ordered response involving the relevant municipal departments.

Important: a detected relationship is a hypothesis for investigation, not proof of physical causation.

---

🚨 The Problem

Municipal authorities receive complaints through multiple channels, often with incomplete information and limited visibility into relationships between incidents.

Challenge| Consequence
Fragmented complaints| Related problems are handled as separate tickets
Geographic and temporal overlap| Important patterns remain hidden
Unclear root causes| Teams may treat symptoms instead of underlying problems
Disconnected departments| Response activities can occur in the wrong order
Manual prioritization| High-impact incidents may not receive timely attention
Weak resolution evidence| Incorrect or unrelated proof may be accepted
Missed deadlines| Escalation can happen too late

The fundamental problem is not simply collecting complaints. It is connecting evidence, coordinating action, and validating outcomes.

---

💡 The Solution

CivicIQ introduces an intelligent incident lifecycle:

<div align="center">REPORT → CORRELATE → DETECT → INVESTIGATE → PRIORITIZE → COORDINATE → VERIFY

</div>1. Collect: Receive a citizen complaint containing issue details, location, timestamp, and supporting evidence.
2. Correlate: Identify reports that are geographically and temporally related.
3. Detect: Distinguish potential duplicates, independent incidents, and possibly connected problems.
4. Investigate: Generate candidate root-cause relationships using infrastructure dependencies and supporting evidence.
5. Prioritize: Calculate an explainable civic impact score.
6. Coordinate: Generate a proposed, dependency-aware multi-department response plan.
7. Track: Create simulated municipal filings and monitor service-level deadlines.
8. Verify: Evaluate submitted resolution evidence and update the incident lifecycle.

---

✨ Key Features

🧠 Multi-Agent Intelligence

Ten specialized backend agents perform focused tasks instead of relying on a single, opaque decision-making component.

📍 Geographic and Temporal Correlation

Identify potentially related reports using Haversine distance and configurable time windows.

🕸️ Root-Cause Hypothesis Generation

Combine infrastructure dependency rules with AI-generated reasoning to identify plausible cascading failures.

⚠️ Explainable Civic Impact Scoring

Calculate a normalized impact score using severity, proximity, population impact, duration, recurrence, and risk factors.

🏛️ Multi-Department Response Planning

Generate a dependency-aware response sequence so that proposed remediation follows the defined operational prerequisites.

📄 Traceable Municipal Filings

Create structured, simulated filing records linked to incident identifiers.

⏰ SLA Monitoring and Escalation

Track deadlines, simulate elapsed time, and trigger escalation when configured service-level thresholds are breached.

📸 Evidence-Based Resolution Verification

Evaluate resolution photographs and location evidence, rejecting mismatched evidence under the demo's verification rules.

🔄 Persistent Incident State

Maintain shared incident state through the orchestrator and the demo's JSON-backed persistence layer.

📴 Offline-Friendly Demonstration

Use deterministic rules and predefined narratives when an LLM API key is unavailable, keeping the core demonstration reproducible.

---

🏗️ Multi-Agent Architecture

CivicIQ uses ten specialized backend agents, coordinated through a shared incident lifecycle.

#| Agent| Primary Responsibility| Implementation Approach
01| 👁️ Perception| Extract issue type, severity, and confidence from complaint evidence| Deterministic image lookup and LLM evidence synthesis
02| 📍 Clustering| Find geographically and temporally related reports| Haversine distance below 180 m and a configurable seven-day window
03| 🔍 Incident Detection| Classify relationships between reports| Rule-based classification and LLM-assisted reasoning
04| 🕸️ Root-Cause Analysis| Identify plausible causal chains| Dependency graph traversal using "civic_dependencies.json"
05| ⚠️ Civic Impact| Estimate incident impact on the public| Weighted score from 0 to 100
06| 🏛️ Response Planning| Generate a coordinated departmental response| Dependency-aware ordering using "departments.json"
07| 📄 Filing| Create traceable municipal filing records| Structured "FILE-[INC_ID]" identifiers
08| ⏰ Escalation| Track deadlines and escalate overdue incidents| State machine and simulated time advancement
09| ✅ Verification| Evaluate submitted resolution evidence| Configured GPS-distance threshold and follow-up complaint checks
10| 🧭 Orchestrator| Coordinate agents and persist incident state| Shared state management using "incidents.json"

Why use multiple agents?

A single large model could attempt the entire workflow, but it would make individual decisions harder to test, audit, and reproduce.

CivicIQ separates responsibilities so that:

- Rules handle predictable operations: distance checks, scoring, deadline evaluation, and dependency ordering.
- LLMs handle selected reasoning tasks: evidence synthesis and candidate root-cause narratives.
- The orchestrator manages the workflow: agent outputs contribute to a consistent incident lifecycle.
- Fallback behavior preserves the demo: core deterministic paths remain available without an API key.

The architecture is multi-agent, but that does not automatically make every component an autonomous AI agent. The actual level of autonomy depends on the implementation of each component.

---

🔄 Incident Intelligence Workflow

flowchart TD
    A["Citizen Complaint"] --> B["Perception Agent"]
    B --> C["Geospatial & Temporal Clustering"]
    C --> D["Incident Relationship Detection"]
    D --> E["Root-Cause Hypothesis"]
    E --> F["Civic Impact Scoring"]
    F --> G["Multi-Department Response Plan"]
    G --> H["Simulated Municipal Filing"]
    H --> I["SLA Monitoring & Escalation"]
    I --> J["Resolution Evidence Submission"]
    J --> K{"Verification Passed?"}
    K -->|Yes| L["Mark Incident Resolved"]
    K -->|No| M["Keep Incident Open"]
    M --> J
    L --> N["Update Incident State"]

Example: One Infrastructure Failure, Multiple Symptoms

Report| Observed Problem| Potential Relationship
Report A| Water leakage| Possible initiating infrastructure issue
Report B| Road damage| Possible downstream effect
Report C| Pothole with standing water| Potentially related road and drainage issue
Report D| Localized waterlogging| Potentially connected drainage problem

CivicIQ can group these reports for investigation, propose a possible relationship chain, and recommend a coordinated response.

The system must not treat geographic proximity alone as proof that one incident caused another. Physical inspection and corroborating evidence remain necessary.

---

📊 Civic Impact Scoring

CivicIQ computes an impact score on a scale of 0–100 using the following weighted factors.

Factor| Weight| Purpose
Severity| 30%| Measures the seriousness of the reported issue
Proximity| 20%| Accounts for proximity to relevant locations or risk zones
People Impacted| 15%| Estimates the potential scale of public disruption
Duration| 10%| Accounts for how long the incident remains unresolved
Recurrence| 10%| Captures repeated complaints or recurring problems
Risk Factors| 15%| Accounts for additional public-safety or infrastructure risks
Total| 100%| 

Conceptually:

[
\begin{aligned}
I ={}& 0.30S + 0.20P + 0.15N\
&+ 0.10D + 0.10R + 0.15K
\end{aligned}
]

Where each normalized factor is scaled to the same range before aggregation.

The score supports transparent prioritization. It should not be interpreted as a calibrated probability of harm or a substitute for professional risk assessment.

Demo scenario: A seeded incident produces a critical impact score of 88/100. This is a predefined demonstration outcome, not a claim of validated real-world performance.

---

🛠️ Technology Stack

Layer| Technology| Role
Backend| Python 3.10+| Core application logic and agent orchestration
API| FastAPI| Backend endpoints and request handling
Frontend| React| Interactive operator interface
Runtime| Node.js 18+| Frontend development environment
AI reasoning| Groq API / configured LLM| Evidence synthesis and reasoning narratives
Geospatial analysis| Haversine distance| Geographic proximity calculations
Workflow logic| Python rules and state machines| Scoring, sequencing, escalation, and verification
Data persistence| JSON files| Demo incident state and configuration
Configuration| Environment variables| API credentials and runtime settings

The exact dependencies and model capabilities depend on the implementations and versions configured in the repository.

---

📁 Project Structure

The following is a representative layout of the documented components. Match it to the actual repository before treating every path as present.

CivicIQ/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   ├── scripts/
│   │   └── seed_data.py
│   ├── agents/
│   │   ├── perception.py
│   │   ├── clustering.py
│   │   ├── incident_detection.py
│   │   ├── root_cause.py
│   │   ├── civic_impact.py
│   │   ├── response.py
│   │   ├── filing.py
│   │   ├── escalation.py
│   │   ├── verification.py
│   │   └── orchestrator.py
│   ├── data/
│   │   ├── civic_dependencies.json
│   │   ├── departments.json
│   │   └── incidents.json
│   └── ...
├── frontend/
│   ├── package.json
│   ├── src/
│   ├── public/
│   └── ...
├── .gitignore
└── README.md

---

🚀 Getting Started

Follow these steps to run the demo locally.

Prerequisites

Requirement| Version| Required?
Python| 3.10 or newer| Yes
Node.js| 18 or newer| Yes
npm| Compatible with installed Node.js| Yes
Groq API key| Valid configured key| Optional, if fallback mode is implemented

1. Clone the Repository

git clone <YOUR_REPOSITORY_URL>
cd CivicIQ

Replace "<YOUR_REPOSITORY_URL>" with your actual repository URL.

2. Set Up the Backend

From the repository root:

python -m venv backend/venv
.\backend\venv\Scripts\Activate.ps1
python -m pip install -r backend/requirements.txt

If PowerShell blocks virtual environment activation, you can run the environment's Python executable directly instead of changing your system execution policy.

Create the environment file in the location supported by your application. For example, "backend/.env":

GROQ_API_KEY=your_groq_api_key_here

Do not commit ".env" or expose API credentials in screenshots, logs, or public repositories.

3. Seed Demo Data

Run the seeding command from the repository root if the script is configured for this import path:

python -m backend.scripts.seed_data

This should initialize the predefined incident scenarios required by the demonstration.

4. Start the Backend API

If "backend/main.py" defines the FastAPI application as "app":

python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000

If the module import path differs in your repository, use the corresponding module path. For example, when running from inside "backend/", the command may be:

python -m uvicorn main:app --host 127.0.0.1 --port 8000

FastAPI's interactive API documentation is typically available at:

"http://127.0.0.1:8000/docs"

5. Start the Frontend

Open a second terminal:

cd frontend
npm install
npm run dev

Open the local URL printed by Vite, typically:

"http://localhost:5173"

Ensure the frontend API base URL matches the backend address and that CORS is configured correctly for local development.

---

🎬 Live Demo Walkthrough

The following sequence describes the intended demonstration scenario.

Step| Action| Expected Outcome
1| Open Submit Report, select "leak_01.jpg" for the Water Leakage scenario at Chakala Junction, and submit| Report "CIV-2026-1001" is created
2| Select Go to Dashboard and Analyze| New report appears in the Citizen Reports Feed
3| Select the report and click Run Agentic AI| Pipeline processes perception, clustering, detection, root cause, impact, response, and filing
4| Inspect the Root Cause card| Candidate cascade hypothesis and inspection disclaimer appear
5| Inspect the Civic Impact gauge| Seeded scenario displays CRITICAL — 88/100
6| Review the Response Plan and approve it| Incident status changes to "ACTION_IN_PROGRESS"
7| Submit "resolved_leak_wrong.jpg" as resolution evidence| Verification returns "LOCATION_MISMATCH"; incident remains open
8| Submit "resolved_leak_correct.jpg"| Verification returns "RESOLUTION_VERIFIED"; incident becomes "RESOLVED"
9| Open another scenario and select Advance Time (+3 Days)| Configured SLA breach triggers escalation when its conditions are met

🎯 What the Demo Demonstrates

- Related complaints can be investigated as one potential incident.
- A root-cause hypothesis can connect different infrastructure symptoms.
- Impact scoring can help explain prioritization.
- Departmental work can be ordered according to configured dependencies.
- Resolution evidence can be rejected when it fails verification rules.
- Deadline breaches can trigger escalation.

Presenter tip: Spend the most time on the relationship between complaints and the resolution-verification step. Those features communicate CivicIQ's value more clearly than simply showing an AI-generated narrative.

The filenames, incident IDs, agent outputs, status transitions, and scores above describe the expected seeded scenario; verify them against the current implementation before a live presentation.

---

🧪 MVP vs. Future Scope

Feature| MVP Status| Implementation Notes
Complaint perception| Implemented in demo| Deterministic image lookup with evidence synthesis
Geographic clustering| Implemented in demo| Configured distance and time thresholds
Incident relationship detection| Implemented in demo| Rule-based classification and optional LLM reasoning
Root-cause hypotheses| Implemented in demo| Dependency graph and candidate narratives
Civic impact scoring| Implemented in demo| Weighted scoring formula
Department response planning| Implemented in demo| Dependency-aware ordering
Municipal filing| Simulated| No real government filing
SLA escalation| Simulated| State transitions and demo time advancement
Resolution verification| Implemented in demo| Configured photo and location evidence checks
Hindi localization| Deferred| Future accessibility enhancement
Advanced escalation ladder| Deferred| Multi-level operational escalation

---

⚠️ Limitations and Safety

CivicIQ is a demonstration platform, not a production municipal decision system.

- Causality is not proven: Correlation and dependency rules generate hypotheses, not confirmed physical root causes.
- Vision is limited: Deterministic image lookup is not equivalent to a general-purpose computer vision model.
- GPS is not proof of resolution: Location proximity cannot establish that infrastructure has actually been repaired.
- Impact scores require validation: Weights and thresholds are configurable demonstration assumptions, not empirically validated risk estimates.
- LLM output may be incorrect: Generated explanations require human review and supporting evidence.
- Data is synthetic: Seeded reports and fictional municipal scenarios do not demonstrate performance on real civic data.
- JSON persistence has limits: Concurrent writes, recovery, access control, and production-scale workloads require more robust infrastructure.
- No real-world dispatch: Filing, approvals, and escalation are simulated unless explicitly integrated with authorized municipal systems.

Production Readiness Checklist

Before real-world deployment, the system would require:

- Authentication, role-based access control, and audit logs.
- Secure storage and retention policies for citizen-submitted images and location data.
- Database transactions and concurrency-safe persistence.
- Real-world dataset evaluation and false-positive/false-negative analysis.
- Calibrated impact scoring and human approval for consequential actions.
- Robust image verification, anti-replay checks, and protection against manipulated evidence.
- Monitoring, retries, rate limits, and operational failure recovery.
- Accessibility, localization, and security testing.

---

🔮 Future Enhancements

- Real Computer Vision: Replace deterministic image lookup with validated image classification and damage detection models.
- Advanced Geospatial Intelligence: Incorporate road networks, drainage maps, utility networks, and geographic risk layers.
- Hindi and Regional Language Support: Enable multilingual complaints and accessible citizen interactions.
- Graph-Based Incident Intelligence: Model infrastructure dependencies and recurring incident relationships in a dedicated graph representation.
- Live Municipal Integrations: Connect authorized complaint systems, departmental APIs, and notification services.
- Improved Verification: Combine image similarity, timestamps, GPS evidence, and human review.
- Operational Analytics: Track response times, recurrence rates, resolution quality, and escalation performance.
- Production Database: Migrate JSON persistence to a transactional database and introduce background task processing.

---

🤝 Contributing

Contributions that improve reliability, explainability, usability, and testing are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes and add relevant tests.
4. Verify the backend and frontend locally.
5. Open a pull request describing the changes and their impact.

For significant changes, explain the design decision, expected behavior, and any limitations introduced.

---

📜 Project Disclaimer

CivicIQ is a fictional civic incident intelligence demonstration developed to explore multi-agent orchestration, geospatial correlation, explainable prioritization, and evidence-based resolution workflows.

All fictional city wards, synthetic citizen reports, simulated municipal filings, and demonstration outcomes are intended for educational and prototype purposes.

The system does not establish real-world infrastructure causation, guarantee repair verification, or submit official municipal records.

---

<div align="center">🏙️ CivicIQ

From isolated complaints to connected civic intelligence.

Detect the pattern. Prioritize the impact. Verify the outcome.

</div>