
# Project 1: AI Cyber Log Analyzer

This project is a local AI-assisted cybersecurity log analysis tool built with Python and Ollama.

The tool reads suspicious security logs, extracts IP indicators using Python, sends the log evidence to a locally hosted LLM, and generates a structured SOC-style incident triage report.

## What This Project Does

- Reads suspicious log entries from a text file
- Extracts IP addresses using regular expressions
- Sends the logs to a local LLM through Ollama
- Generates an AI-assisted incident triage report
- Saves the report with timestamp, model name, and extracted indicators

## Tools and Technologies

- Python
- Ollama
- Mistral 7B local LLM
- Regular expressions
- Local file handling
- Cybersecurity log analysis

## Project Files

```text
project-1-ai-cyber-log-analyzer/
├── ai_log_analyzer.py
├── suspicious_logs.txt
├── ai_analysis_report.txt
└── README.md
