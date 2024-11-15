# Simple Calculator Program

# Step 1: Get user input
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))  
operation = input("Enter the operation (+, -, *, /): ") 

# Step 2: Perform calculation based on the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if dividing by zero
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

# Step 3: Output the result
print(f"The result of {num1} {operation} {num2} is: {result}")
