import random

board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
list_player = []
list_pc = []


def print_board():
    print('---------')
    print(board[1], '|', board[2], '|', board[3])
    print('---------')
    print(board[4], '|', board[5], '|', board[6])
    print('---------')
    print(board[7], '|', board[8], '|', board[9])
    print('---------')


def win():
    for elem in win_list:
        result_player = [x for x in list_player if x in elem]
        result_pc = [y for y in list_pc if y in elem]
        if sorted(result_player) == elem:
            print('Победил игрок')
            return True
        elif sorted(result_pc) == elem:
            print('Победил ПК')
            return True


def draw():
    if len(list_player) + len(list_pc) == 9:
        print('Ничья')
        return True


while True:
    print_board()

    player = 'O'
    hod_player = int(input("Игрок укажите клетку: "))
    while hod_player not in board:
        hod_player = int(input("Игрок укажите правильную клетку клетку: "))
    board[hod_player] = player
    list_player.append(hod_player)

    if draw():
        print_board()
        break

    pc = 'X'
    hod_pc = random.randint(1, 9)
    while hod_pc not in board:
        hod_pc = random.randint(1, 9)
    list_pc.append(hod_pc)
    board[hod_pc] = pc

    if win():
        print_board()
        break
