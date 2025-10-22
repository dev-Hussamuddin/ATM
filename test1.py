account_details = {
    "00001" : "8182",
    "00002" : "5152",
    "00003" : "1234"
}

# print(account_details)

user_input = input("Enter your account number: ")
if user_input in account_details:
    print("yea")
else:
    print("oh no")


#TO Do
#1. How to append key value in a dict
#2. If a key exist in the dict or not