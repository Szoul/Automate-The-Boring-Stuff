#! python 3.8.3
#Sandwichmaker.py: Ask for Sandwich preferences

'''
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

    Using inputMenu() for a bread type: wheat, white, or sourdough.
    Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
    Using inputYesNo() to ask if they want cheese.
    If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
    Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
    Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''

import pyinputplus as pyip

prices =    {
            "wheat": 1.5, "white": 1.4, "sourdough": 1.7,                      #bread type
            "chicken": 2.2, "turkey": 3.4, "ham": 3.3, "tofu": 2.6,            #protein type
            "cheddar": 1.7, "swiss": 2.1, "mozzarella": 3.3,                   #cheese type
            "mayo": 0.3, "mustard": 0.3, "lettuce": 0.5, "tomato": 0.5         #extras
            }
list_of_extras = ["mayo", "mustard", "lettuce", "tomato"]
extras = []
number_of_sandwiches = 0

print ("Let's make you a Sandwich!")

bread_type = pyip.inputMenu(["wheat","white","sourdough"], prompt = "What kind of bread would you like?\n", numbered = True)
bread_price = prices[bread_type] 

protein_type = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt = "Any preference on the protein type?\n", numbered = True)
protein_price = prices[protein_type]

if pyip.inputYesNo(prompt = "Would you like to add cheese?\n") == "yes":
    cheese_type = pyip.inputMenu(["cheddar","swiss","mozzarella"], prompt = "What kind of cheese?\n", numbered = True)
try:
    cheese_price = prices [cheese_type]
except (NameError, KeyError):
    cheese_price = 0


for extra in list_of_extras:
    if pyip.inputYesNo(prompt = f"Would you like me to add {extra}?\n") == "yes":
        extras.append(extra)
extras_price = 0
if len(extras) != 0:
    for extra in extras:
        extras_price += prices[extra]

number_of_sandwiches = pyip.inputInt(min = 1, prompt = "How many of these sandwiches would you like to buy?\n")


price_of_sandwich = bread_price + protein_price + cheese_price + extras_price
total_price = price_of_sandwich*number_of_sandwiches

print (f"You have ordered {number_of_sandwiches} Sandwiches for the price of {price_of_sandwich} each")
print (f"That will be {total_price} [currency]")