class BankAccount:
    bank_name = "First Bank"
    all_accounts = []
    def __init__(self, balance, interest_rate):
        self.balance = 0
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = { 
                        "checking": BankAccount(interest_rate=0.02, balance=0),
                        "savings": BankAccount(interest_rate=0.03, balance=0)
                        }	# added this line

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account["checking"].balance += amount	# the specific user's account increases by the amount of the value received

    #Create a file with the User class, including the __init__ and make_deposit methods
    def make_withdrawal(self, amount):
        self.account["checking"].balance -= amount

    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print("User:",self.name,", Checking Balance:",self.account["checking"].balance)
        print("User:",self.name,", Savings Balance:",self.account["savings"].balance)
        #BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(sana, sam, amount):
        sana.account.balance = sana.account.balance - amount
        sam.account.balance  += amount
        print(sana.account.balance)
        print(sam.account.balance)

    
    #Second approch to solve: Add a transfer_money method used functions from above
    def move_money(self, destination, money):
        self.make_withdrawal(money)
        destination.make_deposit(money)
        print(self.account_balance)
        print(destination.account_balance)
        return self  



#Create 3 instances of the User class
sana = User("Sana","sansoon@gmail.com")
john = User("John","john@gmail.com")
sam = User("Sam", "sam#gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
sana.make_deposit(50)
sana.make_deposit(100)
sana.make_deposit(200)
sana.make_withdrawal(40)
result1 = sana.display_user_balance()
print(result1)

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
sam.make_deposit(400)
sam.make_withdrawal(20)
sam.make_withdrawal(30)
sam.make_withdrawal(100)
result2 = sam.display_user_balance()
print(result2)



print(sana.display_user_balance())



