# Question 5: Recursion
# 5. Write a recursive function that calculates the factorial of a given number.
#    Test the function by calculating the factorial of 5 and print the result.

def func(x):
    if (x==1):
        return 1;
    else:
        return x*func(x-1);

print(func(4));