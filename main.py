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
    user = input("Choose any one option:\n1. Credit\n2. Debit\n3. Check balance\n=> ")
    #Credit
    if user == "1" or user == "Credit" or user == "credit":
        amount = int(input("Enter your amount: "))
        print(s1.credit(amount))
        check_balance = input("Do you want to check your current balance? y/n: ")
        if check_balance == "y":
            print(f"Your current balance is Rs {s1.get_balance()}-/")
        else:
            print("Thanks for using our services!!")

    #Debit
    elif user == "2" or user == "Debit" or user == "debit":
        amount = int(input("Enter your amount: "))
        #Print invalid amount if amount > balance
        if amount <= balance:
            print(s1.debit(amount))
        else:
            print("Please enter a valid amount.")
        check_balance = input("Do you want to check your current balance? y/n: ")
        if check_balance == "y":
            print(f"Your current balance is Rs {s1.get_balance()}-/")
        else:
            print("Thanks for using our services!!")

    #Check balance
    elif user == "3" or user == "Check balance" or user == "check balance":
        print(f"Your current balance is Rs {s1.get_balance()}-/")

    #Invalid input
    else:
        print("Invalid. Please enter 1, 2 or 3")

balance = 1000
s1 = account(123, balance) #Ask User their account no. and pass(maybe)

print("Welcome to the ATM.")
ATM()
exit = input("Do you want to exit the ATM? y/n: ")
if exit == "n":
    ATM()
else:
    print("Thanks for using out services!")

#Problems in the code
#Amount does not get updated like if your balance is 1000 and you credited 100 then technically you should be able to debit 1100 but you won't be able to do operations beyond 1000.
#Secondly, the "Do you want to exit ATM" is asked only  once; first time.