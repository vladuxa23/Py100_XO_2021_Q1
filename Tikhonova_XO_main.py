from itertools import combinations
import random

x_choice = []
o_choice = []
field = [str(num) for num in list(range(1, 10))]
possible_moves = [str(num) for num in list(range(1, 10))]
winning_combinations = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"),
                        ("1", "4", "7"), ("2", "5", "8"), ("3", "6", "9"),
                        ("1", "5", "9"), ("3", "5", "7"))


def the_play_0():
    number = str(random.choice(possible_moves))
    number_index = possible_moves.index(number)
    number_index_field = field.index(number)
    field[number_index_field] = "0"
    o_choice.append(possible_moves.pop(number_index))
    print_field()
    return possible_moves


def the_play_x(name_):
    for _ in possible_moves:
        number = input(f"{name_}")
        if number in possible_moves:
            number_index = possible_moves.index(number)
            number_index_field = field.index(number)
            field[number_index_field] = "X"
            x_choice.append(possible_moves.pop(number_index))
            print_field()
            break
        else:
            print("Попробуйте еще раз. Ячейка занята или отсутствует")

    return possible_moves


def check_win():
    for combination in combinations(x_choice, 3):
        if tuple(sorted(combination)) in winning_combinations:
            print("Победа X. Игрок X, Вы великолепны! КОНЕЦ ИГРЫ")
            return True
    for combination in combinations(o_choice, 3):
        if tuple(sorted(combination)) in winning_combinations:
            print("Победа О. КОНЕЦ ИГРЫ")
            return True


def print_field():
    sep_ = "_______________"
    return print(sep_, field[0:3], sep_, field[3:6], sep_, field[6:9], sep_,
                 sep="\n")


def start_game():
    print("Введите имя: ")
    name_ = input()
    print(
        f"{name_}, Добро пожаловать в игру!\nВы играете за X\nВведите номер ячейки: ")
    print_field()
    return name_


def the_contest():
    name = start_game()
    while len(possible_moves) >= 2:
        the_play_x(name)
        if check_win():
            break
        the_play_0()
        if check_win():
            break
    else:
        print("Ходы закончились. НИЧЬЯ")


the_contest()
