# AI-RealTime-SOC-Simulator

🚀 A Python-based real-time SOC simulation tool that continuously generates security events, detects suspicious behavior, updates risk scores, and triggers automated responses such as monitoring or blocking suspicious IP addresses.

---

## Overview

This project simulates how a Security Operations Center (SOC) monitors live activity and reacts to threats in real time.

The system continuously generates simulated security events such as:
- failed logins
- suspicious logins from risky locations
- possible data exfiltration

As activity is analyzed, the simulator:
- increases a dynamic risk score
- classifies overall risk level
- triggers automated responses
- logs alert activity to a file

---

## Features

- Real-time event simulation
- Detection of suspicious login activity
- Detection of brute force behavior
- Detection of possible data exfiltration
- Dynamic risk scoring
- Automated response logic (monitor / block)
- Alert logging to `alerts.log`

---

## How It Works

1. The simulator generates security events continuously  
2. Each event is analyzed  
3. Risk score increases based on suspicious behavior  
4. The system classifies risk as LOW, MEDIUM, or HIGH  
5. Automated responses are triggered:
   - monitor suspicious IPs  
   - block high-risk IPs  
6. Alerts are written to `alerts.log`  

---

## Example Output

```bash
[ALERT] Possible data exfiltration from 203.0.113.10
Current Risk Score: 80
STATUS: MEDIUM RISK ⚠️
[AUTO RESPONSE] Monitoring IP: 203.0.113.10

[ALERT] Brute force attempt from 10.0.0.3
Current Risk Score: 110
STATUS: HIGH RISK 🚨
[AUTO RESPONSE] Blocking IP: 10.0.0.3
