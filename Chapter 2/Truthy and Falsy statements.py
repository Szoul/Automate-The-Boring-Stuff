name = ''
while not name:                         #while not True > name ist "True" solang
                                        #der string leer ist
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:                         #if True > numOfGuests ist "True" solang
                                        #es einen Wert != 0 hat
    print('Be sure to have enough room for all your guests.')
print('Done')
