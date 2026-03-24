import json

def analyze_logs(file_path):
    with open(file_path, "r") as f:
        logs = f.readlines()

    results = []
    risk_score = 0

    for line in logs:
        line = line.strip().lower()

        if "failed login" in line:
            results.append({
                "alert": "Brute Force Attempt",
                "severity": "HIGH",
                "action": "Block IP / investigate source"
            })
            risk_score += 40

        elif "login from new location" in line:
            results.append({
                "alert": "Suspicious Login",
                "severity": "MEDIUM",
                "action": "Verify user identity and location"
            })
            risk_score += 25

        elif "large data transfer" in line:
            results.append({
                "alert": "Possible Data Exfiltration",
                "severity": "HIGH",
                "action": "Investigate transfer and isolate host"
            })
            risk_score += 50

    return results, risk_score

def print_alerts(results, risk_score):
    print("\n===== SOC ALERT REPORT =====\n")

    if not results:
        print("No threats detected.")
    else:
        for r in results:
            print(f"[ALERT] {r['alert']}")
            print(f"Severity: {r['severity']}")
            print(f"Action: {r['action']}")
            print("-" * 30)

    print(f"\nTOTAL RISK SCORE: {risk_score}")

    if risk_score >= 80:
        print("STATUS: HIGH RISK")
    elif risk_score >= 30:
        print("STATUS: MEDIUM RISK")
    else:
        print("STATUS: LOW RISK")

def generate_summary(results, risk_score):
    summary = {
        "total_alerts": len(results),
        "risk_score": risk_score,
        "alerts": results
    }
    with open("report.json", "w") as f:
        json.dump(summary, f, indent=4)

if __name__ == "__main__":
    results, score = analyze_logs("logs.txt")
    print_alerts(results, score)
    generate_summary(results, score)
