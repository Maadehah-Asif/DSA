# Question 2: For Loop Iteration
# 2. Write a for loop to:
#    - Iterate over a list of people's names and print each name followed by a comma.
#    - Iterate over a string and print each letter separated by a comma.
#    - Iterate over a range of numbers (3 to 8) and print each number separated by a comma.
#    - Iterate over a range of numbers (from -5 to 15) and print each number separated by a comma.
#    - Iterate over a range of numbers (from 0 to 50 with a step of 10) and print each number separated by a comma.

names=['a','b','c','d'];

for name in names:
    print(name+","); # the + gives new line 


word="hello";

for i in word:
    print(i,end=','); # using varable end stays in same line

for i in range(3,8):
    print(i,end=','); # producing correct code bcz int and character 

for i in range(-5,15):
    print(str(i)+","); # giving error because int and string , so use str()

for i in range(0,50,10):
    print(str(i)+","); # IMPORTANT: range max value is not inlcuded 