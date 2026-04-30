import subprocess
import re
from datetime import datetime

LOG_FILE = "suspicious_logs.txt"
OUTPUT_FILE = "ai_analysis_report.txt"
MODEL_NAME = "mistral:7b"


def read_log_file(file_path):
    print("[+] Reading suspicious log file...")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_ip_addresses(log_text):
    print("[+] Extracting IP indicators from logs...")
    ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log_text)
    return sorted(set(ip_addresses))


def analyze_logs_with_ai(log_text, extracted_ips):
    print("[+] Sending logs to local AI model for analysis...")

    prompt = f"""
Act as a professional SOC analyst.

The following suspicious IP addresses were pre-detected by Python:
{', '.join(extracted_ips)}

Analyze the following security logs and generate a structured cybersecurity incident triage report.

Your report must include:
1. Executive Summary
2. Likely Attack Techniques
3. Analysis of the Suspicious IP Addresses
4. Severity Rating (Low / Medium / High)
5. Recommended Response Actions

Security Logs:
{log_text}
"""

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace"
    )

    return result.stdout

def clean_ai_output(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def save_report(report_text, output_file, extracted_ips):
    print("[+] Saving AI analysis report...")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("AI CYBERSECURITY INCIDENT TRIAGE REPORT\n")
        file.write(f"Generated: {timestamp}\n")
        file.write(f"Model Used: {MODEL_NAME}\n")
        file.write("=" * 60 + "\n\n")

        file.write("PRE-EXTRACTED IP INDICATORS:\n")
        for ip in extracted_ips:
            file.write(f"- {ip}\n")

        file.write("\n" + "=" * 60 + "\n\n")
        file.write(report_text)


logs = read_log_file(LOG_FILE)
ips = extract_ip_addresses(logs)
raw_analysis = analyze_logs_with_ai(logs, ips)
analysis = clean_ai_output(raw_analysis)
save_report(analysis, OUTPUT_FILE, ips)

print("[+] Analysis complete.")
print(f"[+] Report saved to {OUTPUT_FILE}")
