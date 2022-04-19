class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    #Create a file with the User class, including the __init__ and make_deposit methods
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print("User:"+ str(self.name) +", Balance:" + str(self.account_balance))
        return self
        #BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, user1, amount):
        self.account_balance -=  amount
        user1.account_balance += amount
        self.display_user_balance()
        user1.display_user_balance()
        return self


#Create 3 instances of the User class
sana = User("Sana","sansoon@gmail.com")
john = User("John","john@gmail.com")
sam = User("Sam", "sam#gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
sana.make_deposit(50).make_deposit(100).make_deposit(200).make_withdrawal(40)

result1 = sana.display_user_balance()
print(result1)

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
sam.make_deposit(400).make_withdrawal(20).make_withdrawal(30).make_withdrawal(100)
result2 = sam.display_user_balance()
print(result2)

