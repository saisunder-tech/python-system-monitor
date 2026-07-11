# Import psutil to access information about logged-in users.
import psutil


def get_logged_in_users():
    """
    Return a list of usernames currently logged in.
    """
    users = psutil.users()
    return [user.name for user in users]


# This block runs only when this file is executed directly.
if __name__ == "__main__":
    print("Monitoring logged-in users...")

    users = get_logged_in_users()

    if users:
        print("Logged-in users:")
        for user in users:
            print(f"- {user}")
    else:
        print("No users are currently logged in.")
        