class SavingAccount:
    balance = 20000   # class variable

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            print("Invalid username or password")
            return False

    def withdraw(self, amount):
        if amount > SavingAccount.balance:
            return False
        else:
            SavingAccount.balance -= amount
            return True


# Hardcoded object creation
sobj = SavingAccount("Admin", "123")

# Get login details from user
username = input("Enter user name: ")
password = input("Enter password: ")

# Login validation
if sobj.login(username, password):
    amount = int(input("Enter amount to withdraw: "))
    if sobj.withdraw(amount):
        print("Balance amount after withdrawal is: ", SavingAccount.balance)
    else:
        print("Insufficient funds to withdraw")
