"""
Scenario
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. 
The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") 
of the table must contain all digits from 0 to 9.


Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits 
(check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
"""
def lineIsValid(line):
    #line should be sudoku valid
    rowList = list(line)
    rowList.sort()
    digitList = [str(x) for x in range(1,10,1)]     
    return rowList == digitList

def inputIsValid(input):
    #input should be a string containing only digits from '1' to '9'
    if len(input) != 9 or not input.isdigit():
        return False
    return True

def boardIsSudoku(board):
    #board is a list of nine strings
    sudoku = True
    for row in board:
        if not lineIsValid(row):
            return False    
    
    for i in range(9):
        column = ""
        for j in range(9):
            column += board[j][i]
        if not lineIsValid(column):
            return False
    
    miniBoards = []
    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(3):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""

    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(3,6,1):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""
    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(6,9,1):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""
    
    for line in miniBoards:
        if not lineIsValid(line):
            return False
    return True
    
print(boardIsSudoku(["295743861",
                          "431865927", 
                          "876192543", 
                          "387459216",
                          "612387495",
                          "549216738",
                          "763524189",
                          "928671354",
                          "154938672"]))
