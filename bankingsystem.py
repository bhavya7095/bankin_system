def banking_system():
    print("Welcome to SBI Bank")
balance = 0
transactions = []
while True:
    print("\n----- SBI Banking Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Check")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice: ")
    #deposit option
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            transactions.append("Deposited: Rs. " + str(amount))
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")
        #deposit option
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            transactions.append("Withdrawn: Rs. " + str(amount))
            print("Amount withdrawn successfully.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
        #balance check option
    elif choice == "3":
        print("Your current balance is: Rs.", balance)
    #transaction history option
    elif choice == "4":
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in transactions:
                print(transaction)
    #exit option
    elif choice == "5":
        print("Thank you for using SBI Bank.")
        break
    else:
        print("Invalid choice. Please try again.")
banking_system()