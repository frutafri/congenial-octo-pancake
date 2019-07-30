#Tic Tac Toe

board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "bl": " ", "bm": " ", "br": " "}

board_options = list(board.keys())
turn = "X"
winner = 0
turn_number = 0

#Functions that check for a winner:

def match(a,b,c):
    if a == b and b == c:
        if a != " " and b != " " and c != " ":
            return True
    else:
        return False
       
def match_check():
    if match(board["tl"],board["tm"],board["tr"]):
        return True
    if match(board["tl"],board["mm"],board["br"]):
        return True
    if match(board["tl"],board["ml"],board["bl"]):
        return True
    if match(board["tm"],board["mm"],board["bm"]):
        return True
    if match(board["br"],board["bm"],board["bl"]):
        return True
    if match(board["br"],board["mr"],board["tr"]):
        return True
    if match(board["ml"],board["mm"],board["mr"]):
        return True
    if match(board["tr"],board["mm"],board["bl"]):
        return True

#Illustrates board during the game:
    
def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["bl"] + "|" + board["bm"] + "|" + board["br"])
    print()

#Illustrates the layout of grid for the beginning of game:

def print_board_layout():
    print()
    print("Choices:")
    print()
    print("tl|tm|tr")
    print("--+--+--")
    print("ml|mm|mr")
    print("--+--+--")
    print("bl|bm|br")
    print()

#Player input and calls for a match check:
    
print_board_layout()
while not winner:
    print("Player " + turn + " take your turn!")
    location = input()
    print()
    if location in board.keys() and board[location] == " ":
        board[location] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        turn_number += 1
        print_board(board)       
        if match_check():
            print("We have a winner!")
            break
        if turn_number == 9:
            print("Cat's game")
            break

    else:
        print("Input invalid")
        continue
