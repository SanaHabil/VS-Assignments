class BankAccount:
    bank_name = "First Bank"
    all_accounts = []
    def __init__(self, balance, interest_rate):
        self.balance = 0
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            #print("Accounts:", cls.all_accounts)
            print("Accounts:", account.display_account_info())
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount 
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self    

    def display_account_info(self):
        print("Balance: $"+ str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate 
        return self

# Create 2 accounts:
sana = BankAccount(100, 0.3)
reina = BankAccount(200, 0.3)

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
sana.deposit(100).deposit(200).deposit(100).withdraw(50).yield_interest().display_account_info()

#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
reina.deposit(100).deposit(200).withdraw(100).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()


#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_instances()


