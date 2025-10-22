#WAP in python to debit a banking system. Ask user whether they want to credit or debit amount, or just want to check balance. After that ask them whether they want to check the current balance or not.

class account:
    def __init__(self, acc, bal):
        self.account_no = acc
        self.balance = bal

    def credit(self, amount):
        self.balance += amount
        return (f"You have credited Rs {amount}-/")

    def debit(self, amount):
        self.balance -= amount
        return (f"You have debited Rs {amount}-/")

    def get_balance(self):
        return self.balance
        # return (f"Your current balance is Rs {self.get_balance()}-/")

def ATM():
    user_input = input("Choose any one option:\n1. Credit\n2. Debit\n3. Check balance\n=> ")
    #Credit
    if user_input == "1" or user_input == "Credit" or user_input == "credit":
        amount = int(input("Enter your amount: "))
        print(s1.credit(amount))
        check_balance = input("Do you want to check your current balance? y/n: ")
        if check_balance == "y":
            print(f"Your current balance is Rs {s1.get_balance()}-/")
            exit_ATM()
        else:
            exit_ATM()

    #Debit
    elif user_input == "2" or user_input == "Debit" or user_input == "debit":
        amount = int(input("Enter your amount: "))
        #Print invalid amount if amount > balance
        if amount <= balance:
            print(s1.debit(amount))
        else:
            print("Please enter a valid amount.")
        check_balance = input("Do you want to check your current balance? y/n: ")
        if check_balance == "y":
            print(f"Your current balance is Rs {s1.get_balance()}-/")
            exit_ATM()
        else:
            exit_ATM()

    #Check balance
    elif user_input == "3" or user_input == "Check balance" or user_input == "check balance":
        print(f"Your current balance is Rs {s1.get_balance()}-/")
        exit_ATM()
    #Invalid input
    else:
        print("Invalid. Please enter 1, 2 or 3")

def check_account():
    user = int(input("Enter your account number: "))
    if user == acc_no:
        user = int(input("Enter password: "))
        if user == acc_pass:
            ATM()
        else:
            print("password is wrong")
            exit_ATM()
    else:
        print("The account does not exist")
        exit_ATM()
    

def exit_ATM():
    exit = input("Do you want to exit the ATM? y/n: ")
    if exit == "n":
        check_account()
    else:
        print("Thanks for using our services!")

balance = 1000
#Build a dict for multiple acc_no and acc_pass
acc_no = 12345
acc_pass = 8182
acc_verified = False
s1 = account(123, balance) #Ask user_input their account no. and pass(maybe)

print("Welcome to the ATM.")
check_account()



#Problems in the code
#Amount does not get updated like if your balance is 1000 and you credited 100 then technically you should be able to debit 1100 but you won't be able to do operations beyond 1000.


#TO DO
#Build a proper system for multiple accounts
#ask user's their account number, if doesn't exist, ask wheather they want to register it or not - show just credit amount and check balance option until some amount is credited.
