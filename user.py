# user.py = All user / player details
# login, create new user

import json # saving username, password to a file and loading it back
import os # check if user file exists and creates new one if it doesn't
from getpass import getpass # safety - asks for password without showing password


# location of saved player files
players_file = "data/players.json" # players.json = file where info is stored

# load existing player or start new
# dictionary because we need key-value pairs (username & password)
def load_users():
    if not os.path.exists(players_file): # players file doesn't exist
        return {} # start fresh - return empty dictionary
    with open(players_file, "r") as f: # open players file in read mode as new variable
        try:
            return json.load(f)
        except json.JSONDecodeError: # if file is corrupted it starts fresh
            return{}
        
# save players to file, ensure folder exists
def save_players(players):
    os.makedirs("data", exist_ok=True) # if folder exists continue
    with open(players_file, "w") as f: # open in write mode
        json.dump(players, f, indent=2) # human readable file storing player data
        
# add new player (username & password)
def add_player():
    players = load_players()
    print("\n New Player")
    while True:
        playername = input("Please enter your name: ").strip() # .strip() = remove whitespace from start and end of str
        if not playername:
            print("Player name can't be empty.")
            continue
        if playername in players:
            print("That player name is already taken.")
            continue
        break
    while True:
        password = getpass("Password: ").strip()
        password2 = getpass("Re-enter password: ").strip()
        