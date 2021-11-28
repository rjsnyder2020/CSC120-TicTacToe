board = ['-','-','-','-','-','-','-','-','-']
game_status = True
def print_board():
    print(board[0] + ' ' + board[1] + ' ' + board[2])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[6] + ' ' + board[7] + ' ' + board[8])
def player_turn(current):
    player1 = input("Choose a position (1-9): ")
    player1 = int(player1) - 1
    board[player1] == 'X'
    player2 = input("Choose a position (1-9): ")
    player2 = int(player2) -1
    board[player2] == 'O'
def game_start():
    print_board()
    while game_status == True:
        player_turn()
        swap_turn()
        print_board()
    win()
def swap_turn():
    global current
    global player1
    global player2
    if current == player1:
        current = player2
    elif current == player2:
        current = player1
def win():
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        game_status = False
        print("Player 1 Wins")
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        game_status = False
        print("Player 1 Wins")

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        game_status = False
        print("Player 2 Wins")
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        game_status = False
        print("Player 2 Wins")
def tie():
    game_status = False
    print("It's a Tie")
