# 👋 START HERE: How to Open, Set Up and Begin

This page is written **like I'm explaining to a 5-year-old**. No step is too small.

---

## Part 1: What is this thing and how do I open it?

### 🧒 The 5-year-old version
Think of **GitHub** as a **big online cupboard**. Your cupboard is called **`Project-Hammad`**.
Inside the cupboard there are **shelves** called **branches**.
- The **`main`** shelf is the one everybody sees first.
- Claude put all the new plans on a **different shelf** called **`claude/dreamy-curie-sn7l15`**, so nothing on your main shelf got messy.

So if you open your cupboard and don't see the new files, it's because **you're looking at the wrong shelf.**

### Way 1: Read it in your web browser (easiest, works on phone too)
1. Open this link: **https://github.com/Hammados07/Project-Hammad/tree/claude/dreamy-curie-sn7l15**
2. You'll see folders: **`growth-plan`**, **`mba-ai-ds`** and this file **`START-HERE.md`**.
3. Tap any file ending in **`.md`**. GitHub shows it as a nice, formatted page.
4. If you open the normal repo page and don't see the files: tap the button that says **`main`** (top-left, above the file list) and choose **`claude/dreamy-curie-sn7l15`**.

### Way 2: Move everything onto your `main` shelf (recommended, do it once)
Then the files show up by default whenever you open your repo.
1. Open **https://github.com/Hammados07/Project-Hammad**
2. GitHub usually shows a yellow bar: **"claude/dreamy-curie-sn7l15 had recent pushes"**. Click **Compare & pull request**. (No yellow bar? Go to the **Pull requests** tab → **New pull request** → *base:* `main`, *compare:* `claude/dreamy-curie-sn7l15`.)
3. Click **Create pull request**, then **Merge pull request**, then **Confirm merge**.
4. Done. Everything is now on `main`. *(You can also just ask Claude to open the pull request for you.)*

> 🧒 A **pull request** is like saying: *"Please take the toys from that shelf and put them on the main shelf."* **Merge** means *"Yes, do it."*

### Way 3: Get the files onto your laptop
- **Simple:** On the branch page, click the green **`<> Code`** button → **Download ZIP** → unzip it.
- **Better (keeps in sync):** Install **GitHub Desktop** (free, https://desktop.github.com) → *File → Clone repository* → pick `Project-Hammad`. Use the branch dropdown to switch shelves. Click **Fetch origin** any time to get new updates.

### Way 4: On your phone
Install the **GitHub** app (Android/iOS), log in, open `Project-Hammad`, tap the branch name and choose the Claude branch. Good for reading on your commute.

---

## Part 2: What's in the cupboard? (map)

```
Project-Hammad/
├── START-HERE.md            ← you are here
├── growth-plan/             ← side income, money split, schedule, content & book playbooks
│   ├── README.md
│   ├── 01-content-and-books-playbook.md
│   ├── 02-schedule-and-timetable.md
│   ├── 03-upskill-timetable.md
│   ├── 04-project-roadmap.md
│   └── weekly-timetable.ics ← import into Google Calendar (see Part 4)
├── mba-ai-ds/               ← YOUR MBA REBUILD COURSE (4 semesters, 28 modules)
│   ├── README.md            ← how the course works + 48-week timetable
│   ├── how-to-learn-fast.md ← memory tricks, study method
│   ├── semester-1.md … semester-4.md
│   ├── business-acumen.md
│   ├── free-resources.md
│   ├── youtube-teaching-kit.md
│   └── labs/                ← Python, R, SQL practice code + datasets
├── Task1…Task5 *.sql        ← your SQL projects
└── screenshots/
```

**Reading order:** this file → `mba-ai-ds/README.md` → `mba-ai-ds/how-to-learn-fast.md` → `growth-plan/02-schedule-and-timetable.md` → `mba-ai-ds/semester-1.md`.

---

## Part 3: Setup Week ("Week 0"): 7 small jobs, ~45 min each

Do **one job per day**. Tick each box as you go (in your own copy or notebook).

### Day 1: Accounts (the "keys")
- [ ] **GitHub** (you have it). Install the GitHub app on your phone.
- [ ] **Google account** for learning & channel (can be your existing one).
- [ ] **SWAYAM / NPTEL**: https://swayam.gov.in and https://onlinecourses.nptel.ac.in (free IIT/IIM courses)
- [ ] **Kaggle**: https://www.kaggle.com (free datasets, free Python notebooks, free mini-courses)
- [ ] **Posit Cloud**: https://posit.cloud (run R in the browser, free tier)

> 🧒 Accounts are like library cards. You need the card before you can borrow books.

### Day 2: Zero-install coding (start here, no setup pain)
- [ ] Open **Google Colab**: https://colab.research.google.com → *New notebook*.
- [ ] Type `print("Hello Hammad")` in the box → press **Shift + Enter**. You just ran Python. 🎉
- [ ] Get the lab files into Colab. Pick one:
  - **Copy-paste (always works):** open a lab file on GitHub (e.g. `mba-ai-ds/labs/python/01_python_basics.py`), copy one `# %%` block at a time into a Colab cell and run it.
  - **One command (works if your repo is public):** run this in a Colab cell:
    ```
    !git clone -b claude/dreamy-curie-sn7l15 https://github.com/Hammados07/Project-Hammad
    %cd Project-Hammad/mba-ai-ds/labs
    %run python/01_python_basics.py
    ```
    (Once you've merged into `main`, you can drop the `-b claude/dreamy-curie-sn7l15` part.)

> 🧒 Colab is a computer Google lends you inside your browser. Nothing to install and nothing breaks.

### Day 3: Laptop tools (for later, when you want your own setup)
- [ ] **VS Code**: https://code.visualstudio.com (the notebook where you write code). Add the *Python* and *Jupyter* extensions.
- [ ] **Python**: https://www.python.org/downloads (tick **"Add Python to PATH"** on Windows). Then in a terminal: `pip install pandas numpy matplotlib scikit-learn statsmodels scipy jupyter`
- [ ] **R + RStudio**: https://cran.r-project.org then https://posit.co/download/rstudio-desktop
- [ ] **PostgreSQL + pgAdmin**: https://www.postgresql.org/download (you used this for Tasks 1–5)
- [ ] **Power BI Desktop** (Windows, free from Microsoft Store)

### Day 4: Your "second brain" (notes + memory)
- [ ] **Notes app:** Notion or Obsidian (both free). Make one page per module: *"M1 – How a Business Works"*.
- [ ] **Anki** (free flashcards, https://apps.ankiweb.net): the app that makes you *remember*. See `mba-ai-ds/how-to-learn-fast.md`.
- [ ] A **physical notebook** for drawing concepts. Drawing helps memory.

### Day 5: Put the timetable in your calendar
- [ ] Do **Part 4** below (import the calendar file).
- [ ] Put your phone on **Do Not Disturb** during study blocks.

### Day 6: Content setup (don't post yet)
- [ ] Create your YouTube channel + Instagram professional account (steps in `growth-plan/01-content-and-books-playbook.md`).
- [ ] Record a 1-minute test video on your phone to check sound and light.

### Day 7: Rest + read
- [ ] Read `mba-ai-ds/README.md` and `how-to-learn-fast.md`.
- [ ] Write **why you're doing this** on one page. Read it when motivation drops.

---

## Part 4: Put the timetable into Google Calendar (5 minutes)

The file **`growth-plan/weekly-timetable.ics`** contains your whole weekly routine as repeating calendar events (India time).

1. Download it: open the file on GitHub → click **Download raw file** (⬇ icon).
2. On a **laptop/desktop** (the phone app can't import): open https://calendar.google.com
3. Recommended: first make a new calendar called **"Growth Plan"** (*Settings ⚙ → Add calendar → Create new calendar*), so you can hide or delete it in one click.
4. *Settings ⚙ → Import & export → Import* → choose `weekly-timetable.ics` → pick the **"Growth Plan"** calendar → **Import**.
5. Open the Google Calendar app on your phone. The events and reminders are there.

**Shifts change?** Drag the events to new times, or edit one and choose *"This and following events"*.

---

## Part 5: Your very first learning week (Week 1)

| Day | Time | Do this |
|---|---|---|
| Mon | 60 min | Read **Module 1** in `mba-ai-ds/semester-1.md`. Watch the first free lecture listed |
| Tue | 60 min | Make 10 Anki cards from Module 1. Draw the "business machine" diagram from memory |
| Wed | 60 min | Open `mba-ai-ds/labs/python/01_python_basics.py` in Colab, run it cell by cell |
| Thu | 60 min | Start **Module 2** (accounting). Pick a company and find its annual report |
| Fri | 60 min | Explain Module 1 out loud for 5 minutes, recorded on your phone. That's your first practice video! |
| Sat | 2–3 hrs | Finish Module 2 + its self-test. Repo: commit your notes (optional) |
| Sun | 30 min | Weekly review (see `growth-plan/02-schedule-and-timetable.md`) |

That's it. **Don't try to do everything at once.** One module at a time, one day at a time. 🌱
