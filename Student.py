"""
Defines all functions of a Student in the MSS
"""
import csv
import inquirer
from Helpers import select_menu_options


def register_module(username):
    """
    Creates a new row in the UserModule.csv file
    Args:
        username (str): Unique key for the new row to be created
    Return:
        (int): Exit option
    """
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
    """
    Delete a Module from the UserModule.csv file.
    Args:
        username (str): Unique key for finding the row in the csv file
    Return:
        int: Exit option
    """
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
