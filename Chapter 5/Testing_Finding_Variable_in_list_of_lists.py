height = 5
listwithinlists = [[] for i in range (height)]

for i in range (height):
    for letter in "abcd":
        listwithinlists[i].append(str(i)+str(letter))

for y in range (height):
    for x in range (4):
        print (listwithinlists[y][x] + " ", end ="")
    print ("")

variable_True = "1b"
variable_False = "123bhd"
list_True = ["1a", "2b", "4a"]
list_partially_False = ["123bd", "5423ac", "29ü", "1a"]
dict_True = {"1a":"1a", "2b":"2b", "4a":"3c"}
dict_partially_False = {"123bd":"123bd", "5423ac":"5423ac", "29ü":"29ü", "1a":"2b"}

def checkvariable (variable,list_to_check):              #check if variable exists in a list of lists, return exists/doesn't exist
    isinlist = False
    for i in range(len(list_to_check)):
        if variable in list_to_check[i]:
            print (str(variable) + " \u001b[35m exists  \u001b[37m in the list number " + str(i) + " of the list you checked")
            return True
            isinlist = True
        else:
            pass
    if isinlist == False:
        print (str(variable) + " is not part of the list")
        return False

def checkvariable2 (variable, list_to_check):
        if any(variable in list_to_check[i] for list_to_check[i] in list_to_check):
            print (str(variable) + " \u001b[35m exists  \u001b[37m in the list you checked")
            return True
        else:
            print (str(variable) + " is not part of the list")
            return False

def checklist (mylist,list_to_check):                      #check if all items of list exist in list of lists, return those who do/do not
    isinlist = False
    list_of_matches = []
    list_of_non_matches = []
    for i in range (len(mylist)):
        isincurrentsearch = 0
        for x in range (len(list_to_check)):
            if mylist[i] in list_to_check[x]:
                print (str(mylist[i]) + "  \u001b[35m exists  \u001b[37m in the list number " + str(x) + " of the list you checked")
                isinlist = True
                isincurrentsearch +=1
            
        if isincurrentsearch == 0:
            print (str(mylist[i]) + " does not exist in the you checked")
            list_of_non_matches.append(mylist[i])

    if isinlist == False:
        print ("No item of your list is part of the checked list")
        return mylist
    else:
        return [list_of_matches, list_of_non_matches]

def checkdictkeys (dictionary,list_to_check):           #check if all keys of a dictionary exist as items of a list, return those who do/do not
    list_of_keys = list(dictionary.keys())
    return checklist(list_of_keys, list_to_check)

print ("Check first variable:")
checkvariable2(variable_True, listwithinlists)
print ("\n___________")
print("Check second variable:")
checkvariable2(variable_False, listwithinlists)
print ("\n___________")
print("Check first list:")
checklist(list_True, listwithinlists)
print ("\n___________")
print ("Check second list:")
checklist(list_partially_False, listwithinlists)
print ("\n___________")
print ("Check first dictionary")
checkdictkeys(dict_True, listwithinlists)
print ("\n___________")
print ("Check second dictionary")
checkdictkeys(dict_partially_False, listwithinlists)