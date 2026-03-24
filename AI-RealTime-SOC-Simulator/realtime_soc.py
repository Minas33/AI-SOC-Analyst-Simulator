import time
import random

# Simulated IPs and locations
ips = ["192.168.1.5", "10.0.0.3", "172.16.0.8", "203.0.113.10"]
locations = ["US", "RU", "CN", "DE", "BR"]

risk_score = 0

def generate_log():
    event_type = random.choice(["login", "failed_login", "data_transfer"])
    ip = random.choice(ips)
    location = random.choice(locations)

    return {
        "event": event_type,
        "ip": ip,
        "location": location
    }

def analyze_log(log):
    global risk_score

    if log["event"] == "failed_login":
        print(f"[ALERT] Brute force attempt from {log['ip']}")
        risk_score += 30

    elif log["event"] == "login" and log["location"] in ["RU", "CN"]:
        print(f"[ALERT] Suspicious login from {log['location']} ({log['ip']})")
        risk_score += 20

    elif log["event"] == "data_transfer":
        print(f"[ALERT] Possible data exfiltration from {log['ip']}")
        risk_score += 40

def show_status():
    print(f"Current Risk Score: {risk_score}")

    if risk_score > 100:
        print("STATUS: HIGH RISK 🚨")
    elif risk_score > 50:
        print("STATUS: MEDIUM RISK ⚠️")
    else:
        print("STATUS: LOW RISK ✅")

print("Starting Real-Time SOC Simulator...\n")

while True:
    log = generate_log()
    analyze_log(log)
    show_status()
    print("-" * 40)
    time.sleep(2)
