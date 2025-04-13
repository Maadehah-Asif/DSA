#lambda functions
#lambda functions are a way to create small, anonymous functions without the need for a full function definition using the def keyword.

#Syntax: lambda arguments: expression
#lambda: The keyword used to define the function.
#arguments: The parameters the function will take (can be multiple).
#expression: A single expression whose result will be returned by the function.

#Key Points:
#Lambda functions are anonymous—they do not have a name unless assigned to a variable.
#Lambda functions can have multiple arguments, but they can only contain one expression (no statements).
#The expression is evaluated and returned automatically; no need to use the return keyword.

# A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# A lambda function that squares a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

#When to Use Lambda Functions?
#Short Functions: When you need a simple function for a short task.
#Functional Programming: For operations like map(), filter(), and reduce() that work with iterables.
#Quick Functions: When you don't want to define a whole function using def.

