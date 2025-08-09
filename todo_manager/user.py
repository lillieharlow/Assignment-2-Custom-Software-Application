"""Handles user management (login, signup) securely
Features:
User class: Handles signup, login, tracks current user
__init__: Sets up user file, logged-in user
load_users(): Loads users from file
save_users(): Saves users to file
register_user(): Signup logic
login_user(): Login logic
get_current_user(): Returns current user
GuestUser class: Inherits from User, marks as guest
except Exception as e: handle errors gracefully
->: type hinting for better code clarity"""

import json
import os
from getpass import getpass
from emoji_library import person, add, cross, lock, interesting, smile
from styling import print_error, print_success, clear_screen
import bcrypt

# ========= User class =========
class User:
    """User signup, logging in, and keeping track of who's logged in."""

    # ========== Create user and set up file location ==========
    def __init__(self, users_file: str = "data/users.json"):
        self.users_file = users_file
        self.logged_in_user = None

    # ========== Load user from json file ==========
    def load_users(self) -> dict:
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, "r") as f:
                data = json.load(f) # Convert bytes back to proper format for bcrypt
                for username, user_data in data.items():
                    if isinstance(user_data["password"], str): # Convert string back to bytes for bcrypt
                        user_data["password"] = user_data["password"].encode('latin-1')
                return data
        except Exception as e:
            print_error(f"\nError loading users: {e}")
            return {}
    
    # ========== Save user to json file ==========
    def save_users(self, users: dict) -> None:
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            users_for_json = {} # Convert bytes to string for JSON storage
            for username, user_data in users.items():
                users_for_json[username] = {
                    "password": user_data["password"].decode('latin-1')
                }
            with open(self.users_file, "w") as f:
                json.dump(users_for_json, f, indent=2)
            clear_screen()
            print_success(f"\nNice cache! Your account has been saved.")
        except Exception as e:
            print_error(f"\nUgh, JaSON didn't like that one {interesting}. Error: {e}\nPlease try again.")

    # ========== Sign up/create new user account ==========
    def register_user(self) -> str:
        users = self.load_users()
        print_success(f"\nYay! {smile} Let's create your TO DO. account!")

        while True:
            username = input(f"\n{person} Choose your username: ").strip()
            if not username:
                print_error(f"\nPlease enter a valid username!")
                continue
            if username in users:
                print_error(f"\nThat username's already taken. Please try again!")
                continue
            break

        while True:
            password = getpass(f"\n{add} Please enter your password (5+ characters): ").strip()
            if len(password) < 5:
                print_error(f"\nThat password's too short. Give me a longer one!")
                continue
            password_confirm = getpass(f"\n{add} Second time's a charm! Please re-enter your password: ").strip()
            if password != password_confirm:
                print_error(f"\nHmm {interesting} your passwords don't match. Want to try again?")
                continue
            break

        hashed_password = self.hash_password(password)  # Secure password hashing
        users[username] = {"password": hashed_password}
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    # ========== Log in existing user - 3 attempts ==========
    def login_user(self) -> str:
        users = self.load_users()
        print_success(f"\n {smile} Please enter your login details:")

        attempts = 0
        while attempts < 3:
            username = input(f"\n{person} Username: ").strip()
            if not username:
                print_error(f"\n{cross} Please enter a valid username.")
                continue
            password = getpass(f"\n{lock} Password: ").strip()
            if username in users and self.check_password(password, users[username]["password"]): # Secure password verification
                self.logged_in_user = username
                return username
            else:
                attempts += 1
                if attempts < 3:
                    print_error(f"\nOops! That username or password didn't match {interesting}. Please try again!")
        clear_screen()
        print_error(f"\nUmm, this is awkward {interesting} Did you forget your details?\nLet's go back to the main menu.")
        return None
                
    # ========== Get current user ==========
    def get_current_user(self) -> str:
        return self.logged_in_user # Who's using the app right now

    # ========== Secure password hashing with bcrypt ==========
    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password: str, hashed: bytes) -> bool:
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

# ========== Guest User - doesn't save tasks or login details ==========
class GuestUser(User): # Inherits from User class
    def __init__(self) -> None:
        super().__init__()
        self.is_guest = True