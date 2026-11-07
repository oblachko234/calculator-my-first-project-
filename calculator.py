num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
symbol = input("Enter action(+,-,*,/): ")
if symbol == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif symbol == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif symbol == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif symbol == "/":
    if num2 == 0.0:
        print("Error: Division by zero is not allowed!")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input!")

