from api import fetch_all_users_data
from last_seen_formatter import format_last_seen

def display_users_info():
    users_data = fetch_all_users_data()
    for user in users_data:
        username = user.get('nickname')
        first_name = user.get('firstName')
        last_name = user.get('lastName')
        last_seen = user.get('lastSeen')

        if last_seen is not None:
            last_seen_formatted = format_last_seen(last_seen)
        else:
            last_seen_formatted = "Never"

        print(f"{username} ({first_name} {last_name}) - Last seen: {last_seen_formatted}")


if __name__ == "__main__":
    display_users_info()
