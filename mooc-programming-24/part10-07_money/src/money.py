# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        if euros < 0:
            raise ValueError('Euros can\'t be below zero')
        if cents < 0:
            raise ValueError('Cents can\'t be below zero')
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    
    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __ne__(self, another):
        return not self.__eq__(another)

    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        if self._euros == another._euros:
            return self._cents < another._cents
        return False

    def __gt__(self, another):
        if self._euros > another._euros:
            return True
        if self._euros == another._euros:
            return self._cents > another._cents
        return False

    def __add__(self, another):
        if self._cents + another._cents >= 100:
            return Money(self._euros + another._euros + 1, self._cents + another._cents - 100 )
        return Money(self._euros + another._euros, self._cents + another._cents)

    def __sub__(self, another):
        if self._euros - another._euros < 0:
            raise ValueError('a negative result is not allowed')
        if self._cents - another._cents < 0:
            return Money(self._euros - another._euros - 1, 100 - abs(self._cents - another._cents) )
        return Money(self._euros - another._euros, self._cents - another._cents)

if __name__ == '__main__':
    ## Part 1
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)  # two euros and five cents

    # print(e1)
    # print(e2)

    ## Part 2
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)

    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)

    ## Part 3
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    ## Part 4
    # e1 = Money(4, 5)
    # e2 = Money(2, 95)

    # e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)

    # e5 = e2-e1

    ## Part 5
    e1 = Money(4, 5)
    print(e1)
    e1.euros = 1000
    print(e1)