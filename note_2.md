Name - Petvolution()!
Overview - A fun CLI virtual pet app! Help your pet grow and evolve from a puppy --> lion --> dragon!

You will feed, care, clean and play with your pet whilst learning fun animal facts and testing your quiz skills!

# 1 - Prepare moduels

Virtual Pet Game - Petvolution()!

Folder name - ?
Files I will need:
[] main.py
[] pet.py
[] games.py
[] utilities.py
[] requirements.txt
[] README.md
[] notes.md (& other md files that display psuedocode / planning ideas)

# 2 - Prepare virtual environemnt

Set up my virutal environemnt
```
python3 -m venv venv
source venv/bin/activate
```

# 3 - Figure out third party libraries and packages and create requirements.txt

```
pip install pyfiglet colorama requests emoji questionary
```

``` 
pip freeze > requirements.text
```

# 4 - Lets begin! You've got this! main.py

[] display welcome message
[] short blurb about the game - dog > lion > dragon, complete games/quizzes to level up and care for your pet
[] does user need to load a saved pet or create a new one?
[] show menu for return to saved pet, create new pet or exit user input
[] respond - "return" = account login. "new" = acount sign up (enter your name, pets name, password) loops until user has signed in or exits if they cloose "exit" = display goodbye message (but have input option to easily show welome message again if they accidentally exited)
[] Once signed in or signed up - proceed with main code. Code for save and load pet data in moduel pet

``` import pyfiglet
import emoji
from colorama import Fore, Style, init
from pet import load_pet, save_pet, create_new_pet
from games import play_game
from utilities import get_animal_fact
```

# 5 - Pet moduel - pet.py
[] functions I need to create about users pet
    - save pet
    - load pet
    - create new pet
    - pet (name, level, points, animal, hungry, clean, happy)