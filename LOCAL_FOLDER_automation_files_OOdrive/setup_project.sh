#!/bin/bash

# Ensure the script stops on errors
set -e

# Create project structure
mkdir -p src tests modules
touch src/__init__.py src/main.py tests/test_main.py README.md .gitignore

# Initialize a new Git repository
git init

# Install ruff for linting
python -m pip install ruff

# Run ruff to lint the project
ruff check .

# Add files to Git and make the first commit
git add .
git commit -m "Initial project structure and setup"

# Push to GitHub
git remote add origin git@github.com:GBOGEB/your-repo-name.git
git branch -M main
git push -u origin main

# Print completion message

echo "✅ Project setup, linting, and push to GitHub completed!"

