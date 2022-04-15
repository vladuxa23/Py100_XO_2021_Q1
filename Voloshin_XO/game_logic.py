import copy


class Game():
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]]  # Игровое поле
        self.turn_count = 0  # Счётчик

    def getBoard(self):
        return self.board

    def __str__(self):  # Что будет отображаться
        tempBoard = copy.deepcopy(self.board)
        for i in range(9):
            if tempBoard[i // 3][i % 3] == 0:
                tempBoard[i // 3][i % 3] = " "
            if tempBoard[i // 3][i % 3] == 1:
                tempBoard[i // 3][i % 3] = 'X'
            if tempBoard[i // 3][i % 3] == 2:
                tempBoard[i // 3][i % 3] = 'O'
        return str(tempBoard[0]) + "\n" + str(tempBoard[1]) + "\n" + str(
            tempBoard[2])

    def makeTurn(self, pos, turn):
        if self.board[pos // 3][pos % 3] != 0:
            return False
        self.board[pos // 3][pos % 3] = turn
        self.turn_count += 1
        return True

    def computerMakeTurn(self):
        if self.turn_count == 1:
            if self.board[1][1] != 0:
                self.board[0][0] = 2
                self.turn_count += 1
            else:
                self.board[1][1] = 2
                self.turn_count += 1
        else:
            for i in range(9):  # Проверка выигрыша
                if self.makeTurn(i, 2):
                    if self.checkWin() == 2:
                        self.turn_count += 1
                        return
                    self.board[i // 3][i % 3] = 0
            for i in range(9):  # Проверка выигрышного хода другого игрока
                if self.makeTurn(i, 1):
                    if self.checkWin() == 1:
                        self.board[i // 3][i % 3] = 2
                        self.turn_count += 1
                        return
                    self.board[i // 3][i % 3] = 0
            for i in range(9):
                if self.makeTurn(i, 2):
                    return

    def checkWin(self):
        winner = 0
        sign = self.board[0][0]
        if sign != 0:
            if self.board[0][1] == sign and self.board[0][2] == sign:
                return sign
            elif self.board[1][1] == sign and self.board[2][2] == sign:
                return sign
            elif self.board[1][0] == sign and self.board[2][0] == sign:
                return sign
        sign = self.board[0][1]
        if sign != 0:
            if self.board[1][1] == sign and self.board[2][1] == sign:
                return sign
        sign = self.board[0][2]
        if sign != 0:
            if self.board[1][2] == sign and self.board[2][2] == sign:
                return sign
            elif self.board[1][1] == sign and self.board[2][0] == sign:
                return sign
        sign = self.board[1][0]
        if sign != 0:
            if self.board[1][1] == sign and self.board[1][2] == sign:
                return sign
        sign = self.board[2][0]
        if sign != 0:
            if self.board[2][1] == sign and self.board[2][2] == sign:
                return sign
        for i in self.board:
            for j in i:
                if j == 0:
                    return 0  # Ни кто не выиграл
        return 3  # Отображение
