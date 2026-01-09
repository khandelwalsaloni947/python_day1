number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation  = input("Enter operation (+,-,*,%,/): ")

if operation  == "+":
    print("Result is :", number1 + number2)
elif operation  == "-":
    print("Result is :", number1 - number2)
elif operation  == "*":
    print("Result is :", number1 * number2)
elif operation  == "%":
    print("Result is :", number1 % number2)
elif operation  == "/":
    print("Result is :", number1 / number2)


else:
    print("Please enter correct operation example: +,-,*,%,/")
    operation  = input("Enter operation (+,-,*,%,/): ")