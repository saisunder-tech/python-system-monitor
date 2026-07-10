# Import the required modules.
# psutil provides the system boot time.
# datetime helps us convert timestamps into readable dates and times.
import psutil
from datetime import datetime


def get_uptime():
    """
    Return the system boot time as a human-readable string.
    """
    boot_time = psutil.boot_time()
    return datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")


# This block runs only when this file is executed directly.
if __name__ == "__main__":
    print("Monitoring system uptime...")

    uptime = get_uptime()

    print(f"System boot time: {uptime}")

    