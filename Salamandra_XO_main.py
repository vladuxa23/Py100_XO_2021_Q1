def display_board():
    print(f"""  Ход № {len(x_moves + o_moves) + 1}!
    {board[1]} | {board[2]} | {board[3]}
    ---------
    {board[4]} | {board[5]} | {board[6]}
    ---------
    {board[7]} | {board[8]} | {board[9]}""")


def make_turn():
    global is_it_x_turn
    player_mark = "X" if is_it_x_turn else "O"

    space = int(input(f"Игрок {player_mark} укажите клетку: "))

    board[space] = player_mark
    legal_moves.remove(space)

    if player_mark == "X":
        x_moves.append(space)
    else:
        o_moves.append(space)
    is_it_x_turn = not is_it_x_turn


def is_there_a_winner():
    for win in winning_combinations:
        if win.issubset(x_moves):
            print("Игрок X победил!")
            return True
        elif win.issubset(o_moves):
            print("Игрок O победил!")
            return True

    if not legal_moves:
        print("Ничья")
        return True

    else:
        return False


if __name__ == '__main__':

    board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    legal_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_moves, o_moves = [], []
    winning_combinations = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
                            {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    is_it_x_turn = True

    while not is_there_a_winner():
        display_board()
        make_turn()
