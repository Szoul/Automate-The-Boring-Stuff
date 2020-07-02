#Write a function named isValidChessBoard() that takes a dictionary
#argument and returns True or False depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white king. 
#Each player can only have at most 16 pieces, at most 8 pawns, and all 
#pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t 
#be on space '9z'. The piece names begin with either a 'w' or 'b' to represent 
#white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
#This function should detect when a bug has resulted in an improper chess board.

a_valid_chessboard = {"1h":"wking", "4d":"bking", "3f":"wqueen", "8d": "brook"}
an_invalid_chessboard = {"1h":"bking", "4d":"bking", "3k":"wqueen", "8d": "brook", "4h":"herpaderp"}

def isValidChessBoard(dict):
    error_counter = 0
    #create chess field as a list and check if every key is part of that list
    empty_chess_board = [[] for i in range(8)]
    for number in range(8):
        for letter in "abcdefgh":
            empty_chess_board[number].append(str(number+1)+letter)

    list_of_keys = list(dict.keys())
    for i in list_of_keys:
        is_on_board_counter = 0
        for x in range(len(empty_chess_board)):
            if i in empty_chess_board[x]:
                is_on_board_counter += 1
        if is_on_board_counter != 1:
            print (i + ":" + dict[i] + " is not a valid potition on a Chess board")
            error_counter += 1

    #create a dictionary of all possible pieces(keys) and their maximum numbers (values), compare with input dictionary if valid
    dictionary_of_maximum_pieces = {"bking":1, "bqueen":1, "bknight":2, "bbishop":2, "brook":2, "bpawn":8,
                                    "wking":1, "wqueen":1, "wknight":2, "wbishop":2, "wrook":2, "wpawn":8}
    list_of_values = list(dict.values())
    for i in range(len(list_of_values)):
        if list_of_values[i] in dictionary_of_maximum_pieces.keys():
            dictionary_of_maximum_pieces[list_of_values[i]] -= 1
        else:
            print (list_of_values[i] + " is not a valid Chess-Figure")
            error_counter += 1

    if dictionary_of_maximum_pieces["bking"] > 0:
        print ("your game is missing a black king")
        error_counter += 1
    if dictionary_of_maximum_pieces["wking"] > 0:
        print ("your game is missing a white king")
        error_counter += 1
    
    for x in list(dictionary_of_maximum_pieces.keys()):
        if dictionary_of_maximum_pieces.get(x) < 0:
            difference = abs(dictionary_of_maximum_pieces.get(x))
            print ("There are " + str(difference) + " more than the allowed number of " + x + " on your field")
            error_counter += 1
    
    #returnvalue True if everything correct, otherwise False
    if error_counter > 0:
        print ("\n\n\nYour Chessboard currently has " + str(error_counter) + " non-valid potitions or figures")
        return False
    else:
        print ("\n\n\nYour Chessboard is valid")
        return True

isValidChessBoard(a_valid_chessboard)
print ("\n\n")
isValidChessBoard(an_invalid_chessboard)
input("\n\nAny Input will end the Programm")