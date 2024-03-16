"""
Defines all helper functions
"""
import csv
import inquirer
from prettytable import PrettyTable


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


def block_user(username):
    """
    Handle Blocking user
    """
    users = []
    userFound = False
    with open('Datasets/User.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = list(reader)

        for user in users:
            if user['UserName'] == username:
                userFound = True
                user['LoginStatus'] = 'Blocked'
        if userFound:
            with open('Datasets/User.csv', 'w', newline='') as csvfile:
                fieldnames = ['UserName', 'Password', 'First Name', 'Surname', 'UserType', 'LoginStatus']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(users)

def show_logged_user(userInfo):
    """
    Displays user Full Name and user Type
    """
    table = PrettyTable()
    table.field_names = ["Full Name", "User Type"]
    fullName = f"{userInfo['First Name']} {userInfo['Surname']}"
    table.add_row([fullName, userInfo['UserType']])
    print(table)
