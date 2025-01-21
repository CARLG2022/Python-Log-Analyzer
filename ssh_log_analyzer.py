# Author: Carl Gordon
#Date: January 19,2025
#Description: Python Log analyzer 


import re
import subprocess
from collections import defaultdict



# Run journalctl command to get SSH failed login logs
command ="sudo journalctl -u ssh --no-pager | grep 'Failed password'"
output = subprocess.run(command, shell=True, capture_output=True, text=True).stdout


# Dictionary to store failed login attempts per IP
failed_attempts = defaultdict(int)

# Regular expression pattern to extract IPs
pattern = r"Failed password for .* from ((?:\d{1,3}\.){3}\d{1,3}|[0-9a-fA-F:]+)"
# Process journalctl logs
for line in output.split("\n"):
    print("Checking log line:", line)  # Debugging each line
    match = re.search(pattern, line)
    if match:
        ip_address = match.group(1)
        failed_attempts[ip_address] += 1
        
   
# Print detected brute force attacks
THRESHOLD = 5
print("\n🔍 Potential Brute Force Attacks Detected:\n")
for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        print(f"⚠️ {ip} has {count} failed login attempts!\n")

print("\n Log Analysis Complete.")

with open("brute_force_alerts.txt", "w") as f:
    for ip, count in failed_attempts.items():
        if count > THRESHOLD:
            f.write(f"⚠️ {ip} has {count} failed login attempts!\n")
