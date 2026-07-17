import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration values
CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 80))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "system.log")
MONITOR_INTERVAL = int(os.getenv("MONITOR_INTERVAL", 10))
