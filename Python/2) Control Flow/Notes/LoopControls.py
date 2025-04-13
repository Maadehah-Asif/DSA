#Break(Stops the loop if certain conditions are met)
#Continue(Skips the current iteration if conditions are met)
#Pass(Does nothing, Just a Placeholder)

# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using break
for num in numbers:
    if num == 5:  # Stop the loop if the number is 5
        print("Breaking at:", num)
        break
    print(num, end=",");

print()  # Empty line for readability

# Using continue
for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num,end="")  # Only odd numbers are printed

print()  # Empty line for readability

# Using pass
for num in numbers:
    if num == 3:  # Do nothing if the number is 3
        pass
    else:
        print(num,end=",")  # Print all numbers except 3
