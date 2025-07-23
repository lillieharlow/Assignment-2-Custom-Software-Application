class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5        # 0 = full, 10 = starving
        self.happiness = 5     # 0 = sad, 10 = very happy

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"You feed {self.name}.")
        else:
            print(f"{self.name} is already full!")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            print(f"You play with {self.name}.")
        else:
            print(f"{self.name} is already as happy as possible!")

    def status(self):
        print(f"{self.name} | Hunger: {self.hunger} | Happiness: {self.happiness}")

def main():
    name = input("Name your virtual pet: ")
    pet = VirtualPet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check Status")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.status()
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid option. Please choose between 1-4.")

if __name__ == '__main__':
    main()
