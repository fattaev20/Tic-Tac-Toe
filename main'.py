GAME_BOARD = ("     |     |     \n"
              " 1,1 | 1,2 | 1,3 \n"
              "-----|-----|-----\n"
              " 2,1 | 2,2 | 2,3 \n"
              "-----|-----|-----\n"
              " 3,1 | 3,2 | 3,3 \n"
              "     |     |     \n")

game_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

game_over = False
turn = 1
moves = 0
used_moves = []


def check():
    global game_over
    if game_board[0][0] == game_board[0][1] and game_board[0][2] == game_board[0][1] and game_board[0][0] == \
            game_board[0][2]:
        game_over = True
    elif game_board[1][0] == game_board[1][1] and game_board[1][2] == game_board[1][1] and game_board[1][0] == \
            game_board[1][2]:
        game_over = True
    elif game_board[2][0] == game_board[2][1] and game_board[2][2] == game_board[2][1] and game_board[2][0] == \
            game_board[2][2]:
        game_over = True
    elif game_board[0][0] == game_board[1][0] and game_board[0][0] == game_board[2][0] and game_board[1][0] == \
            game_board[2][0]:
        game_over = True
    elif game_board[0][1] == game_board[1][1] and game_board[0][1] == game_board[2][1] and game_board[1][1] == \
            game_board[2][1]:
        game_over = True
    elif game_board[0][2] == game_board[1][2] and game_board[0][2] == game_board[2][2] and game_board[1][2] == \
            game_board[2][2]:
        game_over = True
    elif game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2] and game_board[1][1] == \
            game_board[2][2]:
        game_over = True
    elif game_board[0][2] == game_board[1][1] and game_board[0][2] == game_board[2][0] and game_board[1][1] == \
            game_board[2][0]:
        game_over = True


print(game_board[1][:])

# Explaining the rules
print("How to play: Just enter the coordinates where you want to put X or O\n"
      "Ex: Player number 1: 3,3\n\n"
      "GAME BOARD:\n\n"
      "      |     |     \n"
      "   -  |  -  |  -  \n"
      "------|-----|-----\n"
      "   -  |  -  |  -  \n"
      "------|-----|-----\n"
      "   -  |  -  |  X  \n"
      "      |     |     \n")

player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")

while not game_over and moves <= 9:

    coor = input(f"Player number {turn}: ")
    while coor in used_moves:
        print("This move is used choose different one")
        coor = input(f"Player number {turn}: ")

    if turn == 1:
        GAME_BOARD = GAME_BOARD.replace(coor, " X ")
    else:
        GAME_BOARD = GAME_BOARD.replace(coor, " O ")

    x = int(coor[0])-1
    y = int(coor[2])-1

    if turn == 1:
        game_board[x][y] = "X"
    else:
        game_board[x][y] = "Y"

    print(game_board)
    print(GAME_BOARD)
    check()
    used_moves.append(coor)
    moves = moves + 1

    if turn == 1:
        turn = 2
    else:
        turn = 1

    if game_over:
        print("GAME OVER !")
        if turn == 2:
            print(f"{player1} wins !")
        else:
            print(f"{player2} wins !")

    else:
        print("GAME OVER ! DRAW")
