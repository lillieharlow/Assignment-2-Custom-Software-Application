'''
User class handles signing up, loggin in and saving user accounts.
Stores user accounts in a JSON file so they don't get lost when the app closes.
'''

import json
import os
import emoji import *
from getpass import getpass

class User:
    
    def __init__(self, users_file="data/users.json"):
        #Create user object, set up where to save the data and track who is logged in.
        self.users_file = users_file
        self.logged_in_user = None
        
    def load_users(self):
        # Load users from json file, if no user exists - create an empty list.
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
        