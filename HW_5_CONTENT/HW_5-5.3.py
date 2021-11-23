from random import randrange

TIC_TAC_TOE_ROLES_MARKS = {
    "AI": "X",
    "PLAYER": "0"
}

game_end = False


def init_board():
    board = []
    current_target = 0
    for i in range(3):
        row = []
        current_target += i + 1
        for j in range(3):
            row.append(j + current_target)
        board.append(row)
        if not i:
            current_target += 1
    return board


board = init_board()


def ai_turn():
    ai_cell_turn = randrange(1, 10)
    turn_result = move(ai_cell_turn, TIC_TAC_TOE_ROLES_MARKS['AI'])
    while not turn_result:
        ai_cell_turn = randrange(1, 9)
        print('AI rerun turn with:', ai_cell_turn)
        turn_result = move(ai_cell_turn, TIC_TAC_TOE_ROLES_MARKS['AI'])
    print(turn_result)


def win_check():
    global game_end
    if [board[0][0], board[1][1], board[2][2]] == list(TIC_TAC_TOE_ROLES_MARKS['AI'] * 3):
        game_end = True
        print('AI win!', board)
    elif [board[0][0], board[1][1], board[2][2]] == list(TIC_TAC_TOE_ROLES_MARKS['PLAYER'] * 3):
        game_end = True
        print('PLAYER win!', board)
    for row in board:
        columns = [[[TIC_TAC_TOE_ROLES_MARKS['AI']], [TIC_TAC_TOE_ROLES_MARKS['AI']], [TIC_TAC_TOE_ROLES_MARKS['AI']]], [
            [TIC_TAC_TOE_ROLES_MARKS['PLAYER']], [TIC_TAC_TOE_ROLES_MARKS['PLAYER']], [TIC_TAC_TOE_ROLES_MARKS['PLAYER']]]]
        if board[board.index(row)][0] == columns[0] or board[board.index(row)][1] == columns[0] or board[board.index(row)][2] == columns[0]:
            game_end = True
            print('AI win!', board)
        elif board[board.index(row)][0] == columns[1] or board[board.index(row)][1] == columns[1] or board[board.index(row)][2] == columns[1]:
            game_end = True
            print('PLAYER win!', board)
        elif row == list(TIC_TAC_TOE_ROLES_MARKS['AI'] * 3):
            game_end = True
            print('AI win!', board)
        elif row == list(TIC_TAC_TOE_ROLES_MARKS['PLAYER'] * 3):
            game_end = True
            print('PLAYER win!', board)
        else:
            print(end='')


def move(value, mark):
    turn_ended_success = False
    win_check()
    for row in board:
        for с in row:
            if с == value:
                current_turn = [board.index(row), row.index(с)]
                board[current_turn[0]][current_turn[1]] = mark
                print(mark, 'was added to position:', current_turn)
                print(board)
                turn_ended_success = True
                return turn_ended_success
    return turn_ended_success


move(board[1][1], TIC_TAC_TOE_ROLES_MARKS['AI'])

value = input('Enter cell number to turn: ')
while not game_end:
    try:
        player_turn = move(int(value), TIC_TAC_TOE_ROLES_MARKS['PLAYER'])
        if not player_turn:
            assert()
        if not game_end:
            ai_turn()
            value = input('Enter cell number to turn: ')
    except:
        print('Please enter valid value!')
        value = input('Enter cell number to turn: ')
    win_check()
print('Game ended!')
