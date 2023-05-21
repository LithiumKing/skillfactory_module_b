# Создание игрового поля
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отрисовки игрового поля
def draw_board():
    print('    1   2   3')
    print('  +---+---+---+')
    for i, row in enumerate(board):
        print(f"{i+1} | {' | '.join(row)} |")
        print('  +---+---+---+')

# Функция для проверки победы
def check_win(player):
    # Проверка по горизонталям и вертикалям
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    # Проверка по диагоналям
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Игровой цикл
current_player = 'X'
game_over = False

while not game_over:
    draw_board()
    print(f"Ходит игрок играющий за {current_player}")
    row = int(input("Введите номер строки (от 1 до 3): ")) - 1
    col = int(input("Введите номер столбца (от 1 до 3): ")) - 1

    if row in range(3) and col in range(3) and board[row][col] == ' ':
        board[row][col] = current_player
        if check_win(current_player):
            draw_board()
            print(f"Игрок {current_player} победил!")
            game_over = True
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            draw_board()
            print("Ничья!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Некорректный ход. Попробуйте еще раз.")