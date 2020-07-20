import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:          #None means shotguns >= 3
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


''' 
Exercise:
Create following bots:
    1. decides randomly after first roll if it wants to contiue or stop
    2. stops rolling after brains rolled = 2 (or higher)
    3. stops rolling after 2 shotguns
    4. randomly decides to roll between 1-4 times, stops if shotguns = 2
    5. "A bot that stops rolling after it has rolled more shotguns than brains"
        -> on current roll(5) or overall(6)?
'''

import random

#1 roll, then randomly roll or stop
class Zombie1:
    def __init__ (self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            continue_rolling = random.randint(0,1)
            if continue_rolling == 0:
                diceRollResults = zombiedice.roll()
            else:
                break

#2
# is the same as example: if brains in current diceRollresults["brains"] + previous rolls < 2 THEN roll again

#3 (basically same as 2 but stop if overall_shotun = 2)
class Zombie3:
    def __init__ (self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns == 2:
                diceRollResults = zombiedice.roll()
            else:
                break

#4 random rolls 1-4, stop if shotguns = 2 or greater
class Zombie4:
    def __init__ (self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
    
        shotguns = 0
        rolls = random.randint(1,3)

        while (diceRollResults is not None) and (rolls > 0):
            rolls -= 1
            shotguns += diceRollResults["shotgun"]

            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


#5 roll until CURRENT number of shotguns > CURRENT number of brains
class Zombie5:
    def __init__ (self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
    
        while diceRollResults is not None:
            if diceRollResults["brains"] > diceRollResults["shotgun"]:
                diceRollResults = zombiedice.roll()
            else:
                break

#6 roll until overall number of shotguns > overall number of brains
class Zombie6:
    def __init__ (self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
    
        brains = 0
        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults["shotgun"]
            brains += diceRollResults["brains"]

            if shotguns <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break

myzombie1 = Zombie1("(selfmade)randomly Rolls")
myzombie3 = Zombie3("(selfmade)Stop at 2 Brains")
myzombie4 = Zombie4("(selfmade)Stop at 2 Shotguns")
myzombie5 = Zombie5("(selfmade)Stop if current shotguns greater than brains")
myzombie6 = Zombie6("(selfmade)Stop if overall shotguns greater than brains")




zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot (2)'),
    # Add any other zombie players here.
    myzombie1,
    myzombie3,
    myzombie4,
    myzombie5,
    myzombie6

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000) 