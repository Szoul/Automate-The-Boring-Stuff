import random, copy, time

empty_board = {"Top-Left":" ", "Top-Middle":" ", "Top-Right":" ",
        "Middle-Left":" ", "Middle-Middle":" ", "Middle-Right":" ",
        "Bottom-Left":" ", "Bottom-Middle":" ", "Bottom-Right":" "}

def printfield(field):
    print (field["Top-Left"] + " | " + field["Top-Middle"] + " | " + field["Top-Right"])
    print ("----------")
    print (field["Middle-Left"] + " | " + field["Middle-Middle"] + " | " + field["Middle-Right"])
    print ("----------")
    print (field["Bottom-Left"] + " | " + field["Bottom-Middle"] + " | " + field["Bottom-Right"])



#Create Player Input
board = copy.deepcopy(empty_board)
while True:
    print ("Enter your move.")
    player_input = input()
    if player_input == "help":
        print ("enter the potition you want to put your mark in (watch for exact spelling):")
        print ("'Top-Left'; 'Top-Right'; 'Top-Middle'; 'Middle-Left'; 'Middle-Middle'; 'Middle-Right'; 'Bottom-Left'; 'Bottom-Middle' or 'Bottom-Right'")
        print ("to leave the game enter 'quit'")
        print ("to restart this round enter 'restart'")
        print ("__________________")
        continue
    if player_input == "quit":
        print("__________________")
        print ("Thanks for playing the game")
        print("__________________")
        time.sleep(3)
        break
    if player_input == "restart":
        board = copy.deepcopy(empty_board)
        print ("Starting new game...")
        time.sleep(2)
        print ("__________________")
        continue
    
    if player_input in board.keys():
        if board[player_input] == " ":
            board[player_input] = "X"
        else:
            print ("This space is already occupied")
            print ("__________________")
            continue
    else:
        print ("You did not type in any known argument. If you want to see the controls enter 'help'")
        print ("__________________")
        continue
    printfield(board)
#Create (random) Computer Input
    print ("Your opponent is making his choice")
    time.sleep(random.uniform(0.5,2.5))
    while True:
        computer_choice = random.choice(list(board.keys()))
        if board[computer_choice] == " ":
            board[computer_choice] = "O"            #This O is a String not the number zero
            break
        else:
            continue
    printfield(board)

#To-Do (if i ever bother to finish this)
    # Think about if it would be easier to do this with lists or dictionaries (especially when changing size/randomizing...)
    #(1)Create win/lose/tie condition
        #(2)Determine who begins the game
        #(2)Let Player Choose wether to use X or O
        #(2)Add a Win-Lose-Tie-Counter
            #(3)Make Player-Input easier to write
                #(4)think about how to make the computer input "smarter"
                #(4)create different boardsizes (and let player decide on size)
    