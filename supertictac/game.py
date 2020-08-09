import sys

class Game:
    board = []
    _movecount = 0
    _lastMove = 0
    _activeGrid = 0
    _whosMove = "x"

    @property
    def activeGrid(self): 
        out = ["A", "B", "C"][int(self._activeGrid / 3)]
        out += str((self._activeGrid % 3) + 1)
        if self.won: out = "N/A"
        return out

    @property
    def currentMove(self): return self._currentMove

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
            if self.won: return

            if self._whosMove == "x": self._whosMove = "o"
            else: self._whosMove = "x"

            self.check_next_grid()
        else: 
            print("Invalid position.")

    def check_win(self):
        winConditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 7)]
        wonBoards = [" "] * 9

        for i in range(9):
            for winSet in winConditions:
                j, k, l = winSet
                if (self.board[i][j] != " " and
                    self.board[i][j] == self.board[i][k] == self.board[i][l]):
                    wonBoards[i] = self.board[i][j]

        
        for winSet in winConditions:
            j, k, l = winSet
            if (wonBoards[j] != " " and
                wonBoards[j] == wonBoards[k] == wonBoards[l]):
                self.won = True

    def check_next_grid(self):
        if " " not in self.board[self._activeGrid]:
            newGrid = ""
            while str(newGrid) not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                newGrid = input(f"{self._whosMove}, choose your grid: ")
                if (newGrid not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or 
                            int(newGrid) - 1 == self._activeGrid):
                    print("Invalid grid selection.")
                    newGrid = ""
                else:
                    self._activeGrid = int(newGrid) - 1

