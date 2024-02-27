# Write your solution here
def print_sudoku(sudoku_list: list):
    for i in range(len(sudoku_list)):
        if i % 3 == 0 and i != 0:
            print()
        for j in range(len(sudoku_list)):
            num = sudoku_list[i][j]
            if j % 3 == 0 and j != 0:
               print(' ', end = '')
            if num == 0:
                print('_', end = '')
            else:
                print(num, end = '')
            print(' ', end = '')
        print()

def copy_and_add(sudoku_list: list, row_no: int, column_no: int, number: int):
    result = []
    for i in range(len(sudoku_list)):
        temp = []
        for j in range(len(sudoku_list)):
            num = sudoku_list[i][j]
            if i == row_no and j == column_no:
                temp.append(number)
            else:
                temp.append(num)
        result.append(temp)
    return result

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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)