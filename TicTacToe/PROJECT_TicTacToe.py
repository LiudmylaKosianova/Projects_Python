from random import randrange

def display_board(board):

    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """
    #create the zero's two dimensional list for printing
    listBoard = [[0 for _ in range(25)] for _ in range(13)]
    for x in range(13):
        for y in range(25):
            if x%4==0:
                if y%8==0:
                    listBoard[x][y] = "+"
                else:
                    listBoard[x][y] = "-"
            else:
                if y%8==0:
                    listBoard[x][y] = "|"
                else:
                    listBoard[x][y] = " "
    # flatten the board two dimensional list into one dimensional moves list
    moves = []
    for i in board:
        for j in i:
            moves.append(j)
        
    # put the moves in the board for printing
    x_s = [2,6,10]
    y_s = [4,12,20]
    index_moves = 0
    for x in x_s:
        for y in y_s:
            listBoard[x][y] = moves[index_moves]
            index_moves+=1
    
    # finally prints the board 
    print("\n*** CURRENT BOARD STATE ***\n")
    for x in range(13):
        for y in range(25):
            print(listBoard[x][y], end="")
        print()
    print()

def get_indices(number):
    """
    returns a tuple, that represent the location on the board
    """
    ind_list = []
    for x in range(3):
        for y in range(3):
            ind_list.append((x,y))
    
    return ind_list[number-1]

def enter_move(board):
    """
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    """
    move = input("Enter your move:")
    if int(move)<=9 and int(move)>=1:
        x, y = get_indices(int(move))
        if board[x][y] != "0" and board[x][y] != "X":
            board[x][y] = "0"

def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """
    free = []
    for x in range(3):
        for y in range(3):
            if board[x][y] != "X" and board[x][y] != "0":
                free.append((x,y))
    return free


def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game
    """
    victory = True

    # check for victory in horizontal lines(rows)
    for x in board:
        victory = True
        for y in x:
            if y!=sign:
                victory = False
                break
        if victory:
            return victory

    #check for victory in vertical lines(columns)
    for y in range(3):
        victory = True
        for x in range(3):
            if board[x][y] != sign:
                victory = False
                break
        if victory:
            return victory
    
    if sign == "X":
        victory = True
        for x, y in zip(range(3), range(3)):
            if board[x][y] != "X":
                victory = False
                break
        if victory:
            return victory
        victory = True
        for x, y in zip(range(3),range(2, -1, -1)):
            if board[x][y] != "X":
                victory = False
                break
        if victory:
            return victory

    return victory

def draw_move(board):
    """
    The function draws the computer's move and updates the board.
    """
    free = make_list_of_free_fields(board)
    
    move = randrange(0, len(free))
    x,y = free[move]
    board[x][y] = "X"

