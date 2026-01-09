print("Tip Calculator")
print("This program calculates tip and total.")

again = "yes"

while again.lower() == "yes":
    # Get bill amount from user
    bill_text = input("Enter the bill amount (example 24.50): ")
    bill = float(bill_text)

    # Tip options menu
    print("Choose a tip option:")
    print("1 = 10%")
    print("2 = 15%")
    print("3 = 20%")
    print("4 = Custom %")

    tip_choice = input("Type 1, 2, 3, or 4: ")

    # Determine tip percentage
    if tip_choice == "1":
        tip_percent = 10
    elif tip_choice == "2":
        tip_percent = 15
    elif tip_choice == "3":
        tip_percent = 20
    elif tip_choice == "4":
        custom_text = input("Enter custom tip percent (example 18): ")
        tip_percent = float(custom_text)
    else:
        tip_percent = 0
        print("Invalid choice. Tip set to 0%.")

    # Calculate tip and total
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount

    # Round to 2 decimals for money format
    tip_amount = round(tip_amount, 2)
    total = round(total, 2)

    # Display results
    print("Tip:", tip_amount)
    print("Total:", total)

    # Ask if user wants to calculate another bill
    again = input("Calculate another bill? Type yes or no: ")

print("Thank you for using the Tip Calculator!")
