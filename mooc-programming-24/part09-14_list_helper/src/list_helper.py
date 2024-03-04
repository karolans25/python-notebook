# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        if len(my_list) == 0:
            raise ValueError('The list can\'t be empty')
        set_of_list = set(my_list)
        common = my_list[0]
        for i in set_of_list:
            if my_list.count(i) > my_list.count(common):
                common = i
        return common

    @classmethod
    def doubles(cls, my_list: list):
        if len(my_list) == 0:
            raise ValueError('The list can\'t be empty')
        set_of_list = set(my_list)
        twice = my_list[0]
        for i in set_of_list:
            if my_list.count(i) >= 2:
                twice = i
                break
        return twice


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))