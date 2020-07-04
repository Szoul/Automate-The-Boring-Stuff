"""Write a function named printTable() that takes a
 list of lists of strings and displays it in a 
 well-organized table with each column right-justified. 
 Assume that all the inner lists will contain the same 
 number of strings. For example, the value could look like 
 this: """
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
"""Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose"""


def printTable(list_of_lists):
    new_list = [[]for i in range(len(list_of_lists))]
    for i in range(len(list_of_lists)):
        length = 0
        for word in list_of_lists[i]:
            current_length = len(word)
            if length < current_length:
                length = current_length
        for word in list_of_lists[i]:
            new_list[i].append(word.rjust(length))
    
    for x in range(len(new_list[0])):
        for i in range(len(new_list)):
            print (new_list[i][x] + " ", end ="")
        print ("")

printTable(tableData)
input()

#TO-DO:
    #Find longest string in each list for all words to adjust to
    #adjust all words in each list to the right side with item.rjust(lenght of longest string in list," ")
    #print list[x][y] + list[x+1][y] + ... in a for loop(within a for loop)
