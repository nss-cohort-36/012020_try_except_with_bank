class BankAccount():

    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        """Add money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will increase
        """

        try:
            self.balance += amount
        except TypeError:
            print('Error: The add_money method requires a numeric value')
            # raise
        except NameError:
            print('Error: Are you sure the variable is defined?')

        print("Money may or may not have been added to your account!")

    def withdraw_money(self, amount):
        """Withdraw money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will decrease
        """
        try:
          if self.balance - amount < 0:
            raise ValueError("There is no money in your account")
          elif amount > 2000:
            raise ValueError("Exceeds max withdrawal amount")
          else:
            self.balance -= amount
        except ValueError as error:
            print(error)
