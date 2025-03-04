import os
import subprocess
import schedule
import time
from datetime import datetime
import random

# Configuration
REPO_PATH = ""  # Change this to your repo's path
COMMIT_MESSAGE = ""
GITHUB_USERNAME = ""
GITHUB_TOKEN = ""

def make_commit():
    try:
        os.chdir(REPO_PATH)
        
        # Determine the number of commits for the day
        num_commits = random.randint(2, 10)  # Randomize between 1 and 5 commits
        for _ in range(num_commits):
            # Create or update a file to make a meaningful commit
            with open("daily_update.txt", "a") as file:
                file.write(f"Commit made on {datetime.now()}\n")
            
            # Git commands
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
            
            # Push to GitHub
            subprocess.run(
                ["git", "push", f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/BULLSHIT_CONTRIBUTION_CHART.git", "main"],
                check=True
            )
            print("Commit and push completed successfully!")
            
            # Wait for a random interval before the next commit
            time.sleep(random.randint(1, 60))  # Randomize between 1 and 60 seconds
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the task
schedule.every().day.at("13:00").do(make_commit)  # Change time as needed

print("Automated commit script is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
