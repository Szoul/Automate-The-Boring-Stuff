import random
my_family = []

def show_list():
    for family_index, name in enumerate(my_family):
        print ("Number " + str(family_index + 1) + " is called '" + str(name) + "'")

print ("Please enter your family member's names one by one; Enter 'Done' when you're finished")

while True:
    name = str(input())
    if name == 'Done':
        break
    my_family += [name]

print ("Your family has " + str(len(my_family)) + " members named: ")
for i in range(len(my_family)):
    print (my_family[i] + ", ", end='')       

print ("")
print ("would you like me to list and/or change them again?, if so type 'Yes', otherwise press Enter")
print ("")
ask_for_listing = input()
if ask_for_listing == 'Yes':
    show_list()

    print ("would you like to change, or randomize their order? If so type in 'change' or 'randomize', otherwise press Enter")
    ask_for_randomize_or_change = input()
    print ("")
    if ask_for_randomize_or_change == 'randomize':
        random.shuffle(my_family)
    elif ask_for_randomize_or_change == 'change':
        print ("if you would like to change the order, enter the name of the first person and press enter, then do so again with the person you want to change him/her with")
        print ("you can also change them by entering the respective number of the first member you want to change and press enter and do so with the other member again")
        print ("If you changed your mind or would like to stop, enter 'Stop'")


        while True:
            print ("first name or number:")
            first_name_change = input()
            if first_name_change == 'Stop':
                break
            print ("name or number that you want to change with:")
            second_name_change = input()
            print ("")

            first_int = False
            second_int = False
            try:
                first_name_change = int(first)
                first_int = True
                second_name_change = int(second)
                second_int = True
            except:
                try:
                    second_name_change = int(second)
                    second_int = True
                except:
                    pass

            if first_int == False and second_int == False:
                if first in my_family and second in my_family:
                    second_position = my_family.index (second)
                    first_position = my_family.index(first) 

                    my_family[first_position] = second
                    my_family[second_position] = first
                else:
                    print ("The names you entered aren't in the List")
            elif first_int == True and second_int == False:
                if first <= len(my_family) and second in my_family:
                    my_family[my_family.index(second)] = my_family[first]
                    my_family[first] = second
                else:
                    print ("the number of the list item or the word is not part of the list")
            elif second_int == True and first_int == False:
                if first in my_family and second <= len(my_family):
                    my_family[my_family.index(first)] = my_family[second]
                    my_family[second] = first
                else:
                    print ("the number of the list item or the word is not part of the list")
            else:
                if first <= len(my_family) and second <= len(my_family):
                    first_position = my_family[first]
                    second_position = my_family [second]

                    my_family [first] = second_position
                    my_family[second] = first_position
                else:
                    print ("At least one of the Numbers you entered does not represent an item in the list")




            if second_name_change == 'Stop':
                break
            if first_name_change in my_family and second_name_change in my_family:
                first_name_change_position = my_family.index(first_name_change)
                second_name_change_position = my_family.index(second_name_change)

                my_family[first_name_change_position] = second_name_change
                my_family[second_name_change_position] = first_name_change 
            else:
                print ("Your Input did not match what is in the List, please only Enter contents of the List to change it, Enter 'Stop' to exit this function")
                print ("")
        

                
# REPLACE COPIED CODE NAMES