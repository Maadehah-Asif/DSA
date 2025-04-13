#Basic try-except (Handling a Single Exception)
try:
    num = int(input("Enter a number: "))  # User enters a string instead of a number
    print("You entered:", num)
except ValueError:
    print("Oops! That was not a valid number.")


# Handling Multiple Exceptions
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")


#Catching Any Exception
try:
    print(10 / 0)  # This causes a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)


# Using else (Runs if no error occurs)
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("No errors occurred! ✅")


# Using finally (Always Runs, Even if There’s an Error)
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")


# Raising Exceptions (raise)
def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older!")
    print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print("Error:", e)


# Custom Exceptions
# A custom exception is a class that inherits from Python’s Exception class.

# Step 1: Define a Custom Exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    pass

# Step 2: Use the Custom Exception
def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("Valid number:", num)

# Step 3: Handle the Exception
try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)


