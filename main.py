# Nickname Assignment by Ibrahim Ismayilov

# Importing the random module 
import random

# Getting the User's First and Last Name
first_name = input("\nPlease enter your first name:")
last_name = input("\nPlease enter your last name:")

# Intializing grades list
names_and_nicknames = {
    "names": f"{first_name} {last_name}",
    "nicknames": ["The Butcher", "The Giant", "The Lion"]
}

def random_nickname():
    random_index = random.randint(0, len(names_and_nicknames["nicknames"]))
    random_nickname = names_and_nicknames["nicknames"][random_index]
    return random_nickname

# Menu Loop
loop = True
while loop:

    # Print Main Menu
    print("\nMAIN MENU")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")

    # Get Menu Selection From The User
    selection = input("Enter Selection (1-6): ")

    # Action Based on Menu Selection
    if selection == "1":
        print("\nChange Name")
        first_name = ("Please enter a first name:")
        last_name = ("Please enter a last name:")
        print(f"\nCurrent Name is {first_name} {last_name}.")
    elif selection == "2":
        print("\nDisplay a Random Nicknname")
        nickname = random_nickname()
        print(f'{first_name} "{nickname}" {last_name}') 
    elif selection == "3":
        print("\nDisplay All Nicknnames")
        for name in names_and_nicknames["nicknames"]:
            print(f'{first_name} "{name} ')
    elif selection == "4":
        print(grades_list)
        for i in range(len(grades_list)):
            grades_list[i] = random.randint(1, 99)
        print(grades_list)
        print("GRADES HAVE BEEN RANDOMIZED")
    elif selection == "4":
        pass
    elif selection == "5":
        pass
    elif selection == "6":
        loop = False