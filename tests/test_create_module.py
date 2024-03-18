import unittest
import shutil
import os
from unittest.mock import patch
from io import StringIO
from Lecturer import create_module


class TestCreateModule(unittest.TestCase):
    def setUp(self):
        shutil.copy2('Datasets/Module.csv', 'Datasets/Module_backup.csv')
        self.fake_out = StringIO()
        print(self.fake_out.getvalue())

    def tearDown(self):
        os.remove('Datasets/Module.csv')
        os.rename('Datasets/Module_backup.csv', 'Datasets/Module.csv')
        # Reset the StringIO buffer after each test case
        self.fake_out.seek(0)
        self.fake_out.truncate(0)
    
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', side_effect=given_answer),  patch('sys.stdout', new=self.fake_out):
            create_module()
            self.assertEqual(self.fake_out.getvalue().strip(), expected_out)

    def test_create_valid_inputs(self):
        self.runTest(["CSCI101", "Introduction to Computer Science"], "Create a new module\nModule created successfully!")

    def test_create_duplicate_course_code(self):
        self.runTest(["317", "Management Information Systems II"], "Create a new module\nA module with that ModuleID or ModuleName already exists!")

    def test_create_duplicate_course_name(self):
        self.runTest(["3171", "Management Information Systems"], "Create a new module\nA module with that ModuleID or ModuleName already exists!")

    def test_create_module_empty_code(self):
        self.runTest([" ", "Introduction to Biology"], "Create a new module\nCourse code or name cannot be empty. Module creation failed.")

    def test_create_module_empty_coursename(self):
        self.runTest(["402", " "], "Create a new module\nCourse code or name cannot be empty. Module creation failed.")

if __name__ == '__main__':
    unittest.main()
