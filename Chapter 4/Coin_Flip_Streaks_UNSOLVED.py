#Write a program to find out how often a streak of six heads or a streak 
#of six tails comes up in a randomly generated list of heads and tails (length 100). 

#Put all of this code in a loop that repeats the experiment 10,000 times
#so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.

import random

streakcounter = 0
for experiment_loops in range (10000):
    coinflips = []
    for i in range (100):
        if random.randint(0,1) == 0:
            coinflips.append("Tails")
        else:
            coinflips.append("Heads")

    current_streak = 0
    for i in range (1,100):
        if coinflips[i] == coinflips[i-1]:
            current_streak += 1
        else:
            current_streak = 0
        if current_streak == 6:
            streakcounter += 1

print('Chance of streak: %s%%' % (streakcounter / 100))

merpcounter = 0
for i in range (1000000):
    newtest = []
    for x in range (6):
        newtest.append(random.randint(0,1))
    if (newtest[0] == newtest [1]) and (newtest[0] == newtest [2]) and (newtest[0] == newtest [3]) and (newtest[0] == newtest [4]) and (newtest[0] == newtest [5]):
        merpcounter += 1

print (str((merpcounter/1000000)))