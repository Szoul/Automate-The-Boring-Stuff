import random, sys
my_family = []

def show_list():
    for family_index, name in enumerate(my_family):
        print ("Number " + str(family_index + 1) + " is called '" + str(name) + "'")
    print ("_____________________________")

print ("Please enter your family member's names; press enter after each name; Enter 'Done' when you're finished")

while True:
    name = str(input())
    if name.lower() == 'done':
        break
    my_family += [name]

print ("")
print ("would you like to work on the list?, if so type 'Yes'and press enter, otherwise press just enter")
print ("")

while True:
    ask_for_listing = input()
    print ("")

    if ask_for_listing.lower() == 'yes':
        show_list()

        print ("Type in 'change' for changing the order the listed items")
        print ("        'randomize' to randomly mix the items")
        print ("        'add' to add additional items")
        print ("        'insert' to add an item at a specific potition")
        print ("        'remove' to remove an item at a specific potition")
        print ("        'sort' to sort the list in alphabetical order")
        print ("        any other input to leave this function")
        print ("")
        ask_for_randomize_or_change = input()
        print ("")
        if ask_for_randomize_or_change == 'randomize':
            print ("_____________________________")
            print ("ok it is shuffled now")
            random.shuffle(my_family)
        elif ask_for_randomize_or_change == 'change':
            print ("_____________________________")
            print ("if you would like to change the order, enter the name of the first person and press enter, then do so again with the person you want to change him/her with")
            print ("you can also change them by entering the respective number of the first member you want to change and press enter and do so with the other member again")
            print ("_____________________________")
            print ("If you changed your mind or would like to stop, enter 'done'")
            print ("If you would like to see the current list, type in 'list'")

            while True:
                print ("first name or number:")
                first_name_change = input()
                if first_name_change.lower() == 'done':
                    break
                elif first_name_change == "list":
                    show_list()
                    continue
                print ("name or number that you want to change with:")
                second_name_change = input()
                print ("")
                if second_name_change.lower == 'done':
                    break
                elif second_name_change == "list":
                    show_list()
                    continue

                first_int = False
                second_int = False
                try:
                    first_name_change = int(first_name_change)
                    first_name_change -= 1
                    first_int = True
                    second_name_change = int(second_name_change)
                    second_name_change -= 1
                    second_int = True
                except:
                    try:
                        second_name_change = int(second_name_change)
                        second_name_change -= 1
                        second_int = True
                    except:
                        pass

                if first_int == False and second_int == False:
                    if first_name_change in my_family \
                        and second_name_change in my_family:

                        second_position = my_family.index (second_name_change)
                        first_position = my_family.index(first_name_change) 

                        my_family[first_position] = second_name_change
                        my_family[second_position] = first_name_change
                    else:
                        print ("The names you entered aren't in the List")
                elif first_int == True \
                        and second_int == False:
                    if first_name_change < len(my_family) and second_name_change in my_family:
                        my_family[my_family.index(second_name_change)] = my_family[first_name_change]
                        my_family[first_name_change] = second_name_change
                    else:
                        print ("the number of the list item or the word is not part of the list")
                elif second_int == True \
                        and first_int == False:
                    if first_name_change in my_family and second_name_change < len(my_family):
                        my_family[my_family.index(first_name_change)] = my_family[second_name_change]
                        my_family[second_name_change] = first_name_change
                    else:
                        print ("the number of the list item or the word is not part of the list")
                elif first_int == True \
                        and second_int == True:
                    if first_name_change < len(my_family) and second_name_change < len(my_family):
                        first_position = my_family[first_name_change]
                        second_position = my_family [second_name_change]

                        my_family [first_name_change] = second_position
                        my_family[second_name_change] = first_position
                    else:
                        print ("At least one of the Numbers you entered does not represent an item in the list")
        elif ask_for_randomize_or_change == "add":
            print ("_____________________________")
            print ("Write the name you want to add and press Enter")
            print ("to review the list type in 'show' and press Enter")
            print ("When you are done write 'Done' and press Enter")
        
            while True:
                print ("")
                add_to_list = input()

                if add_to_list.lower() == "show":
                    show_list()
                elif add_to_list.lower() == "done":
                    break
                else:
                    my_family.append(add_to_list)
        
        elif ask_for_randomize_or_change == "insert":
            print ("_____________________________")
            print ("to insert an item write the name you want to add and press enter. Then write the potition in the List as a number where you want to add it and press enter again")
            print ("write 'done' to exit this function")
            print ("write 'show' to review the list")
            print ("")
            while True:
                print ("Enter the name you want to add")
                insert_to_list = input()
                if insert_to_list.lower() == "done":
                    break
                elif insert_to_list.lower() == 'show':
                    show_list()
                    continue
                print ("Now Enter the Potition")
                print ("")
                
                while True:
                    if insert_to_list.lower() == "show":
                        show_list()
                    try:
                        insert_to_list_potition = int(input())
                        break
                    except:
                        print ("Please enter a Number inside the list. Type in 'show' to review the list")
                        print ("")

                if insert_to_list.lower == "done":
                    break
                elif insert_to_list_potition == "show":
                    show_list()
                    continue
                
                try:
                    my_family.insert(insert_to_list_potition-1, insert_to_list)
                    print (my_family[insert_to_list-1] + " has been added at potition " + insert_to_list_potition)
                except:
                    print ("The number you entered is not within the current list; Type 'show' to see which numbers are possible")
                
        elif ask_for_randomize_or_change == "remove":
            print ("_____________________________")
            print ("To remove an item from the list enter the item's name or its respective number")
            print ("To show your current list enter 'show' ")
            print ("If you want to exit this function enter 'done'")
            print ("")

            while True:
                removing_item = input()
                if removing_item.lower() == "show":
                    show_list()
                    continue
                elif removing_item.lower() == "done":
                    break

                try:
                    test_int = False
                    removing_item = int(removing_item)
                    test_int = True
                except:
                    pass
                
                try:
                    if test_int == False:
                        my_family.remove(removing_item)
                        print ("removed " + removing_item + " from the list")
                        print ("_____________________________")
                    elif test_int == True:
                        removed_name = my_family[removing_item-1]
                        my_family.remove(my_family[removing_item-1])
                        print (removed_name + " has been removed from the list")
                except:
                    print ("The number or Word you entered is not part of the list. Please pay attention to upper and lower case")
                    print ("enter 'done' if you want to exit this function")
                    print ("_____________________________")
    
        elif ask_for_randomize_or_change.lower() == "sort":
            my_family.sort()
            print ("the list has been sorted")

        print("_____________________________")
        print ("You did exit the function")
        print ("Do you want to continue working on your list? If so write 'Yes' and Press enter; otherwise Press enter to show the finsihed list")


    else:
        break

print ("")
print ("Here is your finished List:")
print ("_____________________________")
print ("")
show_list()

print ("_____________________________")
print("Press enter to exit")
input()
sys.exit(0)