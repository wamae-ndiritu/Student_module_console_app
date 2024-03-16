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

