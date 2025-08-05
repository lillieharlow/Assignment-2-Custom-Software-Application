# ============= user.py ============
# This class handles user login, signup and user management.
# Security system to make sure only the right user can access their task list.

import json
import os
from getpass import getpass
from emoji_library import emoji_person, emoji_edit_task, emoji_not_found
from styling import print_error, print_success, clear_screen
import bcrypt

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
                data = json.load(f)
                # Convert bytes back to proper format for bcrypt
                for username, user_data in data.items():
                    if isinstance(user_data["password"], str):
                        # Convert string back to bytes for bcrypt
                        user_data["password"] = user_data["password"].encode('latin-1')
                return data
        except:
            return {}
    
    # ========== Save user to json file ==========
    def save_users(self, users):
        """Save all users so we don't lose anyone!"""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            # Convert bytes to string for JSON storage
            users_for_json = {}
            for username, user_data in users.items():
                users_for_json[username] = {
                    "password": user_data["password"].decode('latin-1')
                }
            
            with open(self.users_file, "w") as f:
                json.dump(users_for_json, f, indent=2)
            clear_screen()
            print_success(f"\nNice cache! Your account has been saved.")
        except:
            print_error(f"\nUgh, JaSON didn't like that one... your account couldn't be saved. Please try again.")

    # ========== Sign up new user ==========
    def register_user(self):
        """Create a new account with username and password"""
        users = self.load_users()
        print_success(f"\nYay! Let's create your TO DO. account!")

        while True:
            username = input(f"\n{emoji_edit_task} Choose your username: ").strip()
            if not username:
                print_error(f"\nPlease enter a valid username!")
                continue
            if username in users:
                print_error(f"\nThat username's already taken. Please try again!")
                continue
            break

        while True:
            password = getpass(f"\n{emoji_edit_task} Please enter your password (5+ characters): ").strip()
            password_confirm = getpass(f"\n{emoji_edit_task} Second time's a charm! Please re-enter your password: ").strip()

            if len(password) < 5:
                print_error(f"\nThat password's too short. Give me a longer one!")
                continue
            if password != password_confirm:
                print_error(f"\nHmm, your passwords don't match. Want to try again?")
                continue
            break

        # Secure password hashing
        hashed_password = self.hash_password(password)
        users[username] = {"password": hashed_password}
        
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    # ========== Log in user - 3 attempts ==========
    def login_user(self):
        """Log in existing user (3 tries max!)"""
        users = self.load_users()
        print_success("\n Welcome back, please enter your login details.")

        attempts = 0
        while attempts < 3:
            username = input(f"\n{emoji_person} Username: ").strip()
            if not username:
                print_error(f"\n{emoji_not_found} Please enter your username!")
                continue

            password = getpass(f"\n{emoji_edit_task} Password: ").strip()

            # Secure password verification
            if username in users and self.check_password(password, users[username]["password"]):
                self.logged_in_user = username
                return username
            else:
                attempts += 1
                if attempts < 3:
                    print_error(f"\nOops! That username or password didn't match. Please try again!")

        print_error(f"\nUmm, this is awkward... Did you forget your details?\nLet's go back to the main menu.")
        return None
                
    # ========== Get current logged in user ==========
    def get_current_user(self):
        """Who's using the app right now"""
        return self.logged_in_user

    # ========== Secure password hashing ==========
    def hash_password(self, password):
        """Securely hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password, hashed):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)