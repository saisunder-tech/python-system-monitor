# Import the functions we created in the previous modules.
from cpu import get_cpu_usage
from memory import get_memory_usage
from disk import get_disk_usage
from system_info import get_hostname, get_ip_address
from uptime import get_uptime
from users import get_logged_in_users


print("Collecting system information...\n")

cpu = get_cpu_usage()
print(f"CPU Usage       : {cpu}%")

# Display a warning if CPU usage is high.
if cpu > 80:
    print("WARNING !! CPU usage is above 80%")

print(f"Memory Usage    : {get_memory_usage()}%")
print(f"Disk Usage      : {get_disk_usage()}%")
print(f"Hostname        : {get_hostname()}")
print(f"IP Address      : {get_ip_address()}")
print(f"System Boot Time: {get_uptime()}")

users = get_logged_in_users()
if users:
    print("Logged-in Users : " + ", ".join(users))
else:
    print("Logged-in Users : None detected")

    