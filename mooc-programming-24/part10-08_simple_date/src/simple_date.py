# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        if not (1 <= day <= 30):
            raise ValueError('Invalid day')
        if not (1 <= month <= 12):
            raise ValueError('Invalid month')
        self._day = day
        self._month = month
        self._year = year
    
    def __repr__(self):
        return f"{self._day}.{self._month}.{self._year}"

    def __eq__(self, another: 'SimpleDate'):
        return self._day == another._day and self._month == another._month and self._year == another._year

    def __ne__(self, another: 'SimpleDate'):
        return not self.__eq__(another)

    def __lt__(self, another: 'SimpleDate'):
        if self._year < another._year:
            return True
        if self._year == another._year:
            if self._month < another._month:
                return True
            if self._month == another._month:
                return self._day < another._day
            return False
        return False
        
    def __gt__(self, another: 'SimpleDate'):
        if self._year > another._year:
            return True
        if self._year == another._year:
            if self._month > another._month:
                return True
            if self._month == another._month:
                return self._day > another._day
            return False
        return False

    def __add__(self, days: int):
        years = (days//30)//12
        months = (days//30)%12
        days -= 30*months + 30*12*years

        days += self._day
        months += self._month
        years += self._year 

        if days > 30:
            days -= 30
            months += 1        
        if months > 12:
            months -= 12
            years += 1

        return SimpleDate(days, months, years)

    def __sub__(self, another: 'SimpleDate'):
        years = self._year - another._year
        months = self._month - another._month
        days = self._day - another._day
        
        return abs(years*12*30 + 30*months + days)

if __name__ == '__main__':
    ## Part 1
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = SimpleDate(28, 12, 1985)

    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    ## Part 2
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)

    # d3 = d1 + 3
    # d4 = d2 + 400

    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)

    ## Part 3
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)