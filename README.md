# Python-RCE-Simulation-Tool
A technical simulation of Remote Code Execution(RCE) via insecure system calls in Python environments. This edeucational Proof of Concept(PoC) demonstrates the critical importance of input sanitization in web-based command execution scenarios
Python Remote Code Execution (RCE) Simulation Tool
​This repository contains a technical Proof of Concept (PoC) demonstrating Insecure Command Injection vulnerabilities within Python-based web environments.
​ DISCLAIMER
​THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING PURPOSES ONLY. The author is not responsible for any misuse, illegal activities, or damage caused by this program. Use it only on systems you own or have explicit permission to test. [cite: 2026-03-26]
​ Vulnerability Analysis
​The simulation highlights the risks of Insecure Deserialization. It demonstrates how unsanitized JSON payloads passed directly to system-level calls (e.g., os.system) can lead to full Remote Code Execution (RCE). In this scenario, an attacker can manipulate the command key to execute arbitrary OS commands.

Installation & Execution
git clone https://github.com/[YOUR_USERNAME]/Python-RCE-Simulation-Tool.git
Ensure you have the necessary environment
Run the localhost
func start
Trigger the exploit using the following curl 
curl -X POST http://localhost:7071/api/ExploitTrigger \
     -H "Content-Type: application/json" \
     -d '{"command": "calc"}'
     Expected Result
​If the system is vulnerable, the calc [cite: 2026-03-26] command inside the JSON payload will be processed by the OS, triggering the local calculator (e.g., gnome-calculator) as a proof of successful code execution.
