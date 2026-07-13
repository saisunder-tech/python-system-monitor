# Import Python's built-in logging module.
import logging


def setup_logger():
    """
    Create and configure a logger that writes messages to system.log.
    """
    logging.basicConfig(
        filename="system.log",      # Name of the log file.
        level=logging.INFO,         # Record INFO messages and above.
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)


# This block runs only when logger.py is executed directly.
if __name__ == "__main__":
    print("Configuring the logger...")

    logger = setup_logger()

    logger.info("Logger initialized successfully.")

    print("A test message has been written to system.log")
