# Import the monitoring functions from the modules we created.
from datetime import datetime
from cpu import get_cpu_usage
from memory import get_memory_usage
from disk import get_disk_usage
from system_info import get_hostname, get_ip_address
from uptime import get_uptime
from users import get_logged_in_users

# Import the function that configures the logger.
from logger import setup_logger


# This block runs only when monitor.py is executed directly.
if __name__ == "__main__":
    print("Collecting system information...\n")

    current_time = datetime.now()
    print(f"Timestamp       : {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create and configure the logger.
    logger = setup_logger()

    # Get and display CPU usage.
    cpu = get_cpu_usage()
    print(f"CPU Usage       : {cpu}%")
    logger.info(f"CPU Usage: {cpu}%")

    # Print and log a warning if CPU usage is high.
    if cpu > 80:
        print("WARNING !! CPU usage is above 80%")
        logger.warning("CPU usage is above 80%")

    # Get and display memory usage.
    memory = get_memory_usage()
    print(f"Memory Usage    : {memory}%")
    logger.info(f"Memory Usage: {memory}%")

    # Get and display disk usage.
    disk = get_disk_usage()
    print(f"Disk Usage      : {disk}%")
    logger.info(f"Disk Usage: {disk}%")

    # Get and display hostname and IP address.
    hostname = get_hostname()
    ip_address = get_ip_address()
    print(f"Hostname        : {hostname}")
    print(f"IP Address      : {ip_address}")
    logger.info(f"Hostname: {hostname}")
    logger.info(f"IP Address: {ip_address}")

    # Get and display the system boot time.
    uptime = get_uptime()
    print(f"System Boot Time: {uptime}")
    logger.info(f"System Boot Time: {uptime}")

    # Get and display logged-in users.
    users = get_logged_in_users()
    if users:
        users_text = ", ".join(users)
    else:
        users_text = "None detected"

    print(f"Logged-in Users : {users_text}")
    logger.info(f"Logged-in Users: {users_text}")
