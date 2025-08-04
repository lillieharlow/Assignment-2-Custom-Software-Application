# ============= user.py ============
# This class handles user login, signup and user management.

import json
import os
from getpass import getpass
from emoji import emoji_add_task, emoji_edit_task, emoji_wink_face, emoji_not_found, emoji_complete_task, emoji_quit, emoji_priority_high
from styling import print_error, print_success, print_info

# ========= User class =========
class User:

    # ========== Create user object and set up file location ==========
    def __init__(self, users_file="data/users.json"):
        self.users_file = users_file
        self.logged_in_user = None

    # ========== Load user from json file ==========
    def load_users(self):
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except:
            return {}
    
    # ========== Save user to json file ==========
    def save_users(self, users):
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            with open(self.users_file, "w") as f:
                json.dump(users, f, indent=2)
            print_success(f"NICE CACHE! {emoji_wink_face}, your account has been saved successfully.")
        except:
            print_error(f"{emoji_not_found}, Ugh, this is weird... your account couldn't be saved. Please try again.")

    # ========== Sign up new user ==========
    def register_user(self):
        users = self.load_users()
        print_success(f"\n{emoji_add_task} WOOHOO! LET'S CREATE AN ACCOUNT!")

        while True:
            username = input(f"\n{emoji_edit_task}, Choose your username: ").strip()
            if not username:
                print_error(f"{emoji_not_found}, Please enter a valid username!")
                continue
            if username in users:
                print_error(f"{emoji_not_found}, That username's already taken. Please try again!")
                continue
            break

        while True:
            password = getpass(f"{emoji_edit_task}, Please enter your password (5+ characters): ").strip()
            password_confirm = getpass(f"{emoji_edit_task}, Second time's a charm! Please re-enter your password: ").strip()

            if len(password) < 5:
                print_error(f"{emoji_not_found}, That password's too short. Give me a stronger one!")
                continue
            if password != password_confirm:
                print_error(f"{emoji_not_found}, Hmm, your passwords don't match. Want to try again?")
                continue
            break

        users[username] = {"password": password}
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    # ========== Log in existing user ==========
    def login_user(self):
        users = self.load_users()
        password = getpass(f"{emoji_edit_task}, Password: ").strip()

        if username in users and users[username]["password"] == password:
            print_success(f"{emoji_complete_task}, WELCOME BACK {username}. It's nice to see you again!")
            self.logged_in_user = username
            return username
        else:
            print_error(f"{emoji_priority_high}, OOPS! That username or password didn't check out. Please try again.")
