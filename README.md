# SentinelShield – Advanced Intrusion Detection & Web Protection System

SentinelShield is a lightweight Web Intrusion Detection and Monitoring System designed to analyze incoming HTTP requests and detect common web-based attacks.  
The system inspects request payloads, identifies malicious patterns using rule-based detection, logs security events, and visualizes attack statistics through an interactive dashboard.

---

## 🚀 Features

- Detects common web attacks:
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Directory Traversal
  - Local File Inclusion (LFI)
  - Command Injection
- Request inspection and payload analysis
- Rule-based attack detection using JSON signatures
- Request classification (Safe / Malicious)
- Security event logging
- Rate limiting protection
- Security monitoring dashboard with attack statistics
- Visual attack distribution using Chart.js

---

## 🏗 System Architecture

The system processes incoming requests through multiple security modules:

Client Request  
↓  
Flask Web Server (SentinelShield)  
↓  
Request Inspection Module  
↓  
Attack Detection Engine  
↓  
Request Classification  
↓  
Logging System  
↓  
Security Dashboard  

The detection engine analyzes request payloads using predefined attack patterns stored in a JSON rule file.

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Interface structure |
| CSS | UI styling |
| JavaScript | Client-side functionality |
| Chart.js | Dashboard visualization |
| JSON | Attack detection rule storage |

---

## 📂 Project Structure

```
SentinelShield/
│
├── logs/
│   └── waf.log
│
├── rules/
│   └── attack_rules.json
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
│
├── app.py
└── README.md
```

---

## 🧪 Attack Simulation Examples

The following payloads can be used to test the detection system.

| Attack Type | Example Payload |
|-------------|----------------|
| SQL Injection | `' OR 1=1--` |
| Cross-Site Scripting (XSS) | `<script>alert(1)</script>` |
| Directory Traversal | `../../` |
| Local File Inclusion | `../../etc/passwd` |
| Command Injection | `;cat /etc/passwd` |

---

## 📊 Dashboard

The SentinelShield dashboard provides a visual overview of system activity, including:

- Total requests
- Blocked requests
- Attack type distribution
- Rate limiting events

Charts are generated using **Chart.js** to help visualize security activity.

---

## 📝 Logging System

All detected attacks are recorded in the log file:

```
logs/waf.log
```

Each entry includes:

- Timestamp
- IP address
- Request payload
- Detected attack type

Example:

```
[2026-03-14] ALERT | SQL Injection | IP: 127.0.0.1 | Payload: ' OR 1=1--
```

---

## ⚡ Rate Limiting

SentinelShield includes a basic rate-limiting mechanism to prevent excessive request attempts.

Example rule:

```
10 requests within 300 seconds
```

If exceeded, the system returns **Too Many Requests**.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/SentinelShield.git
```

### 2. Navigate to the project folder

```
cd SentinelShield
```

### 3. Install dependencies

```
pip install flask
```

### 4. Run the application

```
python app.py
```

### 5. Open the browser

```
http://127.0.0.1:5000
```

---

## 📈 Results

- Successfully detected multiple simulated attack payloads.
- Logged all malicious requests for monitoring.
- Displayed attack distribution through the dashboard.
- Implemented rate limiting to prevent request abuse.

---

## 🎯 Project Purpose

This project demonstrates how basic web intrusion detection techniques can be implemented using Python and Flask.  
It highlights how rule-based detection, request inspection, logging, and monitoring dashboards can help identify suspicious web activity.

---

## 👨‍💻 Author

**Prithak Das**  
Cybersecurity Intern - Unified Mentor Private Limited

---

## 📜 License

This project is intended for **educational and learning purposes**.