# Write your solution here:
class Item:
    def __init__(self, name: str = None, kg: int = None):
        self.__name = '' if name == None else name
        self.__weight = 0 if kg == None else kg
        
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_kg: int = None):
        self.__max_weight = 0 if max_kg == None else max_kg
        self.__items = []

    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.__calculate_total_weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.__calculate_total_weight()} kg)"

    def add_item(self, item: Item):
        if self.__calculate_total_weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for i in self.__items:
            print(i)

    def weight(self):
        return self.__calculate_total_weight()

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        heaviest = self.__items[0]
        for i in self.__items:
            if i.weight() > heaviest.weight():
                heaviest = i
        return heaviest

    def __calculate_total_weight(self):
        if self.__items == None:
            return 0
        total = sum( i.weight() for i in self.__items )
        return total
    

class CargoHold:
    def __init__(self, max_kg: int = None):
        self.__max_weight = 0 if max_kg == None else max_kg
        self.__suitcases = []

    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.__calculate_total_weight()} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.__calculate_total_weight()} kg"

    def add_suitcase(self, suitcase: Suitcase):
        if self.__calculate_total_weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for i in self.__suitcases:
            i.print_items()

    def __calculate_total_weight(self):
        if self.__suitcases == None:
            return 0
        total = sum( i.weight() for i in self.__suitcases )
        return total

if __name__ == '__main__':
    # ## Part 1
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)

    # print("Name of the book:", book.name())
    # print("Weight of the book:", book.weight())

    # print("Book:", book)
    # print("Phone:", phone)

    # # book = Item("ABC Book", 2)
    # # book.weight = 10
    # # print("Book:", book)

    ## Part 2
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(5)
    # print(suitcase)

    # suitcase.add_item(book)
    # print(suitcase)

    # suitcase.add_item(phone)
    # print(suitcase)

    # suitcase.add_item(brick)
    # print(suitcase)

    ## Part 4
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # print("The suitcase contains the following items:")
    # suitcase.print_items()
    # combined_weight = suitcase.weight()
    # print(f"Combined weight: {combined_weight} kg")

    ## Part 5
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # heaviest = suitcase.heaviest_item()
    # print(f"The heaviest item: {heaviest}")

    ## Part 6
    # cargo_hold = CargoHold(1000)
    # print(cargo_hold)

    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # adas_suitcase = Suitcase(10)
    # adas_suitcase.add_item(book)
    # adas_suitcase.add_item(phone)

    # peters_suitcase = Suitcase(10)
    # peters_suitcase.add_item(brick)

    # cargo_hold.add_suitcase(adas_suitcase)
    # print(cargo_hold)

    # cargo_hold.add_suitcase(peters_suitcase)
    # print(cargo_hold)

    ## Part 7
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()