from random import randrange
from Packages.tictactoe import TicTacToe

GAME_ROLES = ['ai', 'player']

new_game = TicTacToe()
new_game.board_creation()

board = new_game.get_board()
is_turn_successful = new_game.turn_result()

new_game.turn(GAME_ROLES[0], board[1][1])

print('Welcome to tic tac toe game!')
print(board)
userInput = input('Enter cell number where you want put you mark: ')
while not is_turn_successful and userInput:
    ai_turn_end = False
    try:
        if not new_game.get_winner():
            while not ai_turn_end:
                ai_cell_turn = randrange(1, 10)
                new_game.turn(GAME_ROLES[0], ai_cell_turn)
                if new_game.turn_result():
                    ai_turn_end = True
            print(new_game.turn_count)
            new_game.turn(GAME_ROLES[1], int(userInput))
            print(board)
            userInput = input(
                'Enter cell number where you want put you mark: ')
        else:
            break
    except:
        print('Something are wrong!')

winner = new_game.get_winner()
print('Winner is:', winner)
