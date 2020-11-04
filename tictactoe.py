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

   # return b
test = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
board(test)


def player_input():
    '''Collects player one marker choice and assign a marker to player two based on player one marker choice'''
    marker = ''
    while marker != 'X' and marker != 'O':
        print('Player One, please choose a marker between X or O to begin your game:')
        marker = input()
        if marker != 'X' or marker != 'O':
            print('Wrong choice!')
    p1 = marker
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    print(f'Player One chose {p1}, so Player Two your marker is {p2}')
    return (p1, p2)


p1_marker, p2_marker = player_input()


def place_marker(test, marker):
    '''Places the player marker in the the selected board index'''
    position = int(
        input('Enter a position to from 1 to 9 for assign your marker: '))
    test[position] = marker
    return test

# 4º Check if the game is won,tied, lost, or ongoing.
# 5º Repeat 2º and 3ª until the game has been won or tied.
# 6º Ask if players want to play again.


board(test)
place_marker(test, 'X')
board(test)
