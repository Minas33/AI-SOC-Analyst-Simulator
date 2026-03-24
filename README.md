# 🛡️ AI-SOC-Analyst-Simulator
🚀 AI-powered SOC (Security Operations Center) simulator...
## 🚀 Features
- Detects brute force attacks
- Identifies suspicious logins (location anomalies)
- Detects possible data exfiltration
- Assigns severity levels (LOW / MEDIUM / HIGH)
- Provides recommended SOC actions
- Generates structured JSON report
## 🧠 Example Output
```bash
[ALERT] Brute Force Attempt
Severity: HIGH
Action: Block IP / investigate source

[ALERT] Suspicious Login
Severity: MEDIUM
Action: Verify user identity and location

[ALERT] Possible Data Exfiltration
Severity: HIGH
Action: Investigate transfer and isolate host

TOTAL RISK SCORE: 155
STATUS: HIGH RISK

## 🔥 Overview

This project simulates how a real SOC analyst thinks and responds to security alerts.

It reads log data, identifies suspicious behavior, classifies incidents, assigns severity, and suggests what to do next — just like a real cybersecurity analyst.

---

## ⚡ Features

- Detects brute force attacks
- Detects suspicious logins (impossible travel, anomalies)
- Detects potential data exfiltration
- Assigns severity levels (Low / Medium / High)
- Calculates overall risk score
- Provides recommended response actions
- Outputs structured JSON results (real-world format)

---

## 🧠 How It Works

1. Reads logs from a file (`logs.txt`)
2. Analyzes each line for patterns
3. Matches indicators of compromise (IOCs)
4. Assigns severity + risk score
5. Generates structured results

---

## 📂 Project Structure

AI-SOC-Analyst-Simulator/
│
├── soc_analyzer.py     # Main detection engine
├── logs.txt            # Sample log input
└── README.md           # Project documentation

---

## 🧪 Example Input (logs.txt)

Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
User logged in from Russia
Large data upload detected

---

## 📊 Example Output

[
  {
    "type": "Brute Force Attack",
    "severity": "High",
    "recommendation": "Block IP and investigate login attempts"
  },
  {
    "type": "Suspicious Login",
    "severity": "Medium",
    "recommendation": "Verify user identity and location"
  },
  {
    "type": "Data Exfiltration",
    "severity": "High",
    "recommendation": "Investigate data transfer and isolate system"
  }
]

---

## 🛠️ How to Run

python3 soc_analyzer.py

---

## 📈 Real-World Skills Demonstrated

- SOC alert triage
- Threat detection & classification
- Incident response thinking
- Log analysis
- Risk scoring methodology
- Security automation (Python)

---

## 🎯 Why This Project Matters

This project demonstrates practical, job-ready cybersecurity skills.

It shows how an analyst:
- Detects attacks
- Prioritizes threats
- Makes decisions under pressure
- Responds to incidents

---

## 🚀 Future Improvements (Already Included in Design)

- Real-time log monitoring
- SIEM integration (Splunk, Elastic)
- MITRE ATT&CK mapping
- Web dashboard (alerts + metrics)
- Machine learning anomaly detection
- Export reports (JSON / PDF)
- API integration
- Expanded detections (phishing, malware, lateral movement)

---

## 🧑‍💻 Author

Minas Fretzagias  
AI Security | Red Teaming | SOC Analysis

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and follow for more AI + Cybersecurity projects.
