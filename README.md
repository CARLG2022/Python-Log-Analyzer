# Log Analysis and Detection System

## Overview
This is a Python-based log analysis tool used to scan SSH authentication logs to detect brute force attacks. It captures failed login attempts and IP addresses exceeding a treshold.

## Features
* Used regular expressions (regrex) to extract and analyze failed login attempts
* Flags suspicious IP addresses exceeding a defined failure treshold
* Outputs a summary of potential brute force attack sources

## Prerequisites 
Ensure you have the following installed: 
Python 3.x
sudo privileges (required for accessing system logs via `journalctl`) 

## Installation & Usage
Clone the repository  
git clone https://github.com/CARLG2022/Python-Log-Analyzer.git
- cd log-analysis
## Run the code
python3 ssh_log_analyzer.py 
## Example Output
Potential Brute Force Attacks Detected:

* ::1 has 29 failed login attempts!
## License 
This project is licensed under the MIT License.
  
