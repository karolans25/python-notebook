# Write your solution here
def all_the_longest(list):
    result = []
    for i in list:
        if result == [] or len(i) > len(result[0]):
            result = [i]
        elif len(i) == len(result[0]):
            result.append(i)
    return result

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']