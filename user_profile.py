import sys

def display_user_profile(username, first_name, surname, user_type, login_status):
    print("User Profile:")
    print("─────────────────────────────────────")
    print(f"Username:     {username}")
    print(f"First Name:   {first_name}")
    print(f"Surname:      {surname}")
    print(f"User Type:    {user_type}")
    print(f"Login Status: {login_status}")
    print("─────────────────────────────────────")

if __name__ == "__main__":
    # Extract user data from command-line arguments
    username, first_name, surname, user_type, login_status = sys.argv[1:]
    display_user_profile(username, first_name, surname, user_type, login_status)
    input("Press Enter to return to the main page...")
