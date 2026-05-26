'''
ATM PROJRCT:
'''

user_info = {
    "Name": "sravyasri",
    "Mobile no": "",
    "ATM pin": "2619",
    "Balance": 56000,
    "Transaction History": []
}

print("Please insert your ATM card")
remaining_attempts = 3
while remaining_attempts > 0:
    pin = input("Enter 4 digit PIN: ")
    if len(pin) == 4:
        if pin == user_info["ATM pin"]:
            print("Welcome to ATM")
            break
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left")
            else:
                print("Your ATM is temporarily blocked")
    else:
        print("PIN must contain exactly 4 digits")


balance = 56000
 
choice = int(input("Enter \n1.Deposit \n2.Withdraw \n3.Balance\n"))
if choice == 1:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Amount deposited successfully")
    print("Current balance:", balance)
elif choice == 2:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Please collect cash")
        print("Current balance:", balance)
    else:
        print("Insufficient balance")
elif choice == 3:
    print("Current balance:", balance)
else:
    print("Invalid choice")
        
    
    
            











        
        



