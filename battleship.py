#creating a grid size of Os
board = []
for i in (range(0,5)):
    result = ["O"] * 5
    board.append(result)
    print board



#printing row by row of the board lists
board = []
for i in (range(0,5)):
    result = ["O"] * 5
    board.append(result)
def print_board(board):
    for row in board:
        print row



#printing pretty
board = []
for i in (range(0,5)):
    result = ["O"] * 5
    board.append(result)
def print_board(board):
    for row in board:
        print " ".join(row)

#hiding some elements from the user
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)
board
# Add your code below!
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board) - 1)

print random_row(board)
print random_col(board)


