# Ensure the file is located at:
# C:/Users/gbonthuy/Documents/ProjectStarterPack/# Project Starter Pack_generic_repo_1805.py

# Project Starter Pack

# This project includes automation and configuration files to get started quickly.

# Bash Commands

# Run the following commands in your terminal to initialize the project:

# Initialize a new Git repository
# git init

# Create the project structure
# mkdir src tests
# touch src/__init__.py src/main.py tests/test_main.py README.md .gitignore

# Add files to Git and make the first commit
# git add .
# git commit -m "Initial project structure and setup"

# src/main.py

# Create the main Python file for the project.

# Main entry point for the project

def main():
    print("Hello, Project Starter Pack!")

if __name__ == "__main__":
    main()

# tests/test_main.py

# Create the test file for `main.py`.

# Test file for main.py

import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Navigate to your project root directory
project_path = r'C:\Users\gbonthuy\OneDrive - Studiecentrum voor Kernenergie\Documents\GitHub\LOCAL_FOLDER_automation_files_OOdrive'
if os.path.exists(project_path):
    os.chdir(project_path)
else:
    print(f"Error: The directory '{project_path}' does not exist.")
    exit(1)

# Ensure proper Python package structure
# touch src/__init__.py

# Run the main application
# python -m src.main

# Run the tests
# python -m unittest tests/test_main.py

# If you're having import issues, you can also try running tests with PYTHONPATH set
# PYTHONPATH=. python -m unittest tests/test_main.py

class TestMain(unittest.TestCase):
    def test_main_output(self):
        # Capture the output of the main function
        with self.assertLogs() as captured:
            main()
        self.assertIn("Hello, Project Starter Pack!", captured.output[0])

if __name__ == "__main__":
    unittest.main(exit=False)  # Prevent unittest from exiting the program

# .gitignore

# Add the following entries to the `.gitignore` file:

# Byte-compiled files
# __pycache__/

# Environment files
# .env

# Test coverage reports
# .coverage
