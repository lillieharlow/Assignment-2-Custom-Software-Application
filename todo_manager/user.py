'''
User class handles signing up, logging in and saving user accounts.
Stores user accounts in a JSON file so they don't get lost when the app closes.
'''

import json
import os
from emoji import *
from getpass import getpass
import rich

class User:
    
    def __init__(self, users_file="data/users.json"):
        """Create user object, set up where to save the data and track who is logged in."""
        self.users_file = users_file
        self.logged_in_user = None
        
    def load_users(self):
        """Load users from json file, if no user exists - create an empty dictionary."""
        if not os.path.exists(self.users_file):
            print(f"{emoji_not_found} No user data found. Let's sign up!")
            return {}
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print(f"{emoji_not_found} Oh no! Your account has been corrupted by the evil JSON overlords. Please sign up again.")
            return {}
    
    def save_users(self, users):
        """Save users to file so we don't lose them."""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        try:
            with open(self.users_file, "w") as f:
                json.dump(users, f, indent=2)
            print(f"Your account has been saved successfully! Or should I say, nice 'cache'! {emoji_wink_face}")
        except IOError as e:
            print(f"{emoji_not_found} Oh-no! {e} ... guess we couldn't 'cache' it. Please try again!")

    def register_user(self):
        """Sign up new user with username and password."""
        users = self.load_users()
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
        self.save_users(users)
        self.logged_in_user = username  # Automatically log in the new user

        print(f"{emoji_complete_task} Awesome! Your account '{username}' is all set up. Welcome to FOR YOU! The to-do manager that cares about you!")
        return username

    def login_user(self):
        """Log in an existing user by checking their username and password."""
        users = self.load_users()
        print(f"\n{emoji_quit} Welcome back! (Type 'exit' or leave empty to cancel login)")

        while True:
            username = input(f"{emoji_edit_task} Username: ").strip()
            if username.lower() == "exit" or username == "":
                print(f"{emoji_quit} Login cancelled. Farewell, goodbye, the end! See you next time!")
                return None

            password = getpass(f"{emoji_edit_task} Password: ").strip()

            if username in users and users[username]["password"] == password:
                print(f"{emoji_complete_task} Welcome back, {username}! It's nice to see you again, let's use FOR YOU!")
                self.logged_in_user = username  # Remember who is logged in
                return username
            else:
                print(f"{emoji_priority_high} Oops! That username or password didn't check out. Try again or type 'exit' to quit.")

    def logout_user(self):
        """Log out whoever is currently logged in."""
        if self.logged_in_user:
            print(f"{emoji_quit} Goodbye, {self.logged_in_user}! Thanks for using FOR YOU!")
            self.logged_in_user = None
        else:
            print(f"{emoji_not_found} No user is currently logged in.")

    def get_current_user(self):
        """Tell us who is logged in right now."""
        return self.logged_in_user

    def is_logged_in(self):
        """Check if someone is logged in (True) or not (False)."""
        return self.logged_in_user is not None
        