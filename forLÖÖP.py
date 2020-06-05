for x in range(5):              #creates new variable x, with the starting 
                                #value 0; each iteration increases its value
                                #by 1
    print (x)
    print("Count to " + str(x))
    if x == 3:
        break                   #beaks the for Loop



#Task: add up all the numbers from 0 to 100
#remember to put INFORMATIONAL variable names

total = 0
for currentNumber in range(101):
    total = currentNumber + total
print (total)

#pause
for i in range (5):
    print ("")
#same thing but with a while Loop

total = 0
currentNumber = 0
while currentNumber < 101:
    total = total + currentNumber
    currentNumber += 1

print (total)
