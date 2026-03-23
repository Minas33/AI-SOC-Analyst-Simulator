import json

def analyze_logs(file_path):
    with open(file_path, "r") as f:
        logs = f.readlines()

    results = []
    risk_score = 0

    failed_logins = {}
    
    for line in logs:
        line = line.strip().lower()

        # -----------------------------
        # BRUTE FORCE DETECTION
        # -----------------------------
        if "failed login" in line:
            ip = line.split()[-1]

            failed_logins[ip] = failed_logins.get(ip, 0) + 1

            if failed_logins[ip] == 3:
                results.append({
                    "alert": "Brute Force Attack",
                    "ip": ip,
                    "severity": "HIGH",
                    "action": "Block IP and investigate login attempts"
                })
                risk_score += 50

        # -----------------------------
        # SUSPICIOUS LOGIN
        # -----------------------------
        elif "logged in from" in line:
            location = line.split()[-1]

            if location not in ["usa", "local"]:
                results.append({
                    "alert": "Suspicious Login",
                    "location": location,
                    "severity": "MEDIUM",
                    "action": "Verify user identity and location"
                })
                risk_score += 30

        # -----------------------------
        # DATA EXFILTRATION
        # -----------------------------
        elif "large data upload" in line:
            results.append({
                "alert": "Data Exfiltration",
                "severity": "HIGH",
                "action": "Investigate data transfer and isolate system"
            })
            risk_score += 50

        # -----------------------------
        # ACCOUNT TAKEOVER SIGNAL
        # -----------------------------
        elif "password reset" in line:
            results.append({
                "alert": "Possible Account Takeover",
                "severity": "MEDIUM",
                "action": "Force password reset and review activity"
            })
            risk_score += 25

        # -----------------------------
        # UNKNOWN ADMIN ACCESS
        # -----------------------------
        elif "admin login" in line:
            results.append({
                "alert": "Unauthorized Admin Access",
                "severity": "HIGH",
                "action": "Investigate admin activity immediately"
            })
            risk_score += 60

    return results, risk_score


def print_alerts(results, risk_score):
    print("\n===== SOC ALERT REPORT =====\n")

    for r in results:
        print(f"[ALERT] {r['alert']}")
        
        if "ip" in r:
            print(f"IP: {r['ip']}")
        if "location" in r:
            print(f"Location: {r['location']}")

        print(f"Severity: {r['severity']}")
        print(f"Action: {r['action']}")
        print("-" * 30)

    print(f"\n🔥 TOTAL RISK SCORE: {risk_score}")

    if risk_score >= 100:
        print("🚨 CRITICAL: Immediate response required")
    elif risk_score >= 50:
        print("⚠️ WARNING: Investigate incidents")
    else:
        print("✅ LOW RISK")

    print("\n=============================\n")


if __name__ == "__main__":
    results, score = analyze_logs("logs.txt")
    print_alerts(results, score)import json

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
