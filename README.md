# Python Automation & Infrastructure Foundations

**This repository serves as a practical engineering logbook and code portfolio documenting my transition into cloud automation, systems scripting, and DevOps engineering. It tracks my progression from core scripting syntax to writing robust, defensive automation utilities designed to interface with infrastructure payloads.**

## Core Technical Competencies Developed
* **Systems I/O & Stream Handling:** Utilizing Python context managers (`with open`) for memory-efficient file reading and writing operations.
* **Structured Data Architectures:** Navigating, filtering, and manipulating complex multi-layered objects (nested Lists and Key-Value Dictionaries).
* **Data Serialization & API Alignment:** Parsing and validating raw JSON payloads mimicking cloud infrastructure API outputs.
* **Defensive Engineering & Fault Tolerance:** Implementing robust `try/except/else` blocks to handle malformed data and missing attributes safely without crashing deployment pipelines.

---

## Repository Directory Structure & Submissions

### 1. Project Setup & Remote Pipeline Configuration
* **Directory:** Root
* **Objective:** Establish an automated environment linking a local Ubuntu development machine (`nickubuntu`) to a public GitHub repository using secure personal access tokens via the command line.
* **Key Command Line Workflow:**
  ```bash
  git remote -v
  git status
  git add .
  git commit -m "feat: initialize automation codebase"
  git push origin main

### 2. Log File Analysis Engine
* Script: log_parser.py

* Objective: Read and scrub system event logs dynamically.

* Core Concepts: String manipulation, whitespace stripping (.rstrip()), sequential data streaming, and programmatic file discovery.

### 3. Infrastructure Inventories
* Script: infrastructure_inventory.py

* Objective: Store, append, and access server target profiles dynamically.

* Core Concepts: Managing ordered sequences (Lists) via .append() versus mapping attributes using Key-Value pairs (Dictionaries). Handled f-string quote nesting to prevent syntax collisions during terminal status reporting.

### 4. Security Compliance Fleet Auditor
* Script: inventory_auditor.py

* Objective: Iterate through an inline array of dictionaries simulating a small server fleet to isolate out-of-compliance OS builds.

* Core Concepts: Multi-layered loops (for server in server_fleet), variable mapping versus string evaluation, and conditional logic filtering.

### 5. Cloud Payload JSON Parser
* Script: json_parser.py

* Objective: Ingest, parse, and unpack a multi-line JSON string payload mirroring a real-world cloud API infrastructure output.

* Core Concepts: Leveraging the built-in json standard library, deserializing text streams with json.loads(), and drilling down into nested JSON arrays using explicit square-bracket keys (parsed_data['hosts']).

### 6. Robust Exception Tracker
* Script: robust_parser.py

* Objective: Intentionally feed malformed payloads and invalid keys to an engine to test operational robustness.

* Core Concepts: Graceful error handling using explicit except json.JSONDecodeError and except KeyError traps, avoiding the anti-pattern of bare exceptions to ensure clear execution visibility.

### Capstone Project: Automated Cloud Readiness Auditor
* Directory: hour-09-capstone/

* Scripts/Assets: cloud_auditor.py, raw_inventory.txt, migration_report.txt

* The Scenario
Prior to executing a mass migration to AWS, the migration team requires a utility to scrub a raw local system inventory file (raw_inventory.txt). The dataset is unstable, containing corrupted syntax strings and missing hardware parameters.

**Technical Implementation**
* The cloud_auditor.py engine orchestrates all foundational Python concepts into a single, cohesive utility:

* Streams the inventory file line-by-line using a context manager.

* Defensively attempts to parse records using json.loads(); logs malformed strings to a failure counter without breaking execution.

* Quantifies explicit target boundaries: ensures keys exist and filters assets dynamically based on compliance thresholds (Minimum 2 CPU cores AND 8GB RAM).

* Pipes the successful objects to an array and writes a clean, formatted deployment artifact (migration_report.txt) complete with newline parameters (\n) and an iterative list of approved cloud hostnames.

* Sample Output Artifact (migration_report.txt):

==============================
AWS MIGRATION READINESS REPORT
==============================
Total Eligible Servers: 2
Total Malformed Records Skipped: 1

The following servers are cleared for AWS migration:
- prod-web-01 (production)
- test-cache-01 (testing)