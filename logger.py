# Import Python's built-in logging module.
import logging
import os

# Load variables from .env
from dotenv import load_dotenv

load_dotenv()


def setup_logger():
    """
    Create and configure a logger that writes messages
    based on values stored in the .env file.
    """

    log_file = os.getenv("LOG_FILE", "system.log")
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    return logging.getLogger(__name__)


if __name__ == "__main__":
    print("Configuring the logger...")

    logger = setup_logger()

    logger.info("Logger initialized successfully.")

    print("A test message has been written.")
