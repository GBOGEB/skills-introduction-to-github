
#!/bin/bash

# Set Git global configuration
git config --global user.name "GBOGEB"
git config --global user.email "gerkotze.bonthuys@sckcen.be"

# Set Git local configuration (for the current repository)
git config user.name "GBOGEB"
git config user.email "gerkotze.bonthuys@sckcen.be"

# Verify Git configuration
git config --list

# Generate an SSH key
ssh-keygen -t ed25519 -C "gerkotze.bonthuys@sckcen.be"

# Create project folder structure
mkdir -p src tests
touch src/main.py tests/test_main.py README.md .gitignore

# Initialize a new Git repository
git init

# Add files to Git and make the first commit
git add .
git commit -m "Initial project structure and setup"

# Print completion message
echo "Project setup complete. Don't forget to add your SSH key to GitHub!"