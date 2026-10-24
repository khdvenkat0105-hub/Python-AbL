#ATM Transaction Sequence Simulation(13th)
balance = float(input("Enter opening balance: Rs. "))
deposits = 0
withdrawals = 0

if balance < 0:
    print("Invalid opening balance")
else:
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: Rs. "))

            if amount > 0:
                balance = balance + amount
                deposits = deposits + amount
                print("Deposit successful")
            else:
                print("Invalid amount")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: Rs. "))

            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient balance")
            elif amount > 10000:
                print("Withdrawal limit exceeded")
            else:
                balance = balance - amount
                withdrawals = withdrawals + amount
                print("Withdrawal successful")

        elif choice == "3":
            print("Current balance: Rs.", round(balance, 2))

        elif choice == "4":
            break

        else:
            print("Invalid choice")

    print("\nTransaction Summary")
    print("Total deposits: Rs.", deposits)
    print("Total withdrawals: Rs.", withdrawals)
    print("Final balance: Rs.", round(balance, 2))
