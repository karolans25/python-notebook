# Write your solution here
def transpose(matrix: list):
    copy = []
    for item in matrix:
        temp = []
        for num in item:
            temp.append(num)
        copy.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = copy[i][j]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)