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

#finds rows and columns
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))


#DEBUGGING NOT CHEATING
from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#prints the debugging statement
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
print ship_col
print ship_row

#You WIn!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"

#you missed
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
    board[int(guess_row)][int(guess_col)] = "X"
    print_board(board)


    #NOT AGAIN
    from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    print "Turn", turn + 1

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print_board(board)

    if turn == 3:
        print "Game Over"

        #breaking after win
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    print "Turn", turn + 1

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        #ADICIONADO NESTE EXERCICIO
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print_board(board)

    if turn == 3:
        print "Game Over"
