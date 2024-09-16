from PROJECT_TicTacToe import display_board
from PROJECT_TicTacToe import get_indices
from PROJECT_TicTacToe import enter_move
from PROJECT_TicTacToe import victory_for
from PROJECT_TicTacToe import draw_move
from PROJECT_TicTacToe import make_list_of_free_fields
from random import randrange

board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]

while True:
    display_board(board)
    enter_move(board)
    if victory_for(board, "0"):
        print("You have won!")
        break
    draw_move(board)
    if victory_for(board, "X"):
        print("Computer has won!")
        break    
 
 
display_board(board)
 

