class User:

    def __init__(self,name, email_address) -> None:
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print('User name: ', self.name)
        print('Account Balance: ', self.account_balance)

    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
brad = User('Brad Pitt', 'pittman@duffman.com')

guido.make_deposit(500)
guido.make_deposit(250)
guido.make_deposit(100)

guido.display_user_balance()

brad.make_deposit(800)
brad.make_deposit(850)

brad.display_user_balance()