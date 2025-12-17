# main.py

import calculator

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division:", calculator.divide(num1, num2))
