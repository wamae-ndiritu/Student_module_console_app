"""
Defines all functions common among the Student and Lecturer
"""
import csv
import getpass
from prettytable import PrettyTable
from Helpers import select_menu_options


def view_user_profile(user):
    """
    Displays the profile info of the logged in user.
    """
    table = PrettyTable()
    table.field_names = ["Attribue", "Value"]
    for key, value in user.items():
        if key != 'Password':
            table.add_row([key, value])
    print("MY PROFILE")
    print(table)
    selected_option = select_menu_options("Go Back to main menu", ['1. Main menu'])
    return selected_option

def view_modules():
    """
    Displays all the registered Modules
    Return:
        int: Exit option
    """
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
    """
    Displays all User Modules
    Args:
        username (str): Username of the current logged in user.
    Return:
        int: Exit option
    """
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


def change_password(username):
    """
    Update the Password column in the User.csv for a specified row
    Args:
        username (str): The value for the UserName column.
    Return:
        (int): Exit option.
    """
    data = []
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

