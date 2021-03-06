# class User:
#     population = 0

#     def __init__(self,name, email_address) -> None:
#         self.name = name
#         self.email = email_address
#         self.account = [BankAccount(int_rate=.04)]
#         User.population += 1

#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         return self

#     def make_withdrawl(self, amount):
#         self.account.withdraw(amount)
#         return self

#     def display_user_balance(self):
#         print(f'User name: {self.name}')
#         print(f'Account Balance: {self.account.display_account_info()}')
#         print('-' * 25)

#     def transfer_money(self, other_user, amount):
#         self.make_withdrawl(amount)
#         other_user.make_deposit(amount)


class BankAccount:
    all_accounts = {}
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance=0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts[self.name]
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
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


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth
        self.name = 'Retirement'

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.1
        super().withdraw(amount)


class CheckingAccount(BankAccount):
    def __init__(self, name, int_rate, balance=0):
        super().__init__(int_rate, balance)
        self.int_rate = 0
        self.name = 'Checking'


# guido = User('Guido van Rossum', 'guido@python.com')
# monty = User('Monty Python', 'monty@python.com')
# brad = User('Brad Pitt', 'pittman@duffman.com')

# guido.make_deposit(500).make_deposit(250).make_deposit(100)
# guido.display_user_balance()

# brad.make_deposit(800).make_withdrawl(425).make_deposit(850).make_withdrawl(400)
# brad.display_user_balance()

# brad.transfer_money(guido, 725)
# brad.display_user_balance()
# guido.display_user_balance()

# monty.make_deposit(1000).make_withdrawl(100).make_withdrawl(125).make_withdrawl(50)

# monty.display_user_balance()

new_list = [BankAccount(.03)]
new_list.append(RetirementAccount(.05, is_roth=True))
# print(new_list[0].display_account_info())
# print(new_list[1].display_account_info())

BankAccount.display_all_info()

# class User:
#     population = 0

#     def __init__(self,name, email_address) -> None:
#         self.name = name
#         self.email = email_address
#         self.account = [BankAccount(int_rate=.04)]
#         User.population += 1

#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         return self

#     def make_withdrawl(self, amount):
#         self.account.withdraw(amount)
#         return self

#     def display_user_balance(self):
#         print(f'User name: {self.name}')
#         print(f'Account Balance: {self.account.display_account_info()}')
#         print('-' * 25)

#     def transfer_money(self, other_user, amount):
#         self.make_withdrawl(amount)
#         other_user.make_deposit(amount)


# class BankAccount:
#     all_accounts = []
#     # don't forget to add some default values for these parameters!
#     def __init__(self, int_rate, balance=0): 
#         self.balance = balance
#         self.int_rate = int_rate
#         BankAccount.all_accounts.append(self)
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#         return self

#     def display_account_info(self):
#         print(f'Your account balance is {self.balance}.')
#         return self.balance

#     def yield_interest(self):
#         if self.balance > 0:
#             return self.balance * (1 + self.int_rate)
#         else:
#             return self.balance

#     @classmethod
#     def display_all_info(cls):
#         for i in range(len(cls.all_accounts)):
#             print(cls.all_accounts[i].balance)
#             print('-' * 25)

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         super().__init__(int_rate, balance)
#         self.is_roth = is_roth

#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.1
#         super().withdraw(amount)


# guido = User('Guido van Rossum', 'guido@python.com')
# monty = User('Monty Python', 'monty@python.com')
# brad = User('Brad Pitt', 'pittman@duffman.com')

# guido.make_deposit(500).make_deposit(250).make_deposit(100)
# guido.display_user_balance()

# brad.make_deposit(800).make_withdrawl(425).make_deposit(850).make_withdrawl(400)
# brad.display_user_balance()

# brad.transfer_money(guido, 725)
# brad.display_user_balance()
# guido.display_user_balance()

# monty.make_deposit(1000).make_withdrawl(100).make_withdrawl(125).make_withdrawl(50)

# monty.display_user_balance()