# Student and Module System - Console Application
This is a Console Application for Managing Modules and Students. It provides a Command Line Interface (CLI) through which users can interact with using text commands. The application retrieves and stores its data in a CSV file.

### Features

#### General User Features
These are features that are common to both Student and Lecturer.
1. View User Profile
2. View all Modules
3. Change Password

#### Student's Features
1. View my modules
2. Register a module
3. Withdraw from a module

#### Lecturer's Features
1. Create a module
2. Update Student's records

### Getting started
1. Clone the repository
```
git clone https://github.com/wamae-ndiritu/Student_module_console_app.git
```
2. Navigate to the project directory
```
cd Student_module_console
```
3. Create a virtual environment
```
python3 -m venv venv
```
4. Activate virtual environment
On Linux
```
source venv/bin/activate
```
On Windows
```
Scripts/bin/activate
```
5. Install dependencies
```
pip install -r requirements.txt
```
6. Run the application
```
python console.py
```

### Project files
| File                                                 | Description                                        |
|------------------------------------------------------|----------------------------------------------------|
| [console.py](./console.py)                           | Main entry point of the program                    |
| [Lecturer.py](./Lecturer.py)                         | Contains all functions for the Lecturer user type. |
| [Student.py](./Student.py)                           | Contains all functions for the Student user type   |
| [Helpers.py](./Helpers.py)                           | Contains all helper functions                      |
| [Auth.py](./Auth.py)                                 | Contains function for authenticating user          |
| [Datasets/User.csv](./Datasets/User.csv)             | CSV file containing users data                     |
| [Datasets/Module.csv](./Datasets/Module.csv)         | CSV file containing modules data                   |
| [Datasets/UserModule.csv](./Datasets/UserModule.csv) | CSV file containing users modules data             |


## Unit Testing
As a part of the assignment task, we were required to pick one function in the above Console application and use it to write a well documented test for 5 test cases

### create_module Function

The `create_module` function is responsible for creating a new row in the Module.csv file, representing a new module.

| Test Case                | Description                               | Expected Output                                        |
|--------------------------|-------------------------------------------|--------------------------------------------------------|
| Valid Input              | Inputting a new course code and name      | "Module created successfully!"                        |
|                          | that do not already exist in the dataset  |                                                        |
| Duplicate Course Code    | Inputting a course code that already      | "A module with that ModuleID or ModuleName already     |
|                          | exists in the dataset                      | exists!"                                               |
| Duplicate Course Name    | Inputting a course name that already      | "A module with that ModuleID or ModuleName already     |
|                          | exists in the dataset                      | exists!"                                               |
| Empty Course Code        | Inputting an empty course code            | "Course code cannot be empty. Module creation failed." |
| Empty Course Name        | Inputting an empty course name            | "Course name cannot be empty. Module creation failed." |


## Encryption
Additionally, we were to demostrate how user data can be encrypted before storing them.

### Simple Console Application for Encrypting Passwords

This Python program is a console application designed to encrypt passwords using the Vigenère Cipher. It prompts the user to input their first name, last name, username, and password, then encrypts the password using the Vigenère Cipher and stores the encrypted user data in a CSV file named "user_encrypted.csv".

Follow the prompts to input user data:
- First name
- Last name
- Username
- Password

After providing the required information, the program will encrypt the password using the Vigenère Cipher and store the encrypted data in a CSV file named "user_encrypted.csv" in the same directory.

### File Structure

- [`vigenere_cipher_encryption.py`](./vigenere_cipher_encryption.py): Python script containing the console application for encrypting passwords.
- [`user_encrypted.csv`](./user_encrypted.csv): CSV file to store the encrypted user data.

