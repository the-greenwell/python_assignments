class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

anthony = BankAccount(.03, 0)
kaitlin = BankAccount(.10, 500)

anthony.deposit(50).deposit(20).deposit(10).withdraw(40).yield_interest().display_account_info()
kaitlin.deposit(50).deposit(10).withdraw(20).withdraw(20).withdraw(10).withdraw(20).yield_interest().display_account_info()
