import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, row, column, piece):
    # Horizontal checking
    count = 0
    for col in range(max(0, column - 3), min(COLUMN_COUNT, column + 4)):
        if board[row][col] == piece:
            count += 1
        else:
            count = 0
        if count >= 4:
            return True

    # Vertical checking
    count = 0
    for r in range(max(0, row - 3), min(ROW_COUNT, row + 4)):
        if board[r][column] == piece:
            count += 1
        else:
            count = 0
        if count >= 4:
            return True
    
    


board = create_board()
print_board(board)
game_over = False
turn = 0


while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, row, col, 1):
                print_board(board)
                print("Player 1 wins the game")
                game_over = True
                break

    # Ask for player 2 input 
    else:
        col = int(input("Player 2, Make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, row, col, 2):
                print_board(board)
                print("Player 2 wins the game")
                game_over = True
                break

    print_board(board)
    turn += 1
    turn = turn % 2
