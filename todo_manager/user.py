# User class handles signing up, logging in and saving user accounts

import json
import os
from getpass import getpass
from emoji import emoji_add_task, emoji_edit_task, emoji_wink_face, emoji_not_found, emoji_complete_task, emoji_quit, emoji_priority_high
from styling import print_error, print_success, print_info, print_warning, print_welcome

class User:
    
    def __init__(self, users_file="data/users.json"):
        """Create user object and set up file location"""
        self.users_file = users_file
        self.logged_in_user = None
        
    def load_users(self):
        """Load users from json file"""
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except:
            return {}
    
    def save_users(self, users):
        """Save users to file"""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            with open(self.users_file, "w") as f:
                json.dump(users, f, indent=2)
            print_success(f"Your account has been saved successfully! Or should I say, nice 'cache'! {emoji_wink_face}")
        except:
            print_error("Could not save your account. Please try again!")

    def register_user(self):
        """Sign up new user with username and password"""
        users = self.load_users()
        print_welcome(f"\n{emoji_add_task} Woohoo! Let's get you signed up!")
        
        while True:
            username = input(f"\n{emoji_edit_task} Choose your username: ").strip()
            if not username:
                print_error(f"{emoji_not_found} Username can't be empty. Please try again!")
                continue
            if username in users:
                print_error(f"{emoji_not_found} That username's already taken. Try another one?")
                continue
            break

        while True:
            password = getpass(f"{emoji_edit_task} Please enter your password (5+ characters): ").strip()
            password_confirm = getpass(f"{emoji_edit_task} Second time's a charm! Please re-enter your password: ").strip()

            if len(password) < 5:
                print_error(f"{emoji_not_found} That password's too short. Give me a stronger one!")
                continue
            if password != password_confirm:
                print_error(f"{emoji_not_found} Hmm, your passwords don't match. Want to try again?")
                continue
            break

        users[username] = {"password": password}
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    def login_user(self):
        """Log in an existing user"""
        users = self.load_users()
        print_info(f"\nWelcome back! (Type 'exit' or leave empty to cancel login)")

        while True:
            username = input(f"{emoji_edit_task} Username: ").strip()
            if username.lower() == "exit" or username == "":
                print_info(f"{emoji_quit} Login cancelled. See you next time!")
                return None

            password = getpass(f"{emoji_edit_task} Password: ").strip()

            if username in users and users[username]["password"] == password:
                print_success(f"{emoji_complete_task} Welcome back, {username}! It's nice to see you again, let's use TO DO!")
                self.logged_in_user = username
                return username
            else:
                print_error(f"{emoji_priority_high} Oops! That username or password didn't check out. Try again or type 'exit' to quit.")

    def get_current_user(self):
        """Return currently logged in user"""
        return self.logged_in_user

    def is_logged_in(self):
        """Check if someone is logged in"""
        return self.logged_in_user is not None