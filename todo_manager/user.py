'''User class (auth/user.py) handles user data.

Write an AuthManager (auth/auth_manager.py):
Allow new users to sign up (choose username & password).
Store hashed passwords securely (Python's hashlib).
Validate credentials on login.
Handle errors (e.g., username taken, wrong password).

Creating new users with secure passwords
Authenticating logins with password verification
Saving/loading user data to/from JSON files
Integration with your AuthManager class
'''

import hashlib
import os
import json

# Represents a single user with storage for username and password (secure)
# Classes best practice have capitalised names (lowercase is for variables/functions)
class User:
    def __init__(self, username, password = None, password_hash = None):
        self.username = username
        self.password_hash = password_hash # loading existing user with hashed password (security)
        
        # Hash a new password or use existing hash
        if password:
            self.password_hash = self._hash_password(password)
        elif password_hash:
            self.password_hash = password_hash
        else:
            raise ValueError("Must provide either password or password_hash") # Error handling for developer mistakes
           
    '''Hash a password using SHA-256.
    Plain text passwords are hased to store securely.
    Takes plin text password and scrambles it into unreadable text
    hashlib.sha256() = uses SHA-256 algorithm to scramble the password
    encode() = converts text to bytes (computer language)
    hexdigest() = converts scrambled bytes back to readable text
    '''    
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    '''Check if password matches stored hash
    Compares new scrambled version against the stored scrambled version
    Boolean functions returns True if match, False if not
    '''

    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)
    
    '''Convert user to dictionary for JSON storage.
    Take user object user = User("Lillie", "password123")
    Gets username & password_hash
    Creates a dictionary with these key-value pairs
    Returns dictionary, ready to be saved as JSON
    Prepares data for storage'''
    
    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }
    
    '''Create a User instance from a dictionary (for loading from JSON)
    @classmethod a class method called on the method itself, a factory that creates User objects
    Receives dictionary, extracts values, creates new user and returns User object
    This allows loading user data from JSON files or other sources
    Rebuilds objects from storage
    '''
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data["username"],
            password_hash=data["password_hash"]
        )
        
    #User object is converted to str, shows username only
    
    def __str__(self):
        return f"User: {self.username}"