# Operators Examples

# 1. Parentheses ()
result = (2 + 3) * 4  # Grouping for order of operations
print("Parentheses:", result)  # Output: 20

# 2. Exponentiation **
power = 2 ** 3  # 2 raised to the power of 3
print("Exponentiation:", power)  # Output: 8

# 3. Unary Plus, Unary Minus, Bitwise NOT (+x, -x, ~x)
a = 3
print("Unary Plus:", +a)    # Output: 3
print("Unary Minus:", -a)    # Output: -3
print("Bitwise NOT:", ~a)    # Output: -4 (flips bits)

# 4. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
print("Multiplication:", 5 * 2)   # Output: 10
print("Division:", 5 / 2)         # Output: 2.5
print("Floor Division:", 5 // 2)  # Output: 2
print("Modulus:", 5 % 2)          # Output: 1

# 5. Addition and Subtraction (+, -)
print("Addition:", 5 + 3)   # Output: 8
print("Subtraction:", 5 - 3)   # Output: 2

# 6. Bitwise Left and Right Shifts (<<, >>)
print("Left Shift:", 2 << 1)  # Output: 4 (2 shifted left by 1)
print("Right Shift:", 4 >> 1)  # Output: 2 (4 shifted right by 1)

# 7. Bitwise AND (&)
print("Bitwise AND:", 5 & 3)   # Output: 1 (binary: 0101 & 0011 = 0001)

# 8. Bitwise XOR (^)
print("Bitwise XOR:", 5 ^ 3)   # Output: 6 (binary: 0101 ^ 0011 = 0110)

# 9. Bitwise OR (|)
print("Bitwise OR:", 5 | 3)   # Output: 7 (binary: 0101 | 0011 = 0111)

# 10. Comparisons (==, !=, >, >=, <, <=)
print("Equality:", 5 == 5)  # Output: True
print("Inequality:", 5 != 3)  # Output: True
print("Greater Than:", 5 > 3)   # Output: True
print("Greater or Equal:", 5 >= 5)  # Output: True
print("Less Than:", 3 < 5)   # Output: True
print("Less or Equal:", 3 <= 3)  # Output: True

# 11. Identity and Membership Operators (is, is not, in, not in)
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("is:", x is y)         # True, x and y refer to the same object
print("is not:", x is not z) # True, x and z are different objects
print("in:", 1 in x)         # True, 1 is in the list x
print("not in:", 4 not in x) # True, 4 is not in the list x

# 12. Logical NOT (not)
is_active = False
print("Logical NOT:", not is_active)  # Output: True (inverts the value)

# 13. Logical AND (and)
a = True
b = False
print("Logical AND:", a and b)  # Output: False (both conditions need to be True)

# 14. Logical OR (or)
a = True
b = False
print("Logical OR:", a or b)   # Output: True (only one condition needs to be True)
