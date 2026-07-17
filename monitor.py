# Import required modules
import os
import time
from datetime import datetime

# Load environment variables from .env
from dotenv import load_dotenv

# Import monitoring functions
from cpu import get_cpu_usage
from memory import get_memory_usage
from disk import get_disk_usage
from system_info import get_hostname, get_ip_address
from uptime import get_uptime
from users import get_logged_in_users

# Import logger setup function
from logger import setup_logger

# Load variables from .env
load_dotenv()

# Read configuration values
CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 80))
MONITOR_INTERVAL = int(os.getenv("MONITOR_INTERVAL", 10))


def monitor_system():
    """
    Collect and display system information.
    """

    # Create logger
    logger = setup_logger()

    print("\n==========================================")
    print("Collecting system information...\n")

    current_time = datetime.now()
    print(f"Timestamp       : {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # CPU Usage
    cpu = get_cpu_usage()
    print(f"CPU Usage       : {cpu}%")
    logger.info(f"CPU Usage: {cpu}%")

    if cpu > CPU_THRESHOLD:
        warning_message = (
            f"WARNING !! CPU usage is above {CPU_THRESHOLD}%"
        )
        print(warning_message)
        logger.warning(warning_message)

    # Memory Usage
    memory = get_memory_usage()
    print(f"Memory Usage    : {memory}%")
    logger.info(f"Memory Usage: {memory}%")

    # Disk Usage
    disk = get_disk_usage()
    print(f"Disk Usage      : {disk}%")
    logger.info(f"Disk Usage: {disk}%")

    # Hostname
    hostname = get_hostname()
    print(f"Hostname        : {hostname}")
    logger.info(f"Hostname: {hostname}")

    # IP Address
    ip_address = get_ip_address()
    print(f"IP Address      : {ip_address}")
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
    print(f"Waiting {MONITOR_INTERVAL} seconds before the next check...")
    print("==========================================\n")


# Main Program
if __name__ == "__main__":

    logger = setup_logger()

    try:
        while True:

            try:
                monitor_system()

            except Exception as error:
                print("\nERROR: Unable to collect system information.")
                print("Continuing monitoring...\n")

                logger.exception(f"Unexpected error: {error}")

            time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping Python System Monitor...")
        print("Goodbye!")

        logger.info("Application stopped by user.")
