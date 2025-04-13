# Question 2: Arbitrary Arguments (*args) and Keyword Arguments
# 2. Write a function that takes a greeting message as the first parameter followed by an arbitrary number of names.
#    The function should print a greeting message for each name in the list (e.g., "Hello, <name>!").
#    Also, write a function that takes the name, age, and country as keyword arguments and prints a message like:
#    "Hello, <name>. You are <age> years old and you live in <country>."

def func(greet,*a):
    for i in a:
        print(greet+"  "+ i);

func("hiiiiii","a","b","c");

def func1(a,b,c):
    print(f"hi {a}, u r {b} and u live in {c} "); #DO NOT MISS THE 'f'


func1(c="pak",a="ali",b=16);
