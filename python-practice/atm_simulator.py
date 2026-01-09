print("ATM Simulator")
print("Welcome!")

# Starting balance
balance = 100.0

# Control variable for the loop
running = "yes"

# Main loop
while running.lower() == "yes":  # Accept yes/Yes/YES
    print("\nMenu")
    print("1 = Check balance")
    print("2 = Deposit")
    print("3 = Withdraw")
    print("4 = Exit")
    print("5 = Reset balance")  # Optional challenge

    choice = input("Choose 1, 2, 3, 4, or 5: ")

    if choice == "1":
        print("Your balance is:", round(balance, 2))

    elif choice == "2":
        amount_text = input("Enter deposit amount: ")
        amount = float(amount_text)
        balance = balance + amount
        print("Deposit complete. New balance:", round(balance, 2))

    elif choice == "3":
        amount_text = input("Enter withdraw amount: ")
        amount = float(amount_text)

        if amount > balance:
            print("Not enough money. Withdrawal cancelled.")
        else:
            balance = balance - amount
            print("Withdrawal complete. New balance:", round(balance, 2))

    elif choice == "4":
        print("Goodbye!")
        running = "no"

    elif choice == "5":  # Optional: reset balance
        balance = 100.0
        print("Balance reset to:", round(balance, 2))

    else:
        print("Invalid choice")

    if running.lower() != "no":  # Ask to continue unless exiting
        running = input("Do you want to perform another operation? Type yes or no: ").lower()
