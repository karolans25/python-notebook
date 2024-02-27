# Write your solution here
def everything_reversed(string_list):
    result = []
    for i in string_list:
        result.append(i[::-1])
    return result[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)