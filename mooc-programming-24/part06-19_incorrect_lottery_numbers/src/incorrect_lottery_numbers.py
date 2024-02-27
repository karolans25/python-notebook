# Write your solution here
def filter_incorrect():
    data = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            data.append(line.split(';'))
    
    with open("correct_numbers.csv", "w") as file:
        for i in data:
            week = i[0].split(" ")[1].isnumeric()
            nums = i[1].replace("\n", "").split(',')
            print(i)
            print(nums)
            if not week:
                continue
            if len(nums) != 7:
                continue
            valid = True
            repeated = []
            for j in nums:
                try:
                    if j.isnumeric():
                        if 1 <= int(j) <= 39 and int(j) not in repeated:
                            repeated.append(int(j))
                        else:
                            valid = False
                            break
                    else:
                        valid = False
                        break
                except:
                    break
            if valid:
                file.write(f"{i[0]};{i[1]}")


if __name__ == "__main__":
    filter_incorrect()