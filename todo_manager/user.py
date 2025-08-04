# ============= user.py ============
# This class handles user login, signup and user management.
# Security system to make sure only the right user can access their task list.

import json
import os
from getpass import getpass
from emoji import emoji_edit_task, emoji_wink_face, emoji_not_found, emoji_complete_task, emoji_person, emoji_priority_high
from styling import print_error, print_success

# ========= User class =========
class User:
    """Handles all the user stuff - signing up, logging in, and keeping track of who's here!"""

    # ========== Create user object and set up file location ==========
    def __init__(self, users_file="data/users.json"):
        """Setting up where we keep user accounts and who's logged in"""
        self.users_file = users_file
        self.logged_in_user = None

    # ========== Load user from json file ==========
    def load_users(self):
        """Grab all existing users from the file"""
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except:
            return {}
    
    # ========== Save user to json file ==========
    def save_users(self, users):
        """Save all users so we don't lose anyone!"""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            with open(self.users_file, "w") as f:
                json.dump(users, f, indent=2)
            print_success(f"\nNICE CACHE! {emoji_wink_face} your account has been saved successfully.")
        except:
            print_error(f"\n{emoji_not_found} UGH, THIS IS WEIRD... your account couldn't be saved. Please try again.")

    # ========== Sign up new user ==========
    def register_user(self):
        """Create a new account with username and password"""
        users = self.load_users()
        print_success(f"\n{emoji_complete_task} WOOHOO! LET'S CREATE AN ACCOUNT!")

        while True:
            username = input(f"\n{emoji_edit_task} Choose your username: ").strip()
            if not username:
                print_error(f"\n{emoji_not_found} Please enter a valid username!")
                continue
            if username in users:
                print_error(f"\n{emoji_not_found} That username's already taken. Please try again!")
                continue
            break

        while True:
            password = getpass(f"\n{emoji_edit_task} Please enter your password (5+ characters): ").strip()
            password_confirm = getpass(f"\n{emoji_edit_task} Second time's a charm! Please re-enter your password: ").strip()

            if len(password) < 5:
                print_error(f"\n{emoji_not_found} That password's too short. Give me a stronger one!")
                continue
            if password != password_confirm:
                print_error(f"\n{emoji_not_found} Hmm, your passwords don't match. Want to try again?")
                continue
            break

        users[username] = {"password": password}
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    # ========== Log in user - 3 attempts ==========
    def login_user(self):
        """Log in existing user (3 tries max!)"""
        users = self.load_users()
        print_success("\n WELCOME BACK!")

        attempts = 0
        while attempts < 3:
            username = input(f"\n{emoji_person} Username: ").strip()
            if not username:
                print_error(f"\n{emoji_not_found} Please enter your username!")
                continue

            password = getpass(f"\n{emoji_edit_task} Password: ").strip()

            if username in users and users[username]["password"] == password:
                self.logged_in_user = username
                return username
            else:
                attempts += 1
                if attempts < 3:
                    print_error(f"\n{emoji_priority_high} OOPS! That username or password didn't check out. Please try again.")
    
        print_error(f"\n{emoji_priority_high} WOOPSEY! Too many failed attempts. Let's go back to main menu.")
        return None
                
    # ========== Get current logged in user ==========
    def get_current_user(self):
        """Who's using the app right now?"""
        return self.logged_in_user