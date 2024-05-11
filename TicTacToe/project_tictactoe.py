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
    
# draw_move(board)
# display_board(board)
# draw_move(board)
# display_board(board)
# draw_move(board)
# display_board(board)
# draw_move(board)
# display_board(board)
# enter_move(board)
# display_board(board)
# board_x0 = [["X", "X", "X"], ["4", "X", "6"], ["7", "8", "9"]]
# print(victory_for(board_x0, "X"))
# board_x1 = [["1", "2", "3"], ["X", "X", "X"], ["7", "8", "9"]]
# print(victory_for(board_x1, "X"))
# board_x2 = [["1", "2", "3"], ["4", "X", "6"], ["X", "X", "X"]]
# print(victory_for(board_x2, "X"))
# board_y0 = [["X", "2", "3"], ["X", "X", "6"], ["X", "8", "9"]]
# print(victory_for(board_y0, "X"))
# board_y1 = [["1", "X", "3"], ["4", "X", "6"], ["7", "X", "9"]]
# print(victory_for(board_y1, "X"))
# board_y2 = [["1", "2", "X"], ["4", "X", "X"], ["7", "8", "X"]]
# print(victory_for(board_y2, "X"))

# board_c1 = [["X", "2", "3"], ["4", "X", "6"], ["7", "8", "X"]]
# print(victory_for(board_c1, "X"))
# board_c2 = [["1", "2", "X"], ["4", "X", "6"], ["X", "8", "9"]]
# print(victory_for(board_c2, "X"))

