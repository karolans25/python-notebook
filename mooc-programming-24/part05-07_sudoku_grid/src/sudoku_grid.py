# Write your solution here
def row_correct(sudoku: list, row_no: int):
    for n in range(1, 10):
        if sudoku[row_no].count(n) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for line in sudoku:
        num = line[column_no]
        if num in numbers and num > 0:
            return False
        numbers.append(num)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(0, 3):
        for j in range(0, 3):
            num = sudoku[row_no + i][column_no + j]
            if num > 0 and num in numbers:
                return False
            numbers.append(num)
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0, len(sudoku)):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            correct = block_correct(sudoku, i, j)
            if not correct:
                return False

    return True

if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))