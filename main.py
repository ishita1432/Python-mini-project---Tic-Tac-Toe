import random

# Creating a sample board
def create_board():
    global board
    board=[]
    for _ in range(3):
        row=[]
        for _ in range(3):
            row.append('-')
        board.append(row)
    return board

def random_player():
    l = ['X','O']
    return random.choice(l)

def update_board(row,column,player):
    board[row][column]=player
    
def check_columns(player):
    #checking the columns
    for i in range(len(board)):
        winner = True
        for j in range(len(board)):
            if board[j][i]!=player:
                winner=False
                break
        if winner:
            return winner
        
def check_diagonals(player):   
    # checking the diagonals
    
    # left diagonal
    winner = True
    for i in range(len(board)):
        if board[i][i]!=player:
            winner=False
            break
    if winner:
        return winner
    # right diagonal
    winner = True
    for i in range(len(board)):
        j = len(board)-1-i
        if board[i][j]!=player:
            winner = False
            break
    if winner:
        return winner
    
def check_rows(player):
    # checking the rows
    for i in range(len(board)):
        winner = True
        for j in range(len(board)):
            if board[i][j]!=player:
                winner = False
                break
        if winner:
            return winner
    
def is_board_filled():
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='-':
                return False
    return True

def change_player(player):
    if player=='X':
        return 'O'
    else:
        return 'X'
    
def display_board():
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end = ' ')
        print('\r')
def start_game():
    create_board()
    player = random_player()
    while True:
        print(f"Player {player}'s turn")
        s = list(map(int,input('Enter the row and column : ').split()))
        update_board(s[0]-1,s[1]-1,player)
        if check_rows(player) or check_diagonals(player) or check_columns(player):
            display_board()
            print(f"Hurray!!! Player {player} wins the match")
            break
        if is_board_filled():
            display_board()
            print('Match draw',end=' ')
            break
        player = change_player(player)
        display_board()
        
start_game()
