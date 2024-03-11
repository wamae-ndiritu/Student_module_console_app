#!/usr/bin/python3

import csv
import inquirer

def welcome():
    print("Welcome to the Module and Student System (MSS)")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def authenticate(username, password):
    """
    Authenticates the username/password passed by the user.
    Return:
        An empty dict {}, if invalid credentials
        Or a dict with user info.
    """
    with open('./Datasets/User.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        error = {}
        user = {}
        for row in reader:
            if row['UserName'] == username:
                user = row
        if user:
            if user['Password'] == password:
                return user, True
            else:
                error['message'] = "Invalid password!"
        else:
            error['message'] = "Invalid username!"
        return error, False

def view_user_profile(user):
    print("User Profile:")
    print("─────────────────────────────────────")
    print(f"Username:     {user['UserName']}")
    print(f"First Name:   {user['First Name']}")
    print(f"Surname:      {user['Surname']}")
    print(f"User Type:    {user['UserType']}")
    print(f"Login Status: {user['LoginStatus']}")
    print("─────────────────────────────────────")
    questions = [
            inquirer.List('option',
                message="Go Back to main menu:",
                choices=['1. Main menu'],
                carousel=True
                ),
            ]
    answer = inquirer.prompt(questions)
    selected_option = int(answer['option'][0])
    return selected_option

def select_menu():
    questions = [
            inquirer.List('option',
                message="Select from the menu below:",
                choices=['1. View user profile', '2. View all modules', '3. Change password', '4. Exit'],
                carousel=True
                ),
            ]
    answer = inquirer.prompt(questions)
    return answer


def main():
    welcome()
    attempts = 0
    while attempts < 3:
        username, password = login()
        data, success = authenticate(username, password)
        if success:
            print("Login successful!")
            print(data)
            while True:
                answer = select_menu()
                selected_option = int(answer['option'][0])

                if selected_option == 1:
                    choice = view_user_profile(data)
                    if choice == 1:
                        continue
                elif selected_option == 4:
                    break # Exit the inner loop and return to login page
            break
        else:
            print(data["message"])
            attempts += 1
    else:
        print("You've exceeded the maximum number of login attempts. Your account is blocked.")

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print()
