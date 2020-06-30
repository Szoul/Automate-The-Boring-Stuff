test = [] 
test +=  "abcd"

print (test)
print ("input 1 = first number, input 2 = 2nd")

while True:
    first = input()
    second = input()

    first_int = False
    second_int = False
    try:
        first = int(first)
        first_int = True
        second = int(second)
        second_int = True
    except:
        try:
            second = int(second)
            second_int = True
        except:
            pass




    if first_int == False and second_int == False:
        if first in test and second in test:
            second_position = test.index (second)
            first_position = test.index(first) 

            test[first_position] = second
            test[second_position] = first
        else:
            print ("The names you entered aren't in the List")
    elif first_int == True and second_int == False:
        if first <= len(test) and second in test:
            test[test.index(second)] = test[first]
            test[first] = second
        else:
            print ("the number of the list item or the word is not part of the list")
    elif second_int == True and first_int == False:
        if first in test and second <= len(test):
            test[test.index(first)] = test[second]
            test[second] = first
        else:
            print ("the number of the list item or the word is not part of the list")
    else:
        if first <= len(test) and second <= len(test):
            first_position = test[first]
            second_position = test [second]

            test [first] = second_position
            test[second] = first_position
        else:
            print ("At least one of the Numbers you entered does not represent an item in the list")
        


    print (test)
    print ("")
    print ("again input")