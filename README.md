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
