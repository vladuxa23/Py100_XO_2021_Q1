consol = [[i + j * 3 for i in range(1, 4)] for j in
          range(0, 3)]  # Игровое поле [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a, b = [], []  # 'X', '0'


def pole(consol):
    """

    :param consol:
    :return:
    """

    for i in range(3):
        print(*consol[i])


def replace(list_: list, k: str, number: int):
    """
    Функция замены символа на игровом поле

    :param list_: список ходов
    :param k:
    :param number:
    :return:
    """

    for i in range(len(list_)):
        for j in range(len(list_[i])):
            if list_[i][j] == number:
                list_[i][j] = k


def player_step(consol, sym: str) -> list:
    """
    Функция хода

    :param consol:
    :param sym:
    :return:
    """
    try:
        poz = int(input('Игрок ' + sym + ' введите цифру хода - '))

        while poz not in range(1, 10) or \
                poz in a or poz in b:
            poz = int(input('Игрок ' + sym + ' ДРУГУЮ цифру хода - '))

    except ValueError:
        poz = int(input('Игрок ' + sym + ' введите ЦИФРУ хода - '))

    replace(consol, sym, poz)
    a.append(poz) if sym == 'X' else b.append(poz)
    return consol


def proverka(v: str) -> bool:  # Функция проверки выйгрыша у Х

    spisok = player_step(consol, v)
    # по диагонали
    if spisok[0][0] == v and spisok[1][1] == v and spisok[2][2] == v:
        return True
    # по диагонали
    elif spisok[2][0] == v and spisok[1][1] == v and spisok[0][2] == v:
        return True

    for i in range(3):
        # по строчке
        if spisok[i][0] == v and spisok[i][1] == v and spisok[i][2] == v:
            return True
        # по столбцу
        elif spisok[0][i] == v and spisok[1][i] == v and spisok[2][i] == v:
            return True
    else:
        return False


print('Добро пожаловать в игру Х и 0 ')
pole(consol)

while True:
    if not proverka('X'):
        if len(a) == 5:
            print('Никто не выйграл, никто не проиграл')
            break
        pole(consol)
        if not proverka('0'):
            pole(consol)
        else:
            pole(consol)
            print('Победа за 0')
            break
    else:
        print('Победа за X')
        break
