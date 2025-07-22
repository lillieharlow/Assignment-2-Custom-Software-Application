# All user / player details. User login or user create new account

import json # Saving username, password to a file and loading it back
import os # Check if user file exists and creates new one if it doesn't
from getpass import getpass # safety - asks for password without showing password

# Add new user (username & password)
def add_user():
    # Load the existing users from file (or empty dict if none)
    users = load_users()

    print("\n New User Registration")

    # Loop until a valid, unique username is entered
    while True:
        # Prompt for username and strip whitespace at start/end
        username = input("Please enter your username: ").strip()
        
        # Check if username is empty
        if not username:
            print("Username can't be empty.")
            continue
        
        # Check if username is already taken
        if username in users:
            print("That username is already taken.")
            continue
        
        # Valid username found, exit loop
        break

    # Loop until a valid password is entered and confirmed
    while True:
        # Prompt for password safely (hidden input)
        password = getpass("Password: ").strip()
        # Prompt again to confirm
        password2 = getpass("Re-enter password: ").strip()

        # Verify minimum password length
        if len(password) < 5:
            print("Your password is too short.")
            continue

        # Check if both passwords match
        if password != password2:
            print("Your passwords don't match.")
            continue

        # Valid password confirmed, exit loop
        break

    # Add the new user and their password to the users dictionary
    users[username] = {"password": password}

    # Save updated users dictionary back to file
    save_users(users)

    # Confirm successful registration
    print("YAY! You've successfully created an account.")

    # Return the new username to calling function
    return username
