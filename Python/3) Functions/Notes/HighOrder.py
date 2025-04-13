from functools import reduce

#Higher-Order Functions in Python

 #A higher-order function is a function that:
    #Takes one or more functions as arguments (i.e., functions can be passed as parameters). 
    #Returns a function as a result (i.e., functions can be returned as output).
    #Higher-order functions are a fundamental concept in functional programming, and Python supports them fully.

#Key Characteristics of Higher-Order Functions: [both can exist OR only either one can exist]
    #Accepting Functions as Arguments: Functions can be passed as arguments to other functions.
    #Returning Functions: Functions can return other functions.


#Two Typpes of Higher-Order Functions
    #1) Custom Functions
    #2) Built-in Functions


#Example: A Custom Higher-Order Function
    # Higher-order function that returns another function
def multiplier(factor):
    return lambda x: x * factor

# Get a function that multiplies by 2
double = multiplier(2)

# Call the returned function
print(double(5))  # Output: 10

"""
Breakdown of the Code:

1.  Higher-Order Function `multiplier(factor)`:
    - `multiplier()` takes one parameter `factor` and returns a new function that multiplies any input `x` by the given `factor`.
    - The `lambda x: x * factor` is an anonymous function (a lambda function) that takes `x` as an input and multiplies it by `factor`.
    - `multiplier()` is a higher-order function because it returns a function that can be called later.

2.  Creating `double`:
    - `double = multiplier(2)` calls the `multiplier()` function with an argument of `2`.
    - The returned function (the `lambda x: x * 2`) is then assigned to the variable `double`.

3.  Calling the `double` function:
    - `double(5)` calls the function that was returned by `multiplier(2)` with `5` as the input.
    - Inside the lambda function, `5` gets multiplied by `2`, and the result `10` is returned.

Explanation:

- The higher-order function `multiplier` is used to create specialized functions that multiply by a specific factor. In this case, `double` is a function that multiplies its input by `2`.
- By using higher-order functions, you can dynamically generate functions based on the parameters passed to the higher-order function.
"""



#Example: Built in High-Order Functions


# A function to sum two numbers
def add(x, y):
    return x + y

# Using reduce to sum all elements in the list
numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)  # Output: 10

# SOME KEY BUILT IN HIGH ORDER FUNCTIONS
    #map(): Apply a function to all items in an iterable.
    #filter(): Filter items in an iterable based on a function.
    #reduce(): Apply a function cumulatively to reduce an iterable to a single value.
    #sorted(): Return a sorted list from an iterable.
    #all(): Return True if all elements are True.
    #any(): Return True if any element is True.
    #zip(): Combine iterables into tuples.
    #enumerate(): Add a counter to an iterable.
    #reversed(): Return an iterator that accesses the elements in reverse order.
    #max() / min(): Return the largest or smallest item in an iterable.
    #id(): Get the unique identifier of an object.
    #callable(): Check if an object is callable.
    #staticmethod() / classmethod(): Convert methods to static/class methods.
    #property(): Create a property for a class attribute.