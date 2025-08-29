import random


def is_valid(board, row, col, num):
    """Проверяет, можно ли разместить число в клетке"""
    # Проверка строки
    for x in range(9):
        if board[row][x] == num:
            return False

    # Проверка столбца
    for x in range(9):
        if board[x][col] == num:
            return False

    # Проверка блока 3x3 (Можно разбить на ячейки)
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """Заменяет 0 на числа в соответствии с правилами судоку"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        # Откат
                        board[row][col] = 0

                return False
    return True


def generate_sudoku():
    """Генерирует доску судоку"""
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board


def print_sudoku(board):
    """Красиво выводит судоку"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()



# Пример использования
if __name__ == "__main__":
    solution = generate_sudoku()
    print_sudoku(solution)