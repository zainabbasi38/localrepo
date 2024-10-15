a = int(input("Enter number:"))
b = int(input("Enter number:"))

operation = input("Please enter an operator (+,-,*,/):" )

if operation == "+":
    total = a + b
    print(f"total: {total}")

elif operation == "-":
    total = a - b
    print(f"total: {total}")

elif operation == "*":
    total = a * b
    print(f"total: {total}")

else:
    total = a / b 
    print(f"total: {total}")
