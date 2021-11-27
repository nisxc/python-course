class TicTacToe:

    def __init__(self):
        self._marks = {
            "ai": "X",
            "player": "O"
        }
        self.turn_count = 1
        self._board = None
        self._winner = None
        self._is_successful = False

    def board_creation(self):
        _temp = []
        _turn = 0
        for i in range(3):
            _row = []
            for j in range(3):
                _turn += 1
                _row.append(_turn)
            _temp.append(_row)
        self._board = _temp

    def get_board(self):
        temp = self._board[:]
        return temp

    def get_winner(self):
        temp = self._winner
        return temp

    def turn_result(self):
        temp = self._is_successful
        return temp

    def win_check(self, who):
        if [self._board[0][0], self._board[1][1], self._board[2][2]] == list(self._marks[who] * 3) \
                or [self._board[0][0], self._board[1][0], self._board[2][0]] == list(self._marks[who] * 3) \
            or [self._board[0][1], self._board[1][1], self._board[2][1]] == list(self._marks[who] * 3) \
                or [self._board[0][2], self._board[1][2], self._board[2][2]] == list(self._marks[who] * 3):
            self._winner = who
        for row in self._board:
            if row == list(self._marks[who] * 3):
                self._winner = who
        if self.turn_count >= 9 and not self._winner:
            self._winner = 'friendship'

    def turn(self, who, where):
        self._is_successful = False
        for row in self._board:
            for cell in row:
                if cell == where and where not in self._marks.values():
                    self._board[self._board.index(
                        row)
                    ][row.index(cell)] = self._marks[who]
                    self._is_successful = True

        if self._is_successful:
            self.turn_count += 1
        self.win_check(who)
