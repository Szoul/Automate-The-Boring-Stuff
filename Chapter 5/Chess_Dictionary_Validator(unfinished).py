#Write a function named isValidChessBoard() that takes a dictionary
#argument and returns True or False depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white king. 
#Each player can only have at most 16 pieces, at most 8 pawns, and all 
#pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t 
#be on space '9z'. The piece names begin with either a 'w' or 'b' to represent 
#white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
#This function should detect when a bug has resulted in an improper chess board.

a_valid_chessboard = {"1h":"wking", "4d":"bking", "3f":"wqueen", "8d": "brook" }
an_invalid_chessboard = {"1h":"bking", "4d":"bking", "3k":"wqueen", "8d": "brook"}

def isValidChessBoard(dict):
    #pieces must be on a valid board (from 1-8 and a-h)
    #create chess field as a list
    empty_chess_board = [[] for i in range(8)]
    for number in range(8):
        for letter in "abcdefgh":
            empty_chess_board[number].append(letter+str(number+1))
    #check if ever key is part of list
    for i in dict.keys():
        print (i)
        if any (i in sublist for sublist in empty_chess_board):
            print (i + ":" + dict[i] + " is not a valid place on a chess board") #returnvalue false; print

    #names begin with w or b - then by name of the figure - then potition (example: {"3d":"wking",...})
    # max 16 pieces for EACH colour
    # only one King/Queen of each color
    # 8 pawn
    # 2 knights/bishops/rook



    #return TRUE or FALSE

    # if false return the "bug"
isValidChessBoard(a_valid_chessboard)