board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "bl": " ", "bm": " ", "br": " "}
board_options = list(board.keys())
board_values = list(board.values())

tl = board_values[0]
tm = board_values[1]
tr = board_values[2]
ml = board_values[3]
mm = board_values[4]
mr = board_values[5]
bl = board_values[6]
bm = board_values[7]
br = board_values[8]

def match(a,b,c):
    if a == b:
    else:
        return False
       
def match_check():
    if match(tl,tm,tr):
        return True
    if match(tl,mm,br):
        return True
    if match(tl,ml,bl):
        return True
    if match(tm,mm,bm):
        return True
    if match(br,bm,bl):
        return True
    if match(br,mr,tr):
        return True
    if match(ml,mm,mr):
        return True
    if match(bl,mm,tr):
        return True
    
def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["bl"] + "|" + board["bm"] + "|" + board["br"])

turn = "X"
winner = 0

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
