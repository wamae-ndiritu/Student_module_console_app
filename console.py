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
    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option

from prettytable import PrettyTable

def view_modules():
    with open('Datasets/Module.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Create a pretty table
        table = PrettyTable()
        table.field_names = ["ModuleID", "ModuleName"]

        # Add rows from the CSV
        for row in reader:
            table.add_row([row['ModuleID'], row['ModuleName']])

        # Print the table
        print(table)
    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option


def select_menu_options(message="", choices=[]):
    """
    Displays menu options and handles the selection of option
    Args:
        message (str): The title message for the select menu
        choices (list): List of menu options
    Return:
        int: Returns an int representing the selected option.
    """
    questions = [
            inquirer.List('option',
                message=message,
                choices=choices,
                carousel=True
                ),
            ]
    answer = inquirer.prompt(questions)
    return int(answer['option'][0])


def main():
    welcome()
    attempts = 0
    while attempts < 3:
        username, password = login()
        data, success = authenticate(username, password)
        if success:
            print("Login successful!")
            while True:
                selected_option = select_menu_options(
                        "Select from the menu below", 
                        [
                            '1. View user profile',
                            '2. View all modules',
                            '3. Change password',
                            '4. Exit'
                        ]
                    )

                if selected_option == 1:
                    exit_option = view_user_profile(data)
                    if exit_option == 1:
                        continue
                elif selected_option == 2:
                    exit_option = view_modules()
                    if exit_option == 1:
                        continue
                elif selected_option == 3:
                    change_password()
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
