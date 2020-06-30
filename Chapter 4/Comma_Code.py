spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all 
#the items separated by a comma and a space, with and inserted before the last item. 
#For example, passing the previous spam list to the function would return 
#'apples, bananas, tofu, and cats'. But your function should be able to work with any 
#list value passed to it. Be sure to test the case where an empty list [] is passed to your function

spam2 = ['apples', 'bananas', 'tofu', 'cats', True, 0, 0.1]
spam3 = ["Hello, World"]
spam4 = []

def printlist (yourlist):
    if len(yourlist) > 2:
        newstring = str(yourlist[0])
        for current_item in range (1, len(yourlist)-1):
            newstring = newstring + ", " + str(yourlist[current_item])
        newstring = newstring + ", and " + str(yourlist[-1])
        return newstring
    elif len(yourlist) == 1:
        return str(yourlist[0])
    else:
        return None         #return "This list has no values in it"

print (printlist(spam))
print (printlist(spam2))
print (printlist(spam3))
print (printlist(spam4))