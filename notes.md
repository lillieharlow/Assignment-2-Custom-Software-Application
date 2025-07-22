# Assignment-2-Custom-Software-Application
Assignment 2 for Coder Academy - aka my first software application.

File IO
User input
Meaningful output
Accessing data from external sources

Design a functioning app - web browser OR terminal (CLI) in python.

Check List:
[] README.md file
    [] help or set up documentation - explain how to install any files & start the app
    [] hardware requirements
    [] features of the app
    [] dependencies required by the app
    [] list required files (third party)
        [] explaining the legal and ethical impacts of their license (+/-)
        [] security impact
        [] purpose
        [] not conflict with each other
[] uses 4+ third party libraries/packages (import ..., virtual environments - add to README for installing)
[] handle all errors - catch errors with error handling teechniques
[] use DRY principles across whole app
[] functions
    [] imported from third party libraries (extensive use)
    [] 6+ functions written by myself
[] 3+ classes
    [] uses inheritance and composition in at least two
[] variable scope & access delarations
[] loops and condiitonal statements
    [] for multiple paths
    [] nested structures that handle multiple contingencies
[] 2+ input and output
    [] retrieving user input and displaying output
    [] reading from files and writing to files
    [] req data from an API and displaying output

## Set up of files:
- readme.md
- main.py
- packages folder
    - __init__.py
    - area to organise other py files?
- virtual environment folder
- requirements.txt
- license - copyright info, etc
- testing - test.py


## DRY PRINCIPALS:

DRY = Don't Repeat Yourself
- A software development principle to avoid code duplication.
- Encourages writing modular, reusable, and clean code.

Why is DRY Important?
- Avoids Repetition
- Prevents writing the same logic multiple times.
- Improves Code Readability
- Easier to understand and maintain.
- Easier Maintenance
- Fixing bugs in one place updates all uses.
- Reduces Errors
- Less duplicated logic = fewer chances for mistakes.
- Supports Scalability
- Code can grow and evolve without becoming messy.
- Functions () , def function_name()

# Brainstorm of idea

### What do I want to build?

A tamgotchi type game - Commmand-line pet game in python3. That evolves the users pet from one animal to the next (leveling up in the game). They need to care for the pet and make sure if doesn't die. So feeding, love, playing, cleaning poop, etc.

### How will I achieve this?

#### Step 1

[] Decide on what animals each level will evolve into? I want to use the VE cowsay.
[] What stats will pet have? Hunger, love, poop, energy, happiness, tired? Should I use emojis?
[] App runs in terminal so how do I want to display the menu/user input?
    - menu and give options linked to a number or letter user types in.
``` What would you like to do?
1. Feed your pet 🥕
2. Play with your pet 🎾
3. Rest 😴
4. Show stats 📊
5. Quit ❌

Enter your choice:
```

[] Add extra interactivity to keep user engagememt high, educational? Add fun facts?
[] File structure? What do I need to have as my py files, do I need to call them specific names?
[] Define what libraries and packages I will use?
    - 4+ from 3rd parties (libraries and packages)
    - 6+ functions I make myself
    - use functions from 3rd party libs/packages
    - 3+ classes

#### Step 2

[] Create and structure my folders correctly
[] Add virutal environemnts - also document set up so it is easier down the line when wirting my readme.md
[] Create requirements.txt
[] install all packages
[] main.py
[] py for classes I make - pets.py
[] game.py - game classes and logic
[] api.py - so I can get fun animals facts off the internet into the command line

``` import requests

response = requests.get("https:// ......)
data = response.json()
print(data['fact'])
```

import json = save user progress, load game when needed. Not actually using JavaScript - just a file format that python reads and writes.
[] storage.py - save game for user?
[] test.py - ```import unitest```

#### Step 3

[]