# Import the socket module.
# It allows us to communicate with the operating system's networking features.
import socket


def get_hostname():
    """
    Return the hostname (computer name) of the current machine.
    """
    return socket.gethostname()


def get_ip_address():
    """
    Return the IP address associated with the current machine.
    """
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


# This block runs only when this file is executed directly.
if __name__ == "__main__":
    print("Monitoring network information...")

    hostname = get_hostname()
    ip_address = get_ip_address()

    print(f"Hostname  : {hostname}")
    print(f"IP Address: {ip_address}")

    