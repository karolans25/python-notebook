# Write your solution here
def length_of_longest(list):
    #long = []
    #for i in list:
    #    long.append(len(i))
    #return max(long)
    longest = 0
    for i in list:
        if len(i) > longest:
            longest = len(i)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
