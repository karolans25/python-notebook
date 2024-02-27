# Write your solution here
def print_sudoku(sudoku_list: list):
    for i in range(len(sudoku_list)):
        if i % 3 == 0 and i != 0:
            print()
        for j in range(len(sudoku_list[i])):
            num = sudoku_list[i][j]
            if j % 3 == 0 and j != 0:
               print(' ', end = '')
            if num == 0:
                print('_', end = '')
            else:
                print(num, end = '')
            print(' ', end = '')
        print()

def add_number(sudoku_list: list, line: int, column: int, element: int):
    sudoku_list[line][column] = element

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)