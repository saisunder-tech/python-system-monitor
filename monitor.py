# Import required modules
import time
from datetime import datetime

# Import monitoring functions
from cpu import get_cpu_usage
from memory import get_memory_usage
from disk import get_disk_usage
from system_info import get_hostname, get_ip_address
from uptime import get_uptime
from users import get_logged_in_users

# Import logger setup function
from logger import setup_logger


# Function to collect and display system information
def monitor_system():

    print("\n==========================================")
    print("Collecting system information...\n")

    current_time = datetime.now()
    print(f"Timestamp       : {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Create logger
    logger = setup_logger()

    # CPU Usage
    cpu = get_cpu_usage()
    print(f"CPU Usage       : {cpu}%")
    logger.info(f"CPU Usage: {cpu}%")

    if cpu > 80:
        print("WARNING !! CPU usage is above 80%")
        logger.warning("CPU usage is above 80%")

    # Memory Usage
    memory = get_memory_usage()
    print(f"Memory Usage    : {memory}%")
    logger.info(f"Memory Usage: {memory}%")

    # Disk Usage
    disk = get_disk_usage()
    print(f"Disk Usage      : {disk}%")
    logger.info(f"Disk Usage: {disk}%")

    # Hostname and IP Address
    hostname = get_hostname()
    ip_address = get_ip_address()

    print(f"Hostname        : {hostname}")
    print(f"IP Address      : {ip_address}")

    logger.info(f"Hostname: {hostname}")
    logger.info(f"IP Address: {ip_address}")

    # System Boot Time
    uptime = get_uptime()
    print(f"System Boot Time: {uptime}")
    logger.info(f"System Boot Time: {uptime}")

    # Logged-in Users
    users = get_logged_in_users()

    if users:
        users_text = ", ".join(users)
    else:
        users_text = "None detected"

    print(f"Logged-in Users : {users_text}")
    logger.info(f"Logged-in Users: {users_text}")

    print("\nMonitoring completed.")
    print("Waiting 10 seconds before the next check...")
    print("==========================================\n")


# Main program
if __name__ == "__main__":

    while True:
        monitor_system()
        time.sleep(10)
