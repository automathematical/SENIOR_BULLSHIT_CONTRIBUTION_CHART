# 🚀 BULLSHIT_CONTRIBUTION_CHART  
### *Because green squares make us feel productive, right?*

Welcome to the most gloriously pointless — yet oddly satisfying — GitHub automation tool you'll ever add to your dev toolkit.  
Let’s be real: sometimes you just want your GitHub profile to *look* like you’ve been grinding, even if you’ve been binge-watching tutorials or doing “deep research” on YouTube.

This project is for **vibe coders** only 😎.  
Yes, it makes **daily commits**. Yes, it's **automated**. And yes, it’s absolutely **ridiculous** — in the best way possible.

---

## 💻 What Does It Do?

**Automatically commits to a GitHub repo every single day.**

**Why?**  
To make your contribution chart look *busy af*, even when you’re deep in thought (or deep in snacks).

---

## 🧠 How It Works

Under the hood, it’s a simple Python script using [`schedule`](https://pypi.org/project/schedule/) to run daily. It:

- Makes a change (or just re-commits something silly)  
- Commits it with a message like “Daily automated commit”  
- Pushes to GitHub using your personal access token  

> Just enough effort to fake the hustle 👀

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/BULLSHIT_CONTRIBUTION_CHART.git
```

### 2. Edit the Config in `main.py`

```python
REPO_PATH = "/path/to/your/repo"
COMMIT_MESSAGE = "Daily automated commit"
GITHUB_USERNAME = "your_username"
GITHUB_TOKEN = "your_personal_access_token"
```

> 💡 **Pro tip:** Store your token securely using environment variables  
> (seriously, don’t push your secrets to GitHub — we’re not *that* chaotic)

```python
import os
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
```

### 3. Install Dependencies

```bash
pip install schedule
```

### 4. Run It

```bash
python main.py
```

Or go full auto-mode with a **cron job (macOS/Linux)** or **Task Scheduler (Windows)**.

---

## 🕒 Setting Up a Cron Job on macOS

Want this to run *every day at 10AM*? Easy:

### Step 1: Open the Terminal

```bash
crontab -e
```

### Step 2: Add This Line

```bash
0 10 * * * /usr/bin/python3 /path/to/your/script.py
```

> 🕘 This means it’ll run daily at **10:00 AM**.

### Step 3: Make the Script Executable

```bash
chmod +x /path/to/your/script.py
```

### Step 4: Check Your Cron Jobs

```bash
crontab -l
```

### Step 5: View Cron Logs (Optional)

```bash
log show | grep cron
```

---

## ⚠️ Security Note

**DO NOT** hardcode your GitHub token like a noob.  
Use `.env` files, secrets managers, or at least `os.getenv()`.

---

## 🧃 Vibe On

If you’re a productivity hacker, a chart chaser, or just someone who appreciates a well-populated contribution graph — this one’s for you.

And hey, if you actually want to *do* something meaningful with your automation… you do you. But this repo? This is just for **fun, flair, and fakery**.

---

## 🧑‍💻 Built with sarcasm by @automathematical (https://github.com/automathematical)  
Pull requests welcome — especially if they automate *more bullshit*.

---
