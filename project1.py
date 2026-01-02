print("Welcome to ATM Simulator!")
security_pin = int(input("To start transactions, you have to type your transaction pin: "))

while (True):
    recheck = int(input("Re-enter the transaction pin: "))
    if (recheck == security_pin):
        print("Transaction Pin set!\n")
        break
    else:
        print("Above Pin doesn't match with your pin.")

balance = 0.0
while (True):
    print("ATM Menu: \n1. Deposit \n2. Withdraw \n3. Check balance \n4. Exit")
    choice = int(input("Enter your choice (1-4): "))

    match (choice):
        case 1:
            deposit = float(input("\nEnter the amount to be deposited: "))
            if (deposit > 0):
                pin = int(input("Enter the Transaction Pin: "))
                if (pin == security_pin):
                    balance += deposit
                    print("Money Deposited Successfully!\n")
                else:
                    print("Invalid Transaction Pin!")
                    print("Money Deposited Failed!\n")
            else:
                print("Invalid deposit amount!")
                print("Money Deposited Failed!\n")
        
        case 2:
            withdraw = float(input("\nEnter the amout to be withdraw: "))
            if (withdraw > 0):
                if (withdraw < balance):
                    pin = int(input("Enter the Transaction Pin: "))
                    if (pin == security_pin):
                        balance -= withdraw
                        print("Money Withdrew Successully!\n")
                    else:
                        print("Invalid Transaction Pin!")
                        print("Money Deposited Failed!\n")
                else:
                    print("Insufficient balance!")
                    print("Money Withdrawal Failed!\n")
            else:
                print("Withdrawal amount must be positive.")
                print("Money Withdrawal Failed!\n")
        
        case 3:
            pin = int(input("\nEnter the Transaction Pin: "))
            if (pin == security_pin):                    
                print("Current Balance: $" + str(balance) + "\n")
            else:
                print("Invalid Transaction Pin!")
                print("Try Again!\n")

        case 4:
            print("\nThank you for banking with us. Goodbye!")
            break

        case _:
            print("\nInvalid Selection. Please choose 1, 2, 3 or 4.")