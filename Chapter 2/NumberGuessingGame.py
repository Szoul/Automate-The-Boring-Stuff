#create a game where you have to guess a number; it has to be in betweeen 2
#random numbers; the Programm should give you a hint whether it is lower or
# higher than the inserted number; if the correct number is typed in, show the
# number of tries before completion of the game

#Bonuspunkte: Hinweis falls die Zahl "viel größer/kleiner" ist (über 100,30,... entfernt)

#Zielzahl ist zwischen -999 und 999




import random
import os

while True:

    goal_number = random.randint(-999,999)
    lower_end = random.randint(-1000,1000)
    upper_end = random.randint(-1000,1000)
    player_try_counter = 0

    while lower_end >= goal_number:
        lower_end = random.randint(-1000,1000)
    while upper_end <= goal_number:
        upper_end = random.randint(-1000,1000)

    print("Welcome to Guessing the Number")
    print("The number you are looking for is in between " + str(lower_end) + " and " + str(upper_end))

    while True:
        print ("Type in your guess")
        player_guess = input()
        
        try:
            int(player_guess)                           #also goes to except if "player_guess" is a float - why?
        except ValueError:
            print ("Please enter an Integer")
            print ("")
            continue
#        if not (float(player_guess)).is_integer():     # dont need this because of upper problem
#                print("Please enter an Integer")
#                continue

        player_guess = int(player_guess)
        player_try_counter += 1

        if player_guess < goal_number:
            if player_guess + 100 < goal_number:
                print("Your number is way too low")
            elif player_guess + 30 < goal_number:
                print("Your number is too low")
            else:
                print("Your number is a just a bit too low")
        if player_guess > goal_number:
            if player_guess -100 > goal_number:
                print("Your number is way too high")
            elif player_guess - 30 > goal_number:
                print("Your number is too high")
            else:
                print("Your number is just a bit too high")
        if player_guess == goal_number:
            print("Congratulations! You found the right number!")
            print("It took you " + str(player_try_counter) + " tries to complete the game")
            break
        continue
    if not input("If you want to restart type in 'restart'. Otherwise press Enter to exit") == 'restart':
        break
os._exit(0)                                                   # hwo to exit shell with this command? - os._exit(0) did reopen new shell?
