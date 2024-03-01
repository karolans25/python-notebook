# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value >= 1:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial

if __name__ == '__main__':
    ## Part 1
    # counter = DecreasingCounter(10)
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()

    ## Part 2
    # counter = DecreasingCounter(2)
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()

    ## Part 3
    # counter = DecreasingCounter(100)
    # counter.print_value()
    # counter.set_to_zero()
    # counter.print_value()

    ## Part 4
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()