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
    with open('Datasets/User.csv', newline='') as csvfile:
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
    print("My Profile")
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
        print("ALL REGISTERED MODULES")
        print(table)
    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option

def view_user_modules(username):
    modules_list = []
    with open('Datasets/UserModule.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['UserName'] == username:
                modules_list.append(row['ModuleID'])
    with open('Datasets/Module.csv', newline='') as csvfile:
        user_modules = []
        reader = csv.DictReader(csvfile)
        user_modules_table = PrettyTable()
        user_modules_table.field_names = ["ModuleID", "ModuleName"]

        for row in reader:
            if row['ModuleID'] in modules_list:
                user_modules_table.add_row([row['ModuleID'], row['ModuleName']])

        # Print user modules
        print("CURRENTLY ENROLLED MODULES")
        print(user_modules_table)

    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option

def register_module(username):
    registered_modules_list = []
    user_modules = []
    with open('Datasets/UserModule.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        user_modules = list(reader)
        for row in user_modules:
            if row['UserName'] == username:
                registered_modules_list.append(row['ModuleID'])

    modules = []
    with open('Datasets/Module.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        modules = list(reader)

    questions = [
            inquirer.List('module',
                message="Select Module to register",
                choices=[f"{module['ModuleID']} {module['ModuleName']}" for module in modules],
                carousel=True
                ),
            ]
    answer = inquirer.prompt(questions)
    moduleId = answer['module'].split(' ')[0]
    if moduleId in registered_modules_list:
        print(f"Module with the code {moduleId} is already registered!")
    else:
        new_user_module = {
                'UserName': username,
                'ModuleID': moduleId
                }
        user_modules.append(new_user_module)
        # Write the updated data back to the CSV file
        try:
            with open('Datasets/UserModule.csv', 'w', newline='') as csvfile:
                fieldnames = ['UserName', 'ModuleID']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(user_modules)
            print(f"You have successfully registered to {answer['module']}!")
        except:
            print(f"An error occurred trying to regster {answer['module']}!")

    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option

def withdraw_module(username):
    registered_modules_codes = []
    registered_modules = []
    modules = []
    with open('Datasets/UserModule.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        modules = list(reader)
        for row in modules:
            if row['UserName'] == username:
                registered_modules_codes.append(row['ModuleID'])

    with open('Datasets/Module.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        course_modules = list(reader)
        for row in course_modules:
            if row['ModuleID'] in registered_modules_codes:
                registered_modules.append(row)
    questions = [
            inquirer.List('module',
                message="Select Module to withdraw from",
                choices=[f"{module['ModuleID']} {module['ModuleName']}" for module in registered_modules],
                carousel=True
                ),
            ]
    answer = inquirer.prompt(questions)
    moduleId = answer['module'].split(' ')[0]

    new_modules = []
    for row in modules:
        if row['UserName'] != username:
            new_modules.append(row)
        else:
            if row['ModuleID'] != moduleId:
                new_modules.append(row)

    # Write the updated data back to the CSV file
    try:
        with open('Datasets/UserModule.csv', 'w', newline='') as csvfile:
            fieldnames = ['UserName', 'ModuleID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_modules)
        print(f"You have successfully withdrawn from {answer['module']}!")
    except:
        print(f"An error occurred trying to withdraw {answer['module']}!")

    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option



import getpass

def change_password(username):
    # Read the CSV file and load its contents into memory
    with open('Datasets/User.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Find the user record based on the provided username
    user_found = False
    for user in data:
        if user['UserName'] == username:
            user_found = True
            break

    if not user_found:
        print(f"User '{username}' not found.")
        return False

    # Prompt the user to enter the new password and confirm it
    while True:
        new_password = getpass.getpass("Enter new password: ")
        confirm_password = getpass.getpass("Confirm new password: ")

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            user['Password'] = new_password
            break

    # Write the updated data back to the CSV file
    with open('Datasets/User.csv', 'w', newline='') as csvfile:
        fieldnames = ['UserName', 'Password', 'First Name', 'Surname', 'UserType', 'LoginStatus']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("Your password has been reset successfully!")
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
                choice_list = []
                if data['UserType'] == 'Student':
                    choice_list = [
                            '1. View user profile',
                            '2. View all modules',
                            '3. Change password',
                            '4. View my modules',
                            '5. Register a module',
                            '6. Withdraw from a module',
                            '9. Exit'
                            ]
                elif data['UserType'] == 'Lecturer':
                    choice_list = [
                            '1. View user profile',
                            '2. View all modules',
                            '3. Change password',
                            '4. View my modules',
                            '7. Create a module',
                            '8. Update student records',
                            '9. Exit'
                            ]
                selected_option = select_menu_options(
                            "Select from the menu below",
                            choice_list
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
                    exit_option = change_password(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 4:
                    exit_option = view_user_modules(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 5:
                    exit_option = register_module(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 6:
                    exit_option = withdraw_module(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 9:
                    break # Exit the inner loop
                else:
                    print(selected_option)
                    break
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
