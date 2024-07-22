import re
from collections import Counter

def analyze_logs(log_data):
    log_pattern = re.compile(
        r'(?P<ip>[\d\.]+) - - \[.*\] ".*" (?P<status>\d{3}) .*'
    )
    
    status_counts = Counter()
    page_requests = Counter()
    ip_requests = Counter()

    for line in log_data.splitlines():
        match = log_pattern.match(line)
        if match:
            status = match.group('status')
            ip = match.group('ip')
            
            status_counts[status] += 1
            ip_requests[ip] += 1
            
            try:
                page_path = line.split('"')[1].split(' ')[1]
                page_requests[page_path] += 1
            except IndexError:
                continue

    report = {
        '404_errors': status_counts.get('404', 0),
        'most_requested_pages': page_requests.most_common(5),
        'ip_with_most_requests': ip_requests.most_common(5),
    }
    return report

with open('logs.log', 'r') as file:
    log_data_from_file = file.read()

report = analyze_logs(log_data_from_file)

print("Report Summary:")
print(f"Number of 404 errors: {report['404_errors']}")
print("Most Requested Pages:")
for page, count in report['most_requested_pages']:
    print(f"  {page}: {count} requests")
print("IP Addresses with Most Requests:")
for ip, count in report['ip_with_most_requests']:
    print(f"  {ip}: {count} requests")
