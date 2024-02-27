# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        biggest = 0
        for num in new_file:
            num = int(num)
            if num > biggest:
                biggest = num
        return biggest

if __name__ == "__main__":
    print(largest())