# print("Hello, World! I'm starting my coding journey 🚀")

# # Storing some information about me
# name = "Rohit"
# experience_years = 3.9
# goal = "Learn Python + Data Engineering"

# print("Name:", name)
# print("Experience:", experience_years, "years")
# print("Goal:", goal)

# Working with numbers

# Integers
age = 30
print("Age:", age)

# Floating point (decimal numbers)
height = 5.9
print("Height:", height)

# Basic math
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)    # result will be a decimal
print("Floor Division:", a // b)  # gives whole number only
print("Remainder:", a % b)
print("Power:", a ** b)  # 10 to the power of 3

# Strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String repetition
laugh = "ha"
print(laugh * 3)  # prints 'hahaha

salary = 50000
print("My salary is", salary, "per month")

# Asking the user for input
name = input("What is your name? ")
print("Hello", name, "welcome to Python!")

# Simple calculator
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# input() gives strings, so we convert them to numbers
num1 = float(num1)
num2 = float(num2)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# BMI Calculator
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
