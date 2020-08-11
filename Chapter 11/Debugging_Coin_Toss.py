'''
The following program is meant to be a simple coin toss guessing game. The player 
gets two guesses (it’s an easy game). However, the program has several bugs in it. 
Run through the program a few times to find the bugs that keep the program from working correctly.
'''

# original (inside a function):
def bugged_game():
    import random
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guesss = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

# debugged version
def debugged_game():
    import random
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1)
    if toss == 0:                                                       # added 4 lines to transform random.randint(0,1) output, so that <if toss == guess> makes sense
        toss = "tails"
    else:
        toss = "heads"
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()                                                 # removed an "s" from variable name
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

# execution: 
print ("bugged coin toss:")
bugged_game()
print ("\ndebugged coin toss:")
debugged_game()