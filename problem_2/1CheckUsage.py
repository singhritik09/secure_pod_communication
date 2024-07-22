import psutil
import logging
from datetime import datetime

logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 70 
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"High CPU usage detected: {cpu_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert_message = f"High memory usage detected: {memory_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert_message = f"High disk usage detected: {disk_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_running_processes():
    process_count = len(psutil.pids())
    PROCESS_COUNT_THRESHOLD = 200
    if process_count > PROCESS_COUNT_THRESHOLD:
        alert_message = f"High number of running processes detected: {process_count}"
        print(alert_message)
        logging.warning(alert_message)

def main():
    print(f"System Health Check started at {datetime.now()}")
    logging.info(f"System Health Check started at {datetime.now()}")
    
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
