# write your solution here
def read_fruits():
    result = {}
    with open("fruits.csv") as new_file:
        for num in new_file:
            fruit, price = num.replace('\n', '').split(';')
            result[fruit] = float(price)
    return result

if __name__ == "__main__":
    print(read_fruits())