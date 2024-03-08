# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_number: int, winner_numbers: list):
        self.__week_number = week_number
        self.__winner_numbers = winner_numbers

    def number_of_hits(self, numbers: list):
        return len([i for i in numbers if i in self.__winner_numbers])

    def hits_in_place(self, numbers: list):
        return [i if i in self.__winner_numbers else -1 for i in numbers]

if __name__ == '__main__':
    ## Part 1
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))

    ## Part 2
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))