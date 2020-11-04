from os import system, name


def clear():
    '''Clears the screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def board(b):
    '''Prints the board to the players'''
    clear()
#    b = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('\n')
    print('  #TIC #TAC #TOE BOARD')
    print('\n')
    print('=========================')
    print('|       |       |       |')
    print(f'|   {b[1]}   |   {b[1]}   |   {b[3]}   |')
    print('|       |       |       |')
    print('=========================')
    print('|       |       |       |')
    print(f'|   {b[4]}   |   {b[5]}   |   {b[6]}   |')
    print('|       |       |       |')
    print('=========================')
    print('|       |       |       |')
    print(f'|   {b[7]}   |   {b[8]}   |   {b[9]}   |')
    print('|       |       |       |')
    print('=========================')
    print('\n')


   # return b
test = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
board(test)


def player_input():
    '''
    Collects player one marker choice and assign a marker to player two based on player one marker choice
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        print('Player One, please choose a marker between X or O to begin your game:')
        marker = input().upper()
        if marker != 'X' or marker != 'O':
            print('Wrong choice!')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


p1_marker, p2_marker = player_input()


def place_marker(test, marker, position):
    '''
    Places the player marker in the the selected board index
    '''
    position = int(
        input('Enter a position to from 1 to 9 for assign your marker: '))
    test[position] = marker


def win_check(board, marker):
    '''
    Checks if the game is won
    '''
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))

# 5º Repeat 2º and 3ª until the game has been won or tied.
# 6º Ask if players want to play again.


board(test)
board(test)
