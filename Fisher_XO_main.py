list_ = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
hod_X = []
hod_O = []
s_win_win = []
win_position = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                [3, 6, 9], [1, 5, 9], [3, 5, 7]]
n = 1


def check_win():
    for i in win_position:
        if i[0] in hod_X and i[1] in hod_X and i[2] in hod_X or i[
            0] in hod_O and i[1] in hod_O and i[2] in hod_O:
            s_win_win.append(True)
    return True if True in s_win_win else False


def no_winner():
    return True if len(hod_X) + len(hod_O) >= 9 else False


def display():
    print("----------------------")
    print(list_[1], list_[2], list_[3])
    print(list_[4], list_[5], list_[6])
    print(list_[7], list_[8], list_[9])
    print("----------------------")


def turn(t):
    if t == 1:
        t = 2
    else:
        t = 1
    return t


def check_trauble(square):
    if square > 9 or square < 1:
        print("Неверное значение! Выберите клетку от 1 до 9")
        return False
    elif list_[square] != ".":
        print("Сюда уже ходили. Выберите другую клетку")
        return False
    else:
        return True


def hod(square):
    if n % 2 == 0:
        list_[square] = "X"
        hod_X.append(square)
        hod_X.sort()
    else:
        list_[square] = "0"
        hod_O.append(square)
        hod_O.sort()
    display()


while True:
    hod_igroka = int(input("Ход игрока " + str(n) + ": "))
    if check_trauble(hod_igroka):
        hod(hod_igroka)
        if check_win():
            print("Игра окончена! Выиграл игрок " + str(n))
            print(" Ходы игрока 1", hod_O)
            print(" Ходы игрока 2", hod_X)
            break
        elif no_winner():
            print("Ничья!")
            break
        n = turn(n)
