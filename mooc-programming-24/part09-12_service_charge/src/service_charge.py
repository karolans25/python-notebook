# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        if owner == '':
            raise ValueError('Name of the owner can\'t be an empty string')
        if account_number == '':
            raise ValueError('The account_number can\'t be an empty string')
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        if self.__check_amount(amount):
            self.__balance = amount

    def __check_amount(self, amount: float):
        if amount < 0:
            raise ValueError('The amount can\'t be below zero')
        return True

    def __service_charge(self):
        self.balance *= 0.99

    def deposit(self, amount: float):
        if self.__check_amount(amount):
            self.__balance += amount
            self.__service_charge()
        
    def withdraw(self, amount: float):
        if self.__check_amount(amount):
            if self.__balance < amount:
                raise ValueError('There\'s not enough money in the account')
            self.__balance -= amount
            self.__service_charge()

if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)