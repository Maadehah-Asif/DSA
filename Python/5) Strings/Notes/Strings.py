# Topic 1 - Strings in General

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
print('Hello, World!')

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
# Note: in the result, the line breaks are inserted at the same position as in the code.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[0])  # Output: H


# Looping Through a String
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a)) #Output:13

# Check String
txt = "The best things in life are free!"
print("free" in txt) #Output:True


# Topic 2 - Slicing in Strings

# Slicing

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5]) # Output: llo

# Slice From the Start
b = "Hello, World!"
print(b[:5]) #Output: Hello

# Slice To the End
b = "Hello, World!"
print(b[2:]) #Output: llo, World!

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2]) #Output: orl


