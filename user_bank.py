class BankAccount:
    accounts = []
    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name
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
            print(f'{self.account_name} - Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
            return False
        return self
    def display_account_info(self):
        print(f"{self.account_name}: {self.balance}")
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


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = {}
    def open_account(self,account_name,int_rate,amount):
        self.accounts[account_name] = BankAccount(account_name.capitalize(),int_rate,amount)
        return self
    def display_info(self):
        dict = vars(self)
        for key in dict:
            print(f"{key}: {dict[key]}")
        return self
    def make_deposit(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
    def make_withdrawal(self, account_name,amount):
        self.accounts[account_name].withdraw(amount)
        return self
    def display_user_accounts(self):
        for account in self.accounts:
            self.accounts[account].display_account_info()
        return self
    def transfer_funds(self,amount,other_user):
        success = self.accounts['checking'].withdraw(amount)
        if success == False:
            print('Transfer failed, insufficient funds; charged $5.')
        else:
            other_user.accounts['checking'].deposit(amount)
        return self


kaitlin = User('kaitlin', 'greenwell')
kaitlin.open_account('checking',0.01,0).display_user_accounts()

anthony = User('anthony', 'greenwell')
anthony.open_account('checking',0.01,0).open_account('savings',0.10,0).make_deposit('checking',30).transfer_funds(10,kaitlin).display_user_accounts()

kaitlin.display_user_accounts()
