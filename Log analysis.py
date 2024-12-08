import re
import csv
from collections import defaultdict

# Constants
FAILED_LOGIN_THRESHOLD = 10
LOG_FILE = "C:/Users/skanda/Desktop/sample.log"  # Updated to your log file name

def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    return logs

def count_requests_per_ip(logs):
    ip_count = defaultdict(int)
    for log in logs:
        # Assuming the IP address is the first element in the log line
        ip_match = re.match(r'(\d+\.\d+\.\d+\.\d+)', log)
        if ip_match:
            ip = ip_match.group(1)
            ip_count[ip] += 1
    return ip_count

def identify_most_accessed_endpoint(logs):
    endpoint_count = defaultdict(int)
    for log in logs:
        # Assuming the endpoint is the second element in the log line
        endpoint_match = re.search(r'\"(GET|POST|PUT|DELETE) (.+?) ', log)
        if endpoint_match:
            endpoint = endpoint_match.group(2)
            endpoint_count[endpoint] += 1
    return max(endpoint_count.items(), key=lambda x: x[1], default=(None, 0))

def detect_suspicious_activity(logs):
    failed_login_count = defaultdict(int)
    for log in logs:
        if '401' in log or 'Invalid credentials' in log:
            ip_match = re.match(r'(\d+\.\d+\.\d+\.\d+)', log)
            if ip_match:
                ip = ip_match.group(1)
                failed_login_count[ip] += 1
    return {ip: count for ip, count in failed_login_count.items() if count > FAILED_LOGIN_THRESHOLD}

def output_results(ip_count, most_accessed_endpoint, suspicious_activity):
    print("IP Address           Request Count")
    for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip:<20} {count}")

    print(f"\nMost Frequently Accessed Endpoint:\n{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    print("IP Address           Failed Login Attempts")
    for ip, count in suspicious_activity.items():
        print(f"{ip:<20} {count}")

def save_results_to_csv(ip_count, most_accessed_endpoint, suspicious_activity):
    with open('log_analysis_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['IP Address', 'Request Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
            writer.writerow({'IP Address': ip, 'Request Count': count})

        writer.writerow({})  # Empty row for separation
        writer.writerow({'IP Address': 'Most Accessed Endpoint', 'Request Count': most_accessed_endpoint[0]})
        writer.writerow({'IP Address': 'Access Count', 'Request Count': most_accessed_endpoint[1]})

        writer.writerow({})  # Empty row for separation
        writer.writerow({'IP Address': 'Suspicious Activity', 'Request Count': 'Failed Login Attempts'})
        for ip, count in suspicious_activity.items():
            writer.writerow({'IP Address': ip, 'Request Count': count})

def main():
    logs = parse_log_file(LOG_FILE)
    ip_count = count_requests_per_ip(logs)
    most_accessed_endpoint = identify_most_accessed_endpoint(logs)
    suspicious_activity = detect_suspicious_activity(logs)

    output_results(ip_count, most_accessed_endpoint, suspicious_activity)
    save_results_to_csv(ip_count, most_accessed_endpoint, suspicious_activity)

if __name__ == "__main__":
    main()