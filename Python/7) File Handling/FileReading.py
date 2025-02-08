# File Handling

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.


# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Syntax for opening and closing a file
f = open("demofile.txt") #Same Code as below
# f = open("demofile.txt", "rt")
# "r" for read, and "t" for text are the default values, you do not need to specify them.
f.close();
# It is a good practice to always close the file when you are done with it.



# Syntax for reading a file as a whole
f = open("demofile.txt") 
print(f.read());
f.close();


# Syntax for reading a file by the number of characters
f = open("demofile.txt") 
print(f.read(5));
f.close();

# Syntax for reading a file line by line
f = open("demofile.txt") 
print(f.readline());
print(f.readline());
f.close();

# Syntax for looping a file line by line
f = open("demofile.txt") 
for x in f:
    print(x);
f.close();



