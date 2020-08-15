import sys


class Game:
    winConditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 7)]
    validMoves = [str(x) for x in range(1, 10)]
    board = []
    _movecount = 0
    _lastMove = 0
    _activeGrid = 0
    _whosMove = "x"

    @property
    def activeGrid(self):
        out = ["A", "B", "C"][int(self._activeGrid / 3)]
        out += str((self._activeGrid % 3) + 1)
        if self.won:
            out = "N/A"
        return out

    @property
    def currentMove(self):
        return self._currentMove

    def __init__(self):
        self.won = False
        self.reset_game()

    def get_board(self):
        return self.board

    def reset_game(self):
        self.won = False
        self._activeGrid = 4
        self._currentMove = 0
        self._whosMove = "x"
        self.board = [[" "] * 9, [" "] * 9, [" "] * 9,
                      [" "] * 9, [" "] * 9, [" "] * 9,
                      [" "] * 9, [" "] * 9, [" "] * 9]

    def play(self, position):
        pos = int(position) - 1
        self._currentMove += 1
        if self.board[self._activeGrid][pos] == " ":
            self.board[self._activeGrid][pos] = self._whosMove
            self._activeGrid = pos
            self.check_win()
            if self.won:
                return

            if self._whosMove == "x":
                self._whosMove = "o"
            else:
                self._whosMove = "x"

            self.check_next_grid()
        else:
            print("Invalid position.")

    def check_win(self):
        wonBoards = [" "] * 9

        for i in range(9):
            result = self.check_board(self.board[i])
            wonBoards[i] = result

        result = self.check_board(wonBoards)
        if result != " ":
            self.won = True

    def check_board(self, board: list) -> str:
        winner = " "

        for winSet in self.winConditions:
            i, j, k = winSet
            if board[i] != " " and board[i] == board[j] == board[k]:
                winner = board[j]

        return winner

    def check_next_grid(self):
        if " " not in self.board[self._activeGrid]:
            newGrid = ""
            validGrids = self.validMoves
            
            while newGrid not in validGrids:
                prompt = f"{self._whosMove}, choose your grid: "
                newGrid = input(prompt)

                cond1 = newGrid not in validGrids
                cond2 = int(newGrid) - 1 == self._activeGrid
                if cond1 or cond2:
                    print("Invalid grid selection.")
                    newGrid = ""
                else:
                    self._activeGrid = int(newGrid) - 1
