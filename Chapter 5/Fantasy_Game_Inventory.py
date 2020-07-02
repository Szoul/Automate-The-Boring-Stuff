#You are creating a fantasy video game. The data structure to model the player’s
#inventory will be a dictionary where the keys are string values describing the 
#item in the inventory and the value is an integer value detailing how many of 
#that item the player has. For example, the dictionary value 
myinventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
#means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
#Inventory:
#12 arrow
#42 gold coin
#1 rope
#6 torch
#1 dagger
#Total number of items: 62

def displayInventory(inventory):
    list_of_keys = list(inventory.keys())
    list_of_keys.sort()                                             #added: always display the list in alphabetical order
    total_number_of_items = 0

    print ("Inventory:")
    for current_item in list_of_keys:
        print (str(inventory[current_item]) + " " + current_item)
        total_number_of_items += int(inventory[current_item]) 
    print ("Total number of items: " + str(total_number_of_items))

displayInventory(myinventory)