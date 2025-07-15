first = float(input("Enter first numebr: "))
second = float(input("Enter second number: "))
operation = str(input("Enter operation(+,-,*,/): "))

if operation == "+":
	print(f"Result: {first + second}")

elif operation == "-":
	print(f"Result: {first - second}")

elif operation == "*":
	print(f"Result: {first * second}")

elif operation == "/":
	print(f"Result: {first / second}")

else:
	print("Unknown operation!")

