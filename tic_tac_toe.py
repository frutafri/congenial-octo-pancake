board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "bl": " ", "bm": " ", "br": " "}
board_options = list(board.keys())

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
    else:
        continue
            
