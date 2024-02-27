# Write your solution here
def shortest(list):
    shortest = list[0]
    for i in list:
        if len(i) < len(shortest):
            shortest = i
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)