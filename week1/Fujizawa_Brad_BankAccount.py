class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        self.balance = balance
        self.int_rate = (int_rate * .01)
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Your account balance is {self.balance}.')
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            return self.balance * (1 + self.int_rate)
        else:
            return self.balance

    @classmethod
    def display_all_info(cls):
        for i in range(len(cls.all_accounts)):
            print(cls.all_accounts[i].balance)
            print('-' * 25)


new_account = BankAccount(3)
new_account2 = BankAccount(3, 500)

new_account.deposit(100).deposit(100).deposit(250).yield_interest()
print(new_account2.deposit(1000).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest())

BankAccount.display_all_info()
