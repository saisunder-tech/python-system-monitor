# Import the psutil library to access disk statistics.
import psutil


def get_disk_usage():
    """
    Return the percentage of disk space currently in use
    on the root (/) filesystem.
    """
    disk = psutil.disk_usage("/")
    return disk.percent


# This block runs only when this file is executed directly.
if __name__ == "__main__":
    print("Monitoring disk usage...")

    disk_usage = get_disk_usage()

    print(f"Disk Usage: {disk_usage}%")
