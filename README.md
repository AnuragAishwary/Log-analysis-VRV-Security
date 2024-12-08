VRV Security Python Intern Assignment: Log Analysis Script
Project Overview
This project is a Python script designed for analyzing server log files to extract critical insights. The script performs tasks such as identifying request counts per IP address, detecting the most frequently accessed endpoint, and flagging suspicious activity like potential brute-force login attempts. This assignment is part of an evaluation process for a Python internship at VRV Security, a global leader in AI-driven cybersecurity solutions.

Features
The script includes the following core functionalities:
1.
Request Counts Per IP Address:
2.
1.Parses log files to count the number of requests made by each IP address.
2.Displays results sorted in descending order of request counts.
3.
Most Frequently Accessed Endpoint:
4.
1.Identifies the endpoint accessed the highest number of times.
2.Outputs the endpoint name and its access count.
5.
Suspicious Activity Detection:
6.
1.Flags IP addresses involved in excessive failed login attempts (e.g., HTTP 401 errors).
2.Allows configuration of the threshold for failed attempts (default: 10).
7.
Output Results:
8.
1.Displays findings in a well-organized terminal output.
2.Saves results to a structured CSV file named log_analysis_results.csv.

Requirements
Software and Libraries
Python 3.7+
Libraries: 
ocsv
ocollections
ore (for regex parsing)
Install dependencies (if required) using:
pip install -r requirements.txt
Hardware
Minimum: Any system capable of running Python 3.7 or higher.
Recommended: A modern system with sufficient RAM for processing larger log files.

Usage
1. Clone the Repository
git clone https://github.com/your-username/log-analysis-script.git
cd log-analysis-script
2. Provide Input Log File
Save the log file (e.g., sample.log) in the project directory.
3. Run the Script
Execute the script using:
python log_analysis.py
4. View Results
Terminal Output: Displays request counts, most accessed endpoint, and flagged suspicious IPs.
CSV Output: Results saved in log_analysis_results.csv with the following structure: 
oRequests per IP: IP Address, Request Count
oMost Accessed Endpoint: Endpoint, Access Count
oSuspicious Activity: IP Address, Failed Login Count

Example Output
Terminal Output
Requests Per IP:
IP Address           Request Count
192.168.1.1          7
203.0.113.5          11
10.0.0.2             6
...

Most Frequently Accessed Endpoint:
/home (Accessed 9 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
192.168.1.100        12
203.0.113.5          11
CSV File Structure
IP Address	Request Count
192.168.1.1	7
203.0.113.5	11
Endpoint	Access Count
/home	9
IP Address	Failed Login Count
192.168.1.100	12
203.0.113.5	11

Configuration
You can configure the script by modifying the following constants at the top of log_analysis.py:
Failed Login Threshold: Default is 10. Adjust as needed: 
FAILED_LOGIN_THRESHOLD = 10


Project Structure
log-analysis-script/
│
├── sample.log               # Sample log file
├── log_analysis.py          # Main script
├── requirements.txt         # Dependencies (if any)
└── README.md                # Project documentation

Development & Contribution
Contributions are welcome! Follow these steps to contribute:
1.Fork the repository.
2.Create a feature branch: git checkout -b feature-name.
3.Commit your changes: git commit -m "Feature description".
4.Push to the branch: git push origin feature-name.
5.Open a pull request.

Contact
For any queries or feedback, please reach out to VRV Security at info@vrvsecurity.com.

License
This project is licensed under the MIT License. See the LICENSE file for details.
