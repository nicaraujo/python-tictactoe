def board():
    '''Prints the board to the players'''
    b = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('   #TIC #TAC #TOE BOARD')
    print('=========================')
    print('|       |       |       |')
    print(f'|   {b[1]}   |   {b[2]}   |   {b[3]}   |')
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

# 2º Take in player input.


def player_input():
    '''This function collects player one marker choice and assign a marker to player two based on player one marker choice'''
    marker = ''
    while marker != 'X' and marker != 'O':
        print('Player One, please choose a marker between X or O to begin your game:')
        marker = input()
    p1 = marker
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    print(f'Player One choose {p1}, so Player Two your marker is {p2}')

    # 3º Place their input on the board.
    # 4º Check if the game is won,tied, lost, or ongoing.
    # 5º Repeat 2º and 3ª until the game has been won or tied.
    # 6º Ask if players want to play again.
board()
player_input()
