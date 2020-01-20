from bank_account import BankAccount

my_account = BankAccount()
my_account.add_money('Gazillion dollars')
my_account.add_money(1000000)
my_account.withdraw_money(2001)
print(f'My remaining balance is {my_account.balance}')
