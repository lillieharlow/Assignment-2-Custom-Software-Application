# Assignment-2-Custom-Software-Application
Assignment 2 for Coder Academy - aka my first software application.

Design a functioning python app for terminal (CLI).

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

# What?

- Virtual pet app
- choose, care for your pet with interactive input
- Goal = keep your pet happy, healthy, and engaged over time by performing actions like feeding, playing, and letting it rest. Here’s how it will work:

How the app works:

Choose and name a pet:
At the start, you pick the type of pet (dog, cat, fish, etc.) and give it a name. This creates a personalized experience.

See your pet’s status:
The app displays your pet’s key stats (e.g., hunger, happiness, energy, and health), often on a 0–10 or 0–100 scale. These numbers change based on your actions (for example, playing makes your pet happier but may decrease its energy).

Care for your pet through actions:
You interact via menu choices for things like:

Feeding (restores hunger)

Playing (increases happiness)

Resting (restores energy)

Sometimes, customizing your pet (appearance or name)

Viewing fun facts, jokes, or images fetched from external APIs (these can enrich the gameplay and demonstrate third-party library usage).

Time-based simulation:
The pet’s stats may slowly decay or change over time, encouraging regular interaction. For example, hunger or boredom increases if ignored.

Real-time feedback:
After each action, you see updated pet stats and receive messages or ASCII graphics reflecting your pet’s mood or activities. For CLI output, colored text can highlight changes.

Error handling:
The app will check for invalid inputs and handle them gracefully by displaying a user-friendly error message and reprompting you, ensuring the game doesn't crash.

Save/load feature:
Your pet’s status is saved to a file, so you can return later and continue caring for the same pet. You can load your saved pet at startup.

API integration:
The app fetches live information (like pet facts or weather for your pet’s mood) using web APIs, expanding interactivity and showing real-world data use.

Multi-class design with inheritance:
The application uses object-oriented programming to represent different pet types, their behaviors, and associated objects (like toys). Classes are structured to demonstrate inheritance (e.g., Dog and Cat subclasses of Animal) and composition (e.g., Pet has a Toy).

Extensible and fun:
The core game can be easily expanded (adding custom actions, sounds, or even a simple graphical interface using libraries like Pygame), making it a fantastic beginner project you can iterate on over time.

Summary:
Your app simulates a virtual pet’s life, letting users actively care for it by performing actions that affect its virtual wellbeing. It gives clear, immediate feedback, uses multiple Python libraries, persists data, and handles input and errors robustly—all in a simple, approachable framework suitable for beginners


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

# Step 1 - Set up files, imports and virtual environment.

- Activate virtual environment
- install ```rich```, ```colorma```, ```pyfiglet```, ```requests```, ```questionary```, ```animals```
- Create files/moduels to organise code

# Step 2 - User/player management code

- login, user input, validate, error handling
- get username/password inputs, save to JSON

# Step 3 - pet.py

- classes and functions for code pet.py moduel, keep all of it in here, comments
- methods and attributes that affect pet and player progression e.g. play, feed, clean.
- save progression in game?

# Step 4 - main.py

- prompt player login, creates new account, exit game
- test login code works
- pet creation for new user

# Step 5 - quiz

# Step 6 - animal facts



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