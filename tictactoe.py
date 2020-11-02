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
# 3º Place their input on the board.
# 4º Check if the game is won,tied, lost, or ongoing.
# 5º Repeat 2º and 3ª until the game has been won or tied.
# 6º Ask if players want to play again.
board()
