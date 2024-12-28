#Recursion is a programming technique where a function calls itself in order to solve a problem. It divides a problem into smaller subproblems and solves them using the same function.

#How Recursion Works:
    #Base Case: This is the condition under which the recursion stops, preventing the function from calling itself indefinitely.
    #Recursive Case: This is where the function calls itself with a modified argument to solve the smaller subproblem.


#General Structure of Recursive Function
    # def recursive_function(parameters):
    #     # Base case: condition to stop recursion
    #     if base_case_condition:
    #         return some_value
        
    #     # Recursive case: calling the function recursively
    #     else:
    #         return recursive_function(modified_parameters)

# Example of a factorial using Recursion
def factorial(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n * factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Testing the function
print(factorial(5))  # Output: 120
