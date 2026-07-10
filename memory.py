# Import the psutil library to access memory statistics.
import psutil


def get_memory_usage():
    """
    Return the percentage of RAM currently in use.
    """
    memory = psutil.virtual_memory()
    return memory.percent


# This block runs only when this file is executed directly.
if __name__ == "__main__":
    print("Monitoring RAM usage...")

    memory_usage = get_memory_usage()

    print(f"Memory Usage: {memory_usage}%")

    