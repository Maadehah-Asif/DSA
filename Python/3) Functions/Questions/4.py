# Question 4: Higher-Order Functions
# 4. Write a higher-order function that takes a number and a function as arguments. 
#    The function should apply the passed function to the number and return the result.
#    Test the higher-order function with both a lambda function that doubles the number and another function that squares it.


def high_order(func,num):
    return func(num);

print(high_order(lambda x: x+3,1));


l=lambda x: x*x;


def square(x):
    return x*x;

print (high_order(l,6));
print(high_order(square,2));