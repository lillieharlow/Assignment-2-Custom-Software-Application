'''User functions: location of user, load user, save user, new user, login user.
Stored using JSON and gathered with user input to securely handle all loading & saving of user data.'''

import json
import os
from emoji import * # * = imports all variables from emoji.py
from getpass import getpass

# LOCATION OF USER DATA - This is the file where user data will be stored
# It's a constant, so the name of the variable is written in ALL CAPS
USERS_FILE = "data/users.json"

# LOAD USERS - Check if file exists, if not, create empty dictionary
def load_users():
    if not os.path.exists(USERS_FILE): # No user data
        print(f"{emoji_not_found} No user data found. Starting fresh!")
        return {} # Start new — create empty dictionary to add key-value
    try:
        with open(USERS_FILE, "r") as f: # r = read mode/read file as new variable 'f'
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"{emoji_not_found} Oh no! Your account is in jail! It's been corrupted by the evil JSON overlords. Time to start fresh!")
        return {}

# Save user
def save_users(users):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    try:
        with open(USERS_FILE, "w") as f: # w = write mode
            json.dump(users, f, indent=2) # makes it human readable json
        print(f"{emoji_complete_task} User data saved successfully!")
    except IOError as e:
        print(f"{emoji_not_found} Oops! We tried to save but hit a snag... guess it couldn't *cache* it. But seriously: {e}")

# New User
def register_user():
    users = load_users()
    print(f"\n{emoji_add_task} Woohoo! Let's get you signed up!")
    while True:
        username = input(f"{emoji_edit_task} Choose your username: ").strip()
        if not username:
            print(f"{emoji_not_found} Username can't be empty... this is awkward. Please try again!")
            continue
        if username in users:
            print(f"{emoji_not_found} Second place! That username's already taken. Try another one?")
            continue
        break

    while True:
        password = getpass(f"{emoji_edit_task} Please enter your password (5+ characters): ").strip()
        password_confirm = getpass(f"{emoji_edit_task} Second time's a charm! Please re-enter your password: ").strip()

        if len(password) < 5:
            print(f"{emoji_not_found} That password's too short. Give me a stronger one!")
            continue
        if password != password_confirm:
            print(f"{emoji_not_found} Hmm, your passwords don't match. Want to try again?")
            continue
        break

    users[username] = {"password": password}
    save_users(users)

    print(f"{emoji_complete_task} Awesome! Your account '{username}' is all set up. Welcome to FOR YOU! The to-do manager that cares about you!")
    return username

# Login user
def login_user():
    users = load_users()
    print(f"\n{emoji_quit} Welcome back! (Type 'exit' or leave empty to cancel login)")

    while True:
        username = input(f"{emoji_edit_task} Username: ").strip()
        if username.lower() == "exit" or username == "":
            print(f"{emoji_quit} Login cancelled. Farewell, goodbye, the end! See you next time!")
            return None

        password = getpass(f"{emoji_edit_task} Password: ").strip()

        if username in users and users[username]["password"] == password:
            print(f"{emoji_complete_task} Welcome back, {username}! It's nice to see you again, let's use FOR YOU!")
            return username
        else:
            print(f"{emoji_priority_high} Oops! That username or password didn't check out. Try again or type 'exit' to quit.")