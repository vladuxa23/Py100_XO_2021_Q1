
import game_logic

game = game_logic.Game()
currentTurn = 1 # 1 - X, 2 - O Кто первый будет ходить
computerGame = 0
while True:
    print("Нажмите 1 для игры с пользователем или 2 для игры с компьютером")
    choice = input()
    try:
        choice = int(choice)
        if choice < 1 or choice > 2:
            print("Неправильный выбор")
            continue
        break
    except ValueError:
        print("Неправильный выбор")
        continue

while(game.checkWin()!=1 and game.checkWin()!=2 and game.checkWin()!=3): 
    print("Текущее поле:")
    print(game)
    if currentTurn==1:
        print("Ходит игрок X. Введите номер ячейки для хода от 1 до 9: ")
    else:
        print("Ходит игрок О. Введите номер ячейки для хода от 1 до 9: ")
    pos = input()
    try:
        pos = int(pos)
        if pos<1 or pos>9:
            print("Неправльный ход")
            continue
    except ValueError:
        print("Неправльный ход")
        continue

    if not game.makeTurn(pos-1,currentTurn):
        print("Ход уже занят")
        continue
    if(choice==2):
        game.computerMakeTurn()
    else:
        if currentTurn == 1:
            currentTurn = 2
        else:
            currentTurn = 1
print("Текущее поле:\n")
print(game)
if game.checkWin()==1:
    print("Выиграл игрок: X")
elif game.checkWin()==2:
    print("Выиграл игрок: О")
else:
    print("Отбражение")



