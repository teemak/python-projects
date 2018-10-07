from IPython.display import  clear_output

def display_board(board):
    clear_output()
    wall = ' | '
    floor = '-'
    print(' ' + floor * 13)
    print(wall + board[7] + wall + board[8]  + wall + board[9] + wall)
    print(' ' + floor * 13)
    print(wall + board[4] + wall + board[5]  + wall + board[6] + wall)
    print(' ' + floor * 13)
    print(wall + board[1] + wall + board[2]  + wall + board[3] + wall)
    print(' ' + floor * 13)

test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)

def player_input():
    marker = ''

    while marker != 'X' and marker !=  'O':
        marker = input('Do you want X or O? (X goes first) ').upper()

    ''' while not (marker == 'X' or marker == 'O'):
        player_1 = marker
    if player_1 == 'X':
        player_2 = '0'
    else:
        player_2 = 'X'
    return (player_1, player_2)'''

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

player_1_marker, player_2_marker = player_input()

#print(f'Player One is {player_1_marker}')

def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board, '$', 8)
display_board(test_board)
