num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
symbol = input("Enter action(+,-,*,/): ")
if symbol == "+":
    print(f"{num1} + {num2}: {num1 + num2}")
elif symbol == "-":
    print(f"{num1} - {num2}: {num1 - num2}")
elif symbol == "*":
    print(f"{num1} * {num2}: {num1 * num2}")
