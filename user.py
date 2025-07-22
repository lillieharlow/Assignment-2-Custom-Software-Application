'''Functions for ALL new & existing users.
Stored using JSON and gathered with user input.
Securely handles ALL loading & saving of user data.'''


import json
import os
from getpass import getpass

# Location of user info
USERS_FILE = "data/users.json"

# Load user
def load_users():
    if not os.path.exists(USERS_FILE): # No user data
        return {} # Start new — create empty dictionary to add key-value
    try:
        with open(USERS_FILE, "r") as f: # r = read mode/read file as new variable 'f'
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Oh no! Your account is in jail! It's been corrupted by the evil JSON overlords. Time to start fresh!")
        return {}

# Save user
def save_users(users):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    try:
        with open(USERS_FILE, "w") as f: # w = write mode
            json.dump(users, f, indent=2) # makes it human readable json
    except IOError as e:
        print(f"Oops! We tried to save but hit a snag... guess it couldn't *cache* it. But seriously: {e}")

# New User
def register_user():
    users = load_users()
    print("\nWoohoo! Let's get you signed up!")
    while True:
        username = input("Choose your username: ").strip()
        if not username:
            print("Ugh, it's empty... this is awkward. Please try again!")
            continue
        if username in users:
            print("Second place! That username's already taken. Try another one?")
            continue
        break

    while True:
        password = getpass("Please enter your password (5+ characters: ").strip()
        password_confirm = getpass("Second times a charm! Please re-enter your password: ").strip()

        if len(password) < 5:
            print("That password's too short. Give me a stronger one!")
            continue
        if password != password_confirm:
            print("Hmm, your passwords don't match. Want to try again?")
            continue
        break

    users[username] = {"password": password}
    save_users(users)

    print(f"Awesome! Your account '{username}' is all set up. Welcome to PETvolution()!")
    return username

# Login user
def login_user():
    users = load_users()
    print("\nWelcome back! (Type 'exit' or leave empty to cancel login)")

    while True:
        username = input("Username: ").strip()
        if username.lower() == "exit" or username == "":
            print("Login cancelled. Farwell, goodbye, the end! See you next time!")
            return None

        password = getpass("Password: ").strip()

        if username in users and users[username]["password"] == password:
            print(f"Welcome back, {username}! It's nice to see you agai, let's play PETvolution()!")
            return username
        else:
            print("Oops! That username or password didn't check out. Try again or type 'exit' to quit.")
