import pyfiglet

from user import User

u = User()

print(pyfiglet.figlet_format("Welcome to FOR YOU!"))
print("Your personal to-do manager that cares about you!")

# Initalize user login, sign up or logout
while True:
    print("\nPlease choose an option:")
    print("1. Sign up")
    print("2. Log in")
    print("3. Log out")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        u.register_user()
    elif choice == "2":
        u.login_user()
    elif choice == "3":
        u.logout_user()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Ugh, this is awkward. Please eneter a number between 1 - 4. Let's try again!")
        
