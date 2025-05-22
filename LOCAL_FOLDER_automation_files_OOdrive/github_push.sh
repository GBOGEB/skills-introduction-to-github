#!/bin/bash

# Ensure the script stops on errors
set -e

# Add all changes to the staging area
git add .

# Commit the changes with a message
commit_message="Automated commit: $(date)"
git commit -m "$commit_message"

# Push the changes to the GitHub repository
git push origin main

# Print completion message
echo "✅ Changes pushed to GitHub successfully!"
