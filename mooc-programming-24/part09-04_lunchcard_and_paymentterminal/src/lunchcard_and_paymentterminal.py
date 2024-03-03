# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        cost = 2.5
        if payment >= cost:
            self.funds += cost
            self.lunches += 1
            return payment - cost
        return payment

    def eat_special(self, payment: float):
        cost = 4.3
        if payment >= cost:
            self.funds += cost
            self.specials += 1
            return payment - cost
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        cost = 2.5
        if card.balance >= cost:
            card.balance -= cost
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        cost = 4.3
        if card.balance >= cost:
            card.balance -= cost
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount

if __name__ == "__main__":
    ## Part 1
    # card = LunchCard(10)
    # print("Balance", card.balance)
    # result = card.subtract_from_balance(8)
    # print("Payment successful:", result)
    # print("Balance", card.balance)
    # result = card.subtract_from_balance(4)
    # print("Payment successful:", result)
    # print("Balance", card.balance)

    ## Part 2
    # exactum = PaymentTerminal()

    # change = exactum.eat_lunch(10)
    # print("The change returned was", change)

    # change = exactum.eat_lunch(5)
    # print("The change returned was", change)

    # change = exactum.eat_special(4.3)
    # print("The change returned was", change)

    # print("Funds available at the terminal:", exactum.funds)
    # print("Regular lunches sold:", exactum.lunches)
    # print("Special lunches sold:", exactum.specials)

    ## Part 3
    # exactum = PaymentTerminal()

    # change = exactum.eat_lunch(10)
    # print("The change returned was", change)

    # card = LunchCard(7)

    # result = exactum.eat_special_lunchcard(card)
    # print("Payment successful:", result)
    # result = exactum.eat_special_lunchcard(card)
    # print("Payment successful:", result)
    # result = exactum.eat_lunch_lunchcard(card)
    # print("Payment successful:", result)

    # print("Funds available at the terminal:", exactum.funds)
    # print("Regular lunches sold:", exactum.lunches)
    # print("Special lunches sold:", exactum.specials)

    ## Part 4
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)