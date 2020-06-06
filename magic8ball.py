import random, time, sys

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

def magic8ball_with_a_list(absolutely_magical):
    the_real_magic = ["This is just a filler for the 0 spot since it wont be used when called by random.randint(1,9); i dont really know what to write here, soooo.... how was your day you beautiful person?","It is very certain", "Super likely", "Mehh...", "YATSI", "You should rethink your life", "Did you really think that was a good Question?", "JERONIMO", "That would be a nono", "Mayhaps"]
    return the_real_magic[absolutely_magical]

def print_in_red(text):
    print ('\033[31m' + str(text) + '\033[37m')



print ("ask away")
while True:
    question = input ()
    quitting = ["quit" ,"exit", "stop" ,]
    if any(x == question.lower() for x in quitting):
        print_in_red ("Aww, you want to quit?, thats ok...")
        time.sleep (1)
        print_in_red ("But you have to be nice")
        print_in_red ("just say 'Thank you'")
        print ("")
        question = input()
        print ("")
        if "hank you" in question:
            
            print ("")
            print_in_red ("No Problem! Bye!")
            sys.exit()
        else:
            print_in_red ("So much for manners")
            continue
    
    if "thank you" == question or "ok" == question:
        print_in_red ("You are welcome!")
        print ("")
        print ("______________________________")
        continue

    print('\033[31m' + magic8ball_with_a_list(random.randint(1,9)) + '\033[37m')
    print ("")
    print ("the ball has spoken")
    print ("______________________________")
    print ("ask again?")
    print ("")
