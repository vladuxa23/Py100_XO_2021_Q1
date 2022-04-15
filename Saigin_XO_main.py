xy_range = 5  # размер поля по x, y - ибо квадрат
# допустимые значения - от 3 до 5, ибо меньше нет, а больше 5 (до 9) потребует другой логики проверки условия выигрыша,
# поскольку, вероятно, могут быть пропуски в winner() - нужно проверять и корректировать
# y_range = 5 # размер поля по y - не нужен
xo_pool: list = []  #: list = [] # глобальный список - поле игры
str_out = ""  #: string # строка для вывода поля игры
player1 = True  # очередность хода
player2 = False
coord = []  # координаты хода
filler = "-"  # заполнитель
max_in_a_row = 5  # максимальное значение в ряд
player1_sym = ["X"]
player2_sym = ["O"]
number_of_moves = 0


def display_xo_pool():  # вывод игрового поля
    str_out = "  "
    print("*" * 20)

    for i in range(1, xy_range + 1):
        str_out += str(i) + " "  # верхняя строка координат
    str_out += "\n"  # новая срока после верхней

    for i in range(1, xy_range ** 2 + 1):  # цикл по всему полю игры

        if (i - 1) % xy_range == 0:
            str_out += str((i - 1) // xy_range + 1) + " "
        str_out += xo_pool[(i - 1) // xy_range][(i - 1) % xy_range] + " "

        if i % xy_range == 0:
            str_out += "\n"
        # print(i, (i - 1) // xy_range, (i - 1) % xy_range, xo_pool[(i - 1) // xy_range][(i - 1) % xy_range], type(xo_pool[(i - 1) // xy_range][(i - 1) % xy_range]))

    print(str_out)
    return None


def winner():  # проверка условия выигрыша
    str_x = ""  # инициализируем строки, по которым будем проверять выигрыш
    str_y = ""  # строк - 4 штуки, 2 для x и y и две для диагоналей.
    str_d1 = ""
    str_d2 = ""
    for j in range(0, xy_range):  # перебираем координаты матрицы
        for i in range(0, xy_range):
            str_x += xo_pool[j][i]  # строка по горизонтали
            str_y += xo_pool[i][j]  # строка по вертикали
        str_x = str_x.replace(filler, "")  # избавляемся от заполнителя в полученных строках
        str_y = str_y.replace(filler, "")  # избавляемся от заполнителя в полученных строках
        if len(str_x) == max_in_a_row and (list(set(str_x)) == player1_sym
                                           or list(set(str_x)) == player2_sym):
            return True
        if len(str_y) == max_in_a_row and (list(set(str_y)) == player1_sym
                                           or list(set(str_y)) == player2_sym):
            return True

        str_x = ""
        str_y = ""
        str_d1 += xo_pool[j][j]  # диагональ слева сверху - направо вниз
        str_d2 += xo_pool[xy_range - j - 1][j]  # другая диагональ :)

    str_d1 = str_d1.replace(filler, "")  # избавляемся от заполнителя в полученных строках
    str_d2 = str_d2.replace(filler, "")  # избавляемся от заполнителя в полученных строках

    if len(str_d1) == max_in_a_row and (list(set(str_d1)) == player1_sym
                                        or list(set(str_d1)) == player2_sym):
        return True
    if len(str_d2) == max_in_a_row and (list(set(str_d2)) == player1_sym
                                        or list(set(str_d2)) == player2_sym):
        return True

    return False


def input_xy():
    ...  # ввод координат хода
    # xy_move = []
    if player1:
        print("Игрок X, Ваш ход.")
    else:
        print("Игрок O, Ваш ход:")
    # x = int(input("X: "))
    # y = int(input("Y: "))
    while True:
        x = get_coord("X (1-" + str(xy_range) + "): ")
        y = get_coord("Y (1-" + str(xy_range) + "): ")
        target_move = xo_pool[y - 1][x - 1]
        if target_move != filler:  # проверка, не занята ли ячейка
            print("Сюда ходить нельзя - занято!")
            display_xo_pool()
        else:
            # xy_move = [y-1, x-1]
            return [y - 1, x - 1]  # xy_move


def get_coord(str_):  # ввод координаты с приглашением
    while True:
        get_c = input(str_)  # Ввод числа
        if get_c.isdigit() and int(get_c) <= xy_range:
            return int(get_c)  # проверка условий, возврат результата, если ок


def swap_move(player):  # меняет булево значение переменной на противоположное
    return not player


def finnish():
    if not player1:
        return "Игрок 1 победил!"
    else:
        return "Игрок 2 победил!"


# Начало основного скрипта
xo_pool = [[filler for x in range(1, (xy_range + 1))] for y in
           range(1, (xy_range + 1))]  # инициализация
if xy_range < 5:  # корректируем значение в зависимости от доски
    max_in_a_row = xy_range
else:
    max_in_a_row = 5
print("Инициализация.\n", xo_pool)
print("2 игрока, размер поля: ", xy_range, "x", xy_range,
      "\nИгрок 1 = X, Игрок 2 = O\nПоехали!\n")

while not winner():  # цикл, пока нет победителя
    display_xo_pool()  # отображаем игровое поле
    coord = input_xy()  # вводим координаты
    if player1:
        xo_pool[coord[0]][coord[
            1]] = "X"  # str(player1_sym) # ставим крестик, или чем там играет P1? :)
    else:
        xo_pool[coord[0]][coord[
            1]] = "O"  # str(player2_sym) # или нолик - в зависимости от того, чей ход
    player1 = swap_move(player1)  # меняем активоного игрока
    # player2 = swap_move(player2)
    number_of_moves += 1
    if number_of_moves == xy_range ** 2:
        print("Больше некуда ходить. Ничья. Пока!")
        display_xo_pool()
        # number_of_moves += 1
        break

if number_of_moves < xy_range ** 2:
    print(finnish())
    display_xo_pool()
    print("*" * 20)
