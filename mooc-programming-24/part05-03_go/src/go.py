# Write your solution here
def who_won(game_board: list):
    counts_1 = 0
    counts_2 = 0
    for i in game_board:
        counts_1 += i.count(1)
        counts_2 += i.count(2)
    if counts_1 > counts_2:
        return 1
    elif counts_1 < counts_2:
        return 2
    else:
        return 0

if __name__ == "__main__":
    m = [[1, 2, 1], [1, 1, 1], [2, 2, 2]]
    print(who_won(m))
