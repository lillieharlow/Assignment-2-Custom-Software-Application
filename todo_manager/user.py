'''
The User class represents individual users and handles:
- Creating new user accounts with username/password
- Verifying user credentials during login
- Converting user data to/from JSON format for storage
- Secure password hashing to prevent plain-text storage

Designed to integrate with AuthManager for complete authentication workflow.
'''

import hashlib
import os
import json

class User:
    """
    Represents a single user with secure password storage.
    Classes use capitalized names (lowercase is for variables/functions).
    """
    
    def __init__(self, username, password=None, password_hash=None):
        """Initialize user with username and password (hashed for security)."""
        self.username = username
        
        if password:
            self.password_hash = self._hash_password(password)
        elif password_hash:
            self.password_hash = password_hash
        else:
            raise ValueError("Must provide either password or password_hash")
           
    def _hash_password(self, password):
        """
        Hash a password using SHA-256 for secure storage.
        
        Takes plain text password and scrambles it into unreadable text:
        - hashlib.sha256() uses SHA-256 algorithm to scramble the password
        - encode() converts text to bytes (computer language)
        - hexdigest() converts scrambled bytes back to readable text
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        """
        Check if password matches stored hash.
        
        Compares new scrambled version against the stored scrambled version.
        Returns True if passwords match, False if they don't.
        """
        return self.password_hash == self._hash_password(password)
    
    def to_dict(self):
        """
        Convert user to dictionary for JSON storage.
        
        Takes user object like User("Lillie", "password123") and:
        - Gets username & password_hash
        - Creates a dictionary with these key-value pairs
        - Returns dictionary ready to be saved as JSON
        """
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a User instance from a dictionary (for loading from JSON).
        
        This is a factory method that creates User objects:
        - Receives dictionary from JSON file
        - Extracts username and password_hash values
        - Creates new User object and returns it
        - Allows rebuilding users from stored data
        """
        return cls(
            username=data["username"],
            password_hash=data["password_hash"]
        )
        
    def __str__(self):
        """Convert User object to string, shows username only (for security)."""
        return f"User: {self.username}"