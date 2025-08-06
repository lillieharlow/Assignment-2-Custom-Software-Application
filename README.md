# TO DO. App

A vibrant, secure, and easy-to-use command-line task manager designed to help you stay productive every day. Whether you prefer colorful interfaces, emoji-enhanced fun, or secure personalized task tracking, this app has you covered.

<hr>

## ✅ Help & Setup Documentation

### Installation & Setup

1. **System Requirements:**  
   - Python 3.8 or newer  
   - pip (Python package manager, usually installed with Python)

2. **Install dependencies:**  
   Run this command in your terminal to install the required Python packages with pinned versions:

   ```bash
   pip install rich pyfiglet bcrypt emoji
   ```

  Your `requirements.txt` should contain these pinned packages:  
  bcrypt==4.3.0
  emoji==2.14.1
  markdown-it-py==3.0.0
  mdurl==0.1.2
  pyfiglet==1.0.2
  Pygments==2.19.2
  rich==13.7.1
  six==1.17.0

  **Note:** Subdependencies like `Pygments`, `markdown-it-py`, `mdurl`, and `six` are automatically installed by pip — you do not need to install them manually.

3. **Run the app:**  
  From your terminal, start the application:

   ```bash
   python todo_manager/main.py
   ```

   Follow the on-screen prompts to sign up, log in, or use guest mode.

<hr>

## 💻 Hardware Requirements

- **Minimum:**  
- 512 MB RAM  
- 50 MB free disk space  
- CPU from last decade or newer

- **Recommended:**  
- 1 GB RAM or more for smoother multitasking  
- 100 MB disk space for larger task lists  
- Terminal emulator supporting Unicode & colors (e.g., Windows Terminal, macOS Terminal, Linux shells)

---

## ✨ Features of the App

- Secure user sign-up and login with passwords hashed by bcrypt (no plain-text storage)  
- Guest mode with temporary task lists (tasks lost on exit)  
- Easy task management: add, view, complete, or delete tasks with simple commands  
- Task priority levels: High, Medium, or Low for smart organization  
- Colorful CLI enhanced with emoji and ASCII art banners for an engaging user experience  
- User data stored safely in JSON files per account  
- Intuitive menu-driven interface—no steep learning curve

---

## 📦 Dependencies Required by the App

| Library           | Version  | License      | Security Impact        | Purpose                                 | Conflict Risk  |
|-------------------|----------|--------------|-----------------------|-----------------------------------------|---------------|
| **bcrypt**        | 4.3.0    | Apache 2.0   | Low (local, offline)  | Secure password hashing                  | None          |
| **emoji**         | 2.14.1   | MIT          | Low (UI only)         | Emoji rendering                         | None          |
| **markdown-it-py**| 3.0.0    | MIT          | Low (UI only)         | Markdown parsing (used by `rich`)      | None          |
| **mdurl**         | 0.1.2    | MIT          | Low                   | URL handling for markdown (`markdown-it-py` dependency) | None          |
| **pyfiglet**      | 1.0.2    | MIT          | Low (UI only)         | ASCII art banners                       | None          |
| **Pygments**      | 2.19.2   | BSD          | Low (UI only)         | Syntax highlighting (used by `rich`)   | None          |
| **rich**          | 13.7.1   | MIT          | Low (UI only)         | Enhanced CLI formatting, colors, tables | None          |
| **six**           | 1.17.0   | MIT          | Low                   | Python 2/3 compatibility (required by `bcrypt`) | None          |

### Legal & Ethical Impacts

- All dependencies are under permissive open source licenses (MIT, Apache 2.0, BSD) allowing free use, modification, and distribution.  
- No copyleft or restrictive licensing involved—safe to use and distribute in your projects without legal concerns.  
- The app operates locally only with no external data sharing, respecting user privacy and ethical best practices.

### Security Impact

- Passwords are safely hashed with bcrypt, avoiding plaintext risks.  
- All UI libraries affect display only, not security or user data.  
- Data storage is local (JSON files) with no network transmissions.

### Purpose of Each Dependency

- **bcrypt:** Handles the critical task of password hashing.  
- **emoji:** Enables colorful emoji display inside your CLI.  
- **rich:** The main powerhouse for CLI color, tables, and formatting.  
- **pyfiglet:** Generates fun ASCII banners.  
- **markdown-it-py, mdurl, Pygments:** Support markdown parsing and syntax highlighting needed by `rich`.  
- **six:** Provides Python 2/3 compatibility needed by `bcrypt`.

### Conflicts

- These packages are known to be fully compatible with each other, with no conflicting versions or installation issues on the specified versions.

---

## 📁 List of Required Files (Including Third-Party)

- `main.py` — The application’s starting point, launching the CLI task manager  
- `user.py` — Manages user signup, login, and guest access logic  
- `tasks.py` — Defines tasks and task list management classes  
- `styling.py` — Functions and helpers for CLI appearance, colors, and formatting  
- `emoji_library.py` — Central source for emoji codes used in CLI UI  
- `data/users.json` — JSON file storing user account info (created automatically)  
- `data/{username}_tasks.json` — JSON files for each user’s saved tasks (auto-created)

---

**Enjoy organizing your tasks with flair and security!**

If you want help adding usage examples, screenshots, or tips on customizing your app, just ask!


## Reference List:

WebFX (no date) Emoji Cheat Sheet. Available at: https://www.webfx.com/tools/emoji-cheat-sheet/ (Accessed: 6 August 2025).

NeuralNine (2021) 'Colored Console Output in Python', YouTube video, 9 May. Available at: https://www.youtube.com/watch?v=kf8kbUKeM5g (Accessed: 6 August 2025).

Jones, C. et al. (2007-2023) pyfiglet. Available at: https://pypi.org/project/pyfiglet/ (Accessed: 6 August 2025).

GeeksforGeeks (no date) Python ASCII Art Using Pyfiglet Module. Available at: https://www.geeksforgeeks.org/python/python-ascii-art-using-pyfiglet-module/ (Accessed: 6 August 2025).

Tech With Tim (2020) 'Python To-Do List Tutorial', YouTube video, 20 March. Available at: https://www.youtube.com/watch?v=J0w87IpcdYA (Accessed: 6 August 2025).

Stack Overflow (2019) 'I want to use JSON in Python to save users and password', Stack Overflow. Available at: https://stackoverflow.com/questions/54267646/i-want-to-use-json-in-python-to-save-users-and-password (Accessed: 6 August 2025).

Telusko (2018) 'Python GUI To-Do App | Tkinter', YouTube video, 10 January. Available at: https://www.youtube.com/watch?v=pY6RB4_EoSM (Accessed: 6 August 2025).

CodeWithHarry (2019) 'Python Project To-Do Application', YouTube video, 20 October. Available at: https://www.youtube.com/watch?v=uwaHwP3wfjY (Accessed: 6 August 2025).

Telusko (2017) 'Python Tkinter Tutorial', YouTube video, 18 September. Available at: https://www.youtube.com/watch?v=eIYKsSYKNPw (Accessed: 6 August 2025).

Clever Programmer (2020) 'Python Projects - To-Do List App Tutorial', YouTube video, 10 December. Available at: https://www.youtube.com/watch?v=aEIHZDv_23U (Accessed: 6 August 2025).

Halverson, S. (no date) PythonToDo, GitHub repository. Available at: https://github.com/ShaunHalverson/PythonToDo (Accessed: 6 August 2025).

emoji (no date) emoji: Emoji for Python. Available at: https://pypi.org/project/emoji/ (Accessed: 6 August 2025).

AIMind (2021) Creating a Simple To-Do List in Python. Available at: https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814 (Accessed: 6 August 2025).

Joseph, D. (no date) Creating a Simple To-Do List Application in Python: A Guide. LinkedIn. Available at: https://www.linkedin.com/pulse/creating-simple-to-do-list-application-python-guide-daniel-joseph-/ (Accessed: 6 August 2025).

GeeksforGeeks (2022) Installing and Using Rich Package in Python. Available at: https://www.geeksforgeeks.org/python/installing-and-using-rich-package-in-python/ (Accessed: 6 August 2025).

Corey Schafer (2020) 'Python Colorama Tutorial - Colored Console Output', YouTube video, 10 May. Available at: https://www.youtube.com/watch?v=4zbehnz-8QU (Accessed: 6 August 2025).

Patorjk (no date) Text to ASCII Art Generator (TAAG). Available at: https://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Bash%0ABedlam%0A (Accessed: 6 August 2025).

ParcelMaiyo (2019) Text Styling in Python Using PyFiglet. Medium. Available at: https://medium.com/@parcelmaiyo/text-styling-in-python-using-pyfiglet-824c498dfff5 (Accessed: 6 August 2025).

freeCodeCamp.org (2018) 'Python Tutorial - Full Course for Beginners', YouTube video, 17 April. Available at: https://www.youtube.com/watch?v=9N6a-VLBa2I (Accessed: 6 August 2025).

ProgrammingKnowledge (2017) 'Python Tutorial for Beginners', YouTube video, 18 May. Available at: https://www.youtube.com/watch?v=2H4cYt_3DsE (Accessed: 6 August 2025).