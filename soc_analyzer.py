import json

def analyze_logs(file_path):
    with open(file_path, "r") as f:
        logs = f.readlines()

    incidents = []
    risk_score = 0

    for line in logs:
        line = line.strip().lower()

        if "failed login" in line:
            incidents.append({
                "type": "Brute Force Attempt",
                "severity": "High",
                "response": "Block IP, enforce account lockout policy"
            })
            risk_score += 3

        elif "login from new location" in line:
            incidents.append({
                "type": "Suspicious Login",
                "severity": "Medium",
                "response": "Trigger MFA, verify user identity"
            })
            risk_score += 2

        elif "large data transfer" in line:
            incidents.append({
                "type": "Possible Data Exfiltration",
                "severity": "Critical",
                "response": "Investigate traffic, isolate system"
            })
            risk_score += 5

    return {
        "total_incidents": len(incidents),
        "risk_score": risk_score,
        "details": incidents
    }


if __name__ == "__main__":
    result = analyze_logs("logs.txt")
    print(json.dumps(result, indent=4))
