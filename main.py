from api import fetch_all_users_data
from last_seen_formatter import format_last_seen
from localization import translate

def fetch_users():
    return fetch_all_users_data()

def format_user_info(user, lang):
    username = user.get('nickname')
    first_name = user.get('firstName')
    last_name = user.get('lastName')
    last_seen = user.get('lastSeen')

    if last_seen is not None:
        last_seen_formatted = translate(format_last_seen(last_seen), lang)
    else:
        last_seen_formatted = translate("Never", lang)

    return f"{username} ({first_name} {last_name}) - Last seen: {last_seen_formatted}"

def display_users_info(lang):
    users_data = fetch_users()
    for user in users_data:
        print(format_user_info(user, lang))

if __name__ == "__main__":
    print("Select a language: [en] English, [uk] Українська, [ar] العربية, [fr] Français")
    lang = input("Enter the language code (e.g., en, uk, ar, fr): ").strip().lower()
    if lang not in ['en', 'uk', 'ar', 'fr']:
        print("Invalid language selection. Defaulting to English.")
        lang = 'en'
    display_users_info(lang)
