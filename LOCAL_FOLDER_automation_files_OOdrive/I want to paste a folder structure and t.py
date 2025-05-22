# Folder structure diagram (commented out to avoid syntax errors)
# ├── src/
# │   ├── main.py
# ├── tests/
# │   ├── test_main.py
# ├── README.md
# ├── .gitignore

# Replace the above diagram with valid Python code or comments.
from logging import config


print("Ensure your script contains valid Python syntax.")


# Set globally
import subprocess

# Set git config globally
subprocess.run(["git", "config", "--global", "user.name", "GBOGEB"])
subprocess.run(["git", "config", "--global", "user.email", "gerkotze.bonthuys@sckcen.be"])

# Set locally (in the current repository)
subprocess.run(["git", "config", "user.name", "GBOGEB"])
subprocess.run(["git", "config", "user.email", "gerkotze.bonthuys@sckcen.be"])
subprocess.run(["git", "config", "--list"])
subprocess.run(["git", "config", "--list"])

subprocess.run(["git", "config", "--list"])

# subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", "gerkotze.bonthuys@sckcen.be"])