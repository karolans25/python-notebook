# write your solution here
def matrix_sum():
    matrix = get_matrix()
    result = 0
    for line in matrix:
        result += sum(line)
    return result

def matrix_max():
    matrix = get_matrix()
    maximum = 0
    for line in matrix:
        max_line = max(line)
        if max_line > maximum:
            maximum = max_line
    return maximum

def row_sums():
    matrix = get_matrix()
    result = []
    for line in matrix:
        result.append(sum(line))
    return result

def get_matrix():
    num_matrix = []
    with open('matrix.txt') as new_file:
        for line in new_file:
            nums = line.replace('\n', '').split(',')
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            num_matrix.append(nums)
    return num_matrix

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())