from flask import Flask, request, render_template
import datetime
import json
import os

app = Flask(__name__)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
RULES_PATH = os.path.join(BASE_DIR, "rules", "attack_rules.json")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "waf.log")

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Load attack rules
try:
    with open(RULES_PATH) as f:
        attack_rules = json.load(f)
except FileNotFoundError:
    attack_rules = {}

# Track requests per IP
ip_requests = {}

# Rate limiting settings
MAX_REQUESTS = 10
TIME_WINDOW = 300


# Logging function
def write_log(message):
    timestamp = datetime.datetime.now()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

    print("LOG:", message)


# Attack detection
def detect_attack(query):

    if not query:
        return None

    for attack_type, patterns in attack_rules.items():
        for pattern in patterns:
            if pattern.lower() in query.lower():
                return attack_type

    return None


# Rate limiting check
def check_rate_limit(ip):

    now = datetime.datetime.now()

    if ip not in ip_requests:
        ip_requests[ip] = []

    ip_requests[ip] = [
        t for t in ip_requests[ip]
        if (now - t).total_seconds() < TIME_WINDOW
    ]

    ip_requests[ip].append(now)

    request_count = len(ip_requests[ip])

    print(f"IP {ip} request count:", request_count)

    if request_count > MAX_REQUESTS:
        return True

    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():

    user = request.args.get("user", "").strip()
    ip = request.remote_addr
    raw_query = request.query_string.decode()

    # Rate limit check
    if check_rate_limit(ip):

        write_log(f"BLOCKED | Rate Limit | IP: {ip}")

        return render_template(
            "result.html",
            status="rate_limit"
        )

    # Block empty input
    if not user:

        write_log(f"BLOCKED | Empty Input | IP: {ip}")

        return render_template(
            "result.html",
            status="invalid",
        )

    # Attack detection
    attack = detect_attack(user)

    if attack:

        write_log(f"ALERT | {attack} | IP: {ip} | Payload: {raw_query}")

        return render_template(
            "result.html",
            status="attack",
            attack=attack
        )

    # Normal request
    write_log(f"ALLOWED | IP: {ip} | Query: {raw_query}")

    return render_template(
        "result.html",
        status="allowed",
        user=user
    )


# Dashboard route
@app.route("/dashboard")
def dashboard():

    total = 0
    blocked = 0
    attacks = 0
    rate_limit = 0

    sql = 0
    xss = 0
    traversal = 0
    lfi = 0
    command = 0

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, encoding="utf-8") as f:

            for line in f:

                total += 1

                if "BLOCKED" in line:
                    blocked += 1

                if "Rate Limit" in line:
                    rate_limit += 1

                if "ALERT" in line:
                    attacks += 1

                if "SQL Injection" in line:
                    sql += 1

                if "XSS" in line:
                    xss += 1

                if "Directory Traversal" in line:
                    traversal += 1

                if "LFI" in line:
                    lfi += 1

                if "Command Injection" in line:
                    command += 1

    return render_template(
        "dashboard.html",
        total=total,
        blocked=blocked,
        attacks=attacks,
        rate_limit=rate_limit,
        sql=sql,
        xss=xss,
        traversal=traversal,
        lfi=lfi,
        command=command
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)