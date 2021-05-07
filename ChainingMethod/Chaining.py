class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_self, amount):
        self.account_balance -= amount
        other_self.account_balance += amount
        return self
        
sean = User("Sean", "seanruddell@yahoo.com")
guido = User("Guido", "guido@yahoo.com")
monty = User("Monty", "montymcgoo@yahoo.com")

sean.make_deposit(200).make_deposit(300).make_deposit(200).make_withdrawl(150).display_user_balance()
guido.make_deposit(100).make_deposit(500).make_withdrawl(50).make_withdrawl(100).display_user_balance()
monty.make_deposit(1000).make_withdrawl(150).make_withdrawl(200).make_withdrawl(100).display_user_balance()
sean.transfer_money(monty, 1).display_user_balance()
monty.display_user_balance()