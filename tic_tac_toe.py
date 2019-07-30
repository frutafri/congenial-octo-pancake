#Tic Tac Toe
board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "bl": " ", "bm": " ", "br": " "}

board_options = list(board.keys())
turn = "X"
winner = 0

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
    if match(board["tr"],board["mm"],board["tr"]):
        return True

#Illustrates board during the game
    
def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["bl"] + "|" + board["bm"] + "|" + board["br"])

#Player input and calls for a match check

while not winner:
    print("Player " + turn + " take your turn!")
    location = input()
    if location in board.keys():
        board[location] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        print_board(board)
        
        if match_check():
            print("We have a winner!")
            break

    else:
        continue
