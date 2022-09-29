class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            print(account.balance)
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        return True


anthony = BankAccount(.03, 0)
kaitlin = BankAccount(.10, 0)

anthony.deposit(50).deposit(20).deposit(10).withdraw(40).yield_interest().display_account_info()
kaitlin.deposit(50).deposit(10).withdraw(20).withdraw(20).withdraw(10).withdraw(20).yield_interest().display_account_info()

BankAccount.all_accounts()