# Write your solution here
def longest_series_of_neighbours(list_numbers):
    result = []
    temp = [list_numbers[0]]
    for num in list_numbers:
        if abs(num - temp[len(temp)-1]) == 1:
            temp.append(num)
        if len(temp) > len(result):
            result = temp
    return result

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
