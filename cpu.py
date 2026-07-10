# Import the psutil library.
# It provides functions to access system information such as CPU, memory, and disk usage.
import psutil


def get_cpu_usage():
    """
    Measure the CPU utilization over a 1-second interval
    and return it as a percentage.
    """
    return psutil.cpu_percent(interval=1)


# The code inside this block runs only when this file
# is executed directly (for example: python cpu.py).
# It does not run if this file is imported by another module.
if __name__ == "__main__":
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%")
    