# TO DO. CLI App
#### Assignment 2 - Custom Software Application - Coder Academy


TO DO. is a fun, secure, and easy to use task management app that runs in your terminal (CLI)! Perfect for organising your day and keeping on top of tasks. Your account is stored securely, allowing you to come back to your task list when it suits you. Guest mode is also available if you're wanting to try the app before signing up (please note: tasks will not be saved in guest mode when you exit the app).

Any feedback or issues you encounter with using the app, please let me know. I hope you enjoy using TO DO. as much as I enjoyed making it!
<hr>

## Table of Contents

1. [Setup & Installation](#1-setup--installation)
   - [System Requirements](#system-requirements)
   - [Clone Repository](#clone-repository)
   - [Install Dependencies](#install-dependencies)
   - [Run the App](#run-the-app)
2. [Hardware Requirements](#2-hardware-requirements)
3. [App Features](#3-app-features)
4. [Dependencies](#4-dependencies)
   - [Purpose of Each Dependency](#purpose-of-each-dependency)
   - [Legal & Ethical Impacts](#legal--ethical-impacts)
   - [Security Impact](#security-impact)
   - [Conflicts](#conflicts)
5. [Required Files](#5-required-files)
6. [Reference List](#6-reference-list)

## 1. Setup & Installation
TO DO. will run on all major operating systems, including Windows, macOS and Linux.
For the best experience, use a dark theme in your code editor (e.g., "Visual Studio Dark" in VS Code).

1. **System Requirements**  
   - **Python:** 3.8 or newer  
   - **pip:** Python package manager (comes with Python)

   > **Tip:** Make sure `python` and `pip` commands work in your terminal. Windows users please ensure Python was added to your system PATH during installation. You can check this by running:
   > ```bash
   > python3 --version
   > pip3 --version
   > ```
   > If you see version numbers then you are good to go.

2. **Clone Repository**
   ```bash
   git clone https://github.com/lillieharlow/TO_DO._App.git
   cd TO_DO._App
   ```
3. **Install Dependencies**
   ```bash
   pip install rich pyfiglet bcrypt emoji
   ```
   Or create `requirements.txt` and manually add the dependencies (recommended for consistency):
   ```
   bcrypt==4.3.0
   emoji==2.14.1
   markdown-it-py==3.0.0
   mdurl==0.1.2
   pyfiglet==1.0.2
   Pygments==2.19.2
   rich==13.7.1
   six==1.17.0
   ```
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Sub-dependencies like `Pygments`, `markdown-it-py`, `mdurl`, and `six` are installed automatically.
<hr>

4. **Run the App**
   Start the app from the terminal:

   ```bash
   python3 todo_manager/main.py
   ```
   Follow the on-screen prompts to sign up, log in, or try the app in guest mode.
<hr>

## 2. Hardware Requirements
- **Minimum:** 512 MB RAM, 50 MB free disk space, basic CPU
- **Recommended:** 1 GB RAM+, 100 MB free disk space, terminal supporting Unicode & colors
<hr>

## 3. App Features

- Colourful CLI, enhanced with emoji and ASCII art banners for an engaging user experience. Not your average boring terminal app! 
- User data is securely stored in JSON files. With passwords hashed by bcrypt (no plain-text storage).
- Try before creating an account with 'Guest' mode. Create a temporary task lists and see how TO DO. can help you (tasks list not saved in guest mode).
- Keep track of your tasks easily! Add, view, complete, or delete tasks with clear menu options.
- Organise your tasks with priority levels: High, Medium, or Low.
<hr>

## 4. Dependencies

| Library           | Version  | Purpose                               | License      | License Info                         |
|-------------------|----------|---------------------------------------|--------------|--------------------------------------|
| bcrypt            | 4.3.0    | Password hashing (security)           | Apache 2.0   | [PyPI](https://pypi.org/project/bcrypt/) |
| emoji             | 2.14.1   | Emoji rendering in CLI                | BSD          | [PyPI](https://pypi.org/project/emoji/)  |
| rich              | 13.7.1   | CLI formatting, colors, tables        | MIT          | [PyPI](https://pypi.org/project/rich/)   |
| pyfiglet          | 1.0.2    | ASCII art banners                     | MIT          | [PyPI](https://pypi.org/project/pyfiglet/) |
| markdown-it-py    | 3.0.0    | Markdown parsing (rich dependency)    | MIT          | [PyPI](https://pypi.org/project/markdown-it-py/) |
| mdurl             | 0.1.2    | Markdown URL handling                 | MIT          | [PyPI](https://pypi.org/project/mdurl/)  |
| Pygments          | 2.19.2   | Syntax highlighting (rich dependency) | BSD          | [PyPI](https://pypi.org/project/Pygments/) |
| six               | 1.17.0   | Python 2/3 compatibility              | MIT          | [PyPI](https://pypi.org/project/six/)    |

All dependencies are open source and compatible with each other.
<hr>

**Purpose of Each Dependency**
   - **bcrypt:** Provides secure password hashing to protect user data.
   - **emoji:** Display emojis in the CLI for a fun user experience.
   - **rich:** Enhances CLI with style, colours, task table and formatting for better readability.
   - **pyfiglet:** Creates ASCII art banners to make the app pop! Visually engaging and fun.
   - **markdown-it-py, mdurl, Pygments:** Support rich text rendering and syntax highlighting used by `rich`.
   - **six:** Ensures compatibility between Python 2 and 3, used by `bcrypt`.

**Legal & Ethical Impacts**  
   - All files are created and managed by the app, no external dependencies or third-party code.
   - User data stays local and is stored securely in JSON format.
   - Only reputable open source libraries are used (MIT, Apache 2.0, BSD licenses).
   - No restrictive or copyleft licenses—safe for personal or project use and distribution.
   - No external data sharing or tracking.

- **Security Impact** 
   - User passwords are hashed (never stored as plain text).
   - All user data is stored locally and no personal data is shared externally.
   - The app has no internet connectivity requirements, further ensuring data privacy.

- **Conflicts**
   - These packages are known to be fully compatible with each other, with no conflicting versions or installation issues on the specified versions.
   - Use a virtual environment to avoid conflicts with other Python projects. Pinning versions in `requirements.txt` preserves compatibility, preventing future issues with updates.

## 5. Required Files

- `main.py` — Main entry point
- `user.py` — User account classes and authentication
- `tasks.py` — Task management classes
- `styling.py` — CLI styling
- `emoji_library.py` — Emoji codes for UI
- `utils.py` — Shared utility functions
- `data/users.json` — Stores user account info (automatically created)
- `data/{username}_tasks.json` — Per-user task storage (automatically created)
<hr>

## 6. Reference List

AIMind. (2023) *Creating a Simple To-Do List in Python*, https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814, accessed: 19 July 2025.

ComputerScience, Y. (2025) *Python To-Do List Project (For Beginners)🐍*, https://www.youtube.com/watch?v=uwaHwP3wfjY, accessed: 19 July 2025.

DrPython. (2024) *Easy Python Project for Beginners: Build a To-Do List App 2024*, https://www.youtube.com/watch?v=pY6RB4_EoSM, accessed: 22 July 2025.

GeeksforGeeks. (2018) *Python | ASCII Art Using Pyfiglet Module*, https://www.geeksforgeeks.org/python/python-ascii-art-using-pyfiglet-module/, accessed: 6 August 2025.

GeeksforGeeks. (2022) Hashing Passwords in Python with BCrypt, https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/, accessed: 1 August 2025.

GeeksforGeeks. (2025) How To Hash Passwords In Python, https://www.geeksforgeeks.org/python/how-to-hash-passwords-in-python/, accessed: 1 August 2025.

GeeksforGeeks. (2025) *Installing and Using Rich Package in Python*, https://www.geeksforgeeks.org/python/installing-and-using-rich-package-in-python/, accessed: 2 August 2025.

Halverson, S. (2023) *PythonToDo*, https://github.com/ShaunHalverson/PythonToDo, accessed: 18 July 2025.

Halverson, S. (2024) *How To Code A To Do List App In Python | Programming Tutorials For Beginners*, https://www.youtube.com/watch?v=aEIHZDv_23U, accessed: 19 July 2025.

Joseph, D. (2023) *Creating a Simple To-Do List Application in Python: A Guide*, https://www.linkedin.com/pulse/creating-simple-to-do-list-application-python-guide-daniel-joseph-/, accessed: 18 July 2025.

NeuralNine. (2021) *Colored Console Output in Python*, https://www.youtube.com/watch?v=kf8kbUKeM5g, accessed: 27 July 2025.

ParcelMaiyo. (2023) *Text Styling in Python Using PyFiglet*, https://medium.com/@parcelmaiyo/text-styling-in-python-using-pyfiglet-824c498dfff5, accessed: 27 July 2025.

Patorjk. (n.d.) *Text to ASCII Art Generator (TAAG)*, https://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Bash%0ABedlam%0A, accessed: 27 July 2025.

ProgrammingHorizons. (2025) *To Do List App in Python | Python Project for Beginners*, https://www.youtube.com/watch?v=2H4cYt_3DsE, accessed: 18 July 2025.

PyPI. (2025) *emoji: Emoji for Python*, https://pypi.org/project/emoji/, accessed: 1 August 2025.

Schafer, C. (2017) *Python Tutorial: Working with JSON Data using the json Module*, https://www.youtube.com/watch?v=9N6a-VLBa2I, accessed: 22 July 2025.

W3Schools. (n.d.) *Python JSON*, https://www.w3schools.com/python/python_json.asp, accessed: 28 July 2025.

WebFX. (n.d.) *Emoji Cheat Sheet*, https://www.webfx.com/tools/emoji-cheat-sheet/, accessed: 2 August 2025.