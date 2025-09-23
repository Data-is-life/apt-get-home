import os
import subprocess
import random
from datetime import datetime

# === CONFIG ===
REPO_PATH = "/Users/mohitgangwani/Documents/GitHub/apt-get-home/src"  # CHANGE THIS
TARGET_FILE = "daily_log.txt"

def write_to_file(path):
    with open(path, "a") as f:
        f.write(f"{datetime.now().isoformat()} - Mi nombre es Senor Mojito\n")

def git_commit_and_push():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "update - testing new code"], check=True)
    subprocess.run(["git", "push"], check=True)

def main():
    os.chdir(REPO_PATH)
    write_to_file(TARGET_FILE)
    git_commit_and_push()

if __name__ == "__main__":
    if random.random() < 0.6:  # Only commit 60% of the time for realism
        main()
