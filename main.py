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

# Generating a random nickname
def random_nickname():
    random_index = random.randint(0, len(names_and_nicknames["nicknames"]) - 1)
    random_nickname = names_and_nicknames["nicknames"][random_index]
    return random_nickname


# Checking if a given nickname already exists in a list
def check_nickname(added_new_nickname):
    for i in range(len(names_and_nicknames["nicknames"])):
        if names_and_nicknames["nicknames"][i] == added_new_nickname:
                return i
    return -1


# Menu Loop
loop = True
while loop:

    # Print Main Menu
    print("\nMAIN MENU")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Edit a Nickname")
    print("6. Remove a Nickname")
    print("7. Exit")

    # Get Menu Selection From The User
    selection = input("Enter Selection (1-6): ")

    # Action Based on Menu Selection
    if selection == "1":
        print("\nCHANGE NAME")
        first_name = input("Please enter a first name:")
        last_name = input("Please enter a last name:")
        print(f"\nCurrent Name is {first_name} {last_name}.")
    elif selection == "2":
        print("\nRANDOM NICKNAME")
        nickname = random_nickname()
        print(f'\n{first_name} "{nickname}" {last_name}') 
    elif selection == "3":
        print("\nALL NICKNAMES")
        for nickname in names_and_nicknames["nicknames"]:
            print(f'{first_name} "{nickname}" {last_name}') 
    elif selection == "4":
        print("\nADD A NICKNAME")
        new_nickname = input("Please enter a nickname to add:")
        index = check_nickname(new_nickname)
        if index == -1:
            names_and_nicknames["nicknames"].append(new_nickname)
            print(f"{new_nickname} is added to the nickname list.")
        else: 
            print(f"{new_nickname} is already in the list.")
    elif selection == "5":
        print("\nEDIT A NICKNAME")
        edit_nickname = input("Please enter a nickname to edit:")
        new_nickname = input("Please enter the new nickname to add:")
        index = check_nickname(edit_nickname)
        if index == -1:
            print(f"{edit_nickname} was not found in the nickname list.")
        else:
            print(f"{edit_nickname} was edited and is now {new_nickname}.")
            names_and_nicknames["nicknames"][index] = new_nickname
    elif selection == "6":
        print("\nREMOVE A NICKNAME")
        remove_nickname = input("Please enter a nickname to remove:")
        index = check_nickname(remove_nickname)
        if index == -1:
            print(f"{remove_nickname} was not found in the nickname list.")
        else: 
            names_and_nicknames["nicknames"].pop(index)
            print(f"{remove_nickname} was removed from the nickname list.")
    elif selection == "7":
        loop = False
            
        

