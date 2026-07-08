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

### 7. AWS First Contact & API Authentication
* **Script:** `aws_test_connect.py`
* **Objective:** Establish a secure, programmatic connection from a local virtual machine to Amazon Web Services to audit cloud storage infrastructure.

**Milestones Accomplished:**
* **Identity & Access Management (IAM):** Provisioned a dedicated, non-root automation user following the principle of least privilege, restricting access solely to programmatic CLI/API interactions.
* **Secure Environment Configuration:** Bound the local VM to AWS securely using local access keys via `aws configure` to avoid hardcoding credentials.
* **Terminal-Driven Provisioning:** Bypassed AWS Console UI limitations by utilizing the `aws s3api` CLI to programmatically spin up a globally unique storage asset in `us-east-1`.
* **SDK Implementation:** Developed an automated discovery script utilizing `boto3` to hit the global AWS endpoint, unpack the metadata payload, and map active S3 buckets.

#### Execution Verification:
```text
(.venv) nick@nickubuntu:~/python-projects-basics$ python3 aws_test_connect.py
[INFO]: Connecting to AWS API...

=== Active S3 Storage Buckets Found ===
- nick-p-validation-77129
```

### 8. S3 Data Ingestion & Object Telemetry Engine
* **Script:** `aws_s3_archiver.py`
* **Objective:** Programmatically ship local infrastructure state logs to cloud storage and parse object registries using the AWS API.

**Milestones Accomplished:**
* **File Stream Migration:** Utilized the Boto3 `.upload_file()` abstraction layer to transfer a local system asset (`backup_log.txt`) to a remote target bucket.
* **API Response Harvesting:** Captured the complex nested dictionary return payload from `list_objects_v2()`.
* **Defensive Dictionary Traversing:** Implemented a structural check (`if 'Contents' in objects_payload`) to protect the looping logic from breaking if evaluated against an empty cloud bucket directory.
* **Key Mapping:** Iterated through target objects to isolate and extract the precise metadata string identifiers (`obj['Key']`).

### 9. Automated Local-to-Cloud Fleet Archiver
* **Script:** `aws_fleet_backup.py`
* **Objective:** Execute automated directory sweeps across local server infrastructure, construct platform-agnostic file paths, and stream sequential data assets to AWS S3.

**Milestones Accomplished:**
* **Dynamic Directory Ingestion:** Utilized Python's `os.listdir()` to dynamically inventory target directories without hardcoding explicit filename assets.
* **Cross-Platform Path Stability:** Implemented `os.path.join()` to safely handle local directory-to-file paths, preventing path delimiter failures across differing operating system kernels.
* **Deterministic Object Key Mapping:** Engineered dynamic string concatenation logic to append unique file identifiers to explicit cloud path prefixes (`"fleet_backups/" + filename`), avoiding key collisions and unintended object overwrites during iterative loop streams.

---

### 10. Decoupled Cloud Compute Provisioner
* **Script:** `aws_ec2_provisioner.py`
* **Objective:** Programmatically orchestrate virtual hardware allocation and virtual machine lifecycle deployment via API infrastructure blueprints.

**Milestones Accomplished:**
* **API Blueprint Modeling:** Bypassed traditional web console UI dependencies by using the Boto3 EC2 client to compile compute parameters natively in code.
* **Hardware Sizing & Operating System Selection:** Successfully targeted specific geographic Amazon Machine Images (AMIs) for Ubuntu 24.04 LTS and provisioned burstable instance architectures (`t3.micro`).
* **Multi-Service Security Escalation:** Successfully identified, tracked, and isolated cross-service privilege blocks (`UnauthorizedOperation`) by updating AWS IAM identity policies from storage-only scopes to full compute administrative permissions (`AmazonEC2FullAccess`).
* **Free Tier Credit Safeguards:** Configured explicit `CreditSpecification` parameters within the launch payload to lock compute cycles into 'standard' evaluation modes, mitigating unexpected infrastructure billing.
* **Asynchronous Payload Parsing:** Captured the complex returned launch dictionary data stream, target-filtering the array to isolate, extract, and print the live cloud `InstanceId` directly to the terminal console.