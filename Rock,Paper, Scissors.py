import random
import time

games_played = 0
games_won = 0
games_lost = 0
games_ties = 0
dumb_count = 0

#(r)ock = 1
#(p)aper = 2
#(s)cissors = 3

print ("ROCK, PAPER, SCISSORS")
while True:
    print (str(games_played) + " rounds played so far")
    print (str(games_won) + " Wins, " + str(games_lost) + " Losses, " + str(games_ties) + " Ties")

    opponents_move = random.randint (1,3)
    if opponents_move == 1:
        opponents_move = "ROCK"
    elif opponents_move == 2:
        opponents_move = "PAPER"
    elif opponents_move == 3:
        opponents_move = "SCISSORS"

    print ("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
    player_input = input()
    if player_input == "r":
        player_input = "ROCK"
    elif player_input == "p":
        player_input = "PAPER"
    elif player_input == "s":
        player_input = "SCISSORS"
    elif player_input == "q":
        break
    else:
        if dumb_count >= 5 and dumb_count < 10:
            print ("Stop fooling around")
        elif dumb_count >= 10 and dumb_count < 15:
            print ("I like perseverance, but you are overdoing it a bit")
        elif dumb_count >= 15 and dumb_count < 20:
            print ("...")
        elif dumb_count >= 20 and dumb_count < 25:
            print ("Get a life")
        elif dumb_count >= 25 and dumb_count < 30:
            print ("Stop being annoying and play the game")
        elif dumb_count >= 30 and dumb_count < 35:
            print ("YOU CHALLENGE ME MORTAL???")
        elif dumb_count == 35:
            print ("Do not go any further")
        elif dumb_count > 35:
            print ("")
            print ("")
            print ("You were warned")
            print ("")
            print ("")
            time.sleep (2)
            while True:
                print (("UwU OwO ")*10)
        else:
            print ("Please enter: r for ROCK, p for PAPER and s for SCISSORS, or q to QUIT the game")
        dumb_count += 1
        print ("")
        print ("")
        continue
    
    dumb_count = 0
    
    print (player_input + " vs... ")
    random_waiting_time = random.uniform(0.5,4.0)
    time.sleep(random_waiting_time)
    print (opponents_move)

    if player_input == opponents_move:
        game_outcome = "It's a tie!"
        games_ties += 1
    elif (player_input == "ROCK" and opponents_move == "SCISSORS") or (player_input == "PAPER" and opponents_move == "ROCK") or (player_input == "SCISSORS" and opponents_move == "PAPER"): 
        game_outcome = "You won!"
        games_won += 1
    else:
        game_outcome = "You lost!"
        games_lost += 1
    games_played += 1

    print (game_outcome)
    print ("")