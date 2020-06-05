import random

def magic8ball (absolutely_magical):
    if absolutely_magical == 1:
        return "It is certain"
    elif absolutely_magical == 2:
        return "Very likely"
    elif absolutely_magical == 3:
        return "Doubtful"
    elif absolutely_magical == 4:
        return "Definetly"
    elif absolutely_magical == 5:
        return "Yes"
    elif absolutely_magical == 6:
        return "Doesn't look so good"
    elif absolutely_magical == 7:
        return "My answer is no"
    elif absolutely_magical == 8:
        return "Concentrate and ask again"
    elif absolutely_magical == 9:
        return "You will find out in time"

print ("ask away")
while True:
    question = input ()
    print('\033[31m' + magic8ball(random.randint(1,9)) + '\033[37m')
    print ("")
    print ("the ball has spoken")
    print ("______________________________")
    print ("ask again?")
    print ("")
