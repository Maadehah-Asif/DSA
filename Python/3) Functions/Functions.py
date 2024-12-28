#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Covered Here

#1)Function Definition and Calling
#2)Parameter vs Arguments
#3)Arbitrary Arguments(*Args)
#4)Keyword arguments(age=12)
#5)Arbitrary keyword arguments(**kwArgs)
#6)Return Functions
#7)Positional Only Arguments(/)
#8)Keyword Only Arguments(*)

print("1)Function Definition and Calling");
#Function Declaration and Calling
def My_First_Python_Function():
    print("Hello, This is my first Python function!");
    
My_First_Python_Function();
print();


print("2)Parameter vs Arguments");
#Parameters VS Arguments

#Arguments: An argument is the value that is sent to the function when it is called.
#Parameters: A parameter is the variable listed inside the parentheses in the function definition.
#Example:

#Name and Age are Parameters
def my_func(name,age=20):
    print("Hello, " + name + "! "  )
    print("You are " + str(age) + " years old.");

my_func("Usman", 21); #Usman and 21 are Arguments
print();

my_func("Someone"); #Default Parameter in Action
print();


print("3)Arbitrary Arguments(*Args)");
#Arbitrary Arguments(*args)
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def greet(*args):
    for name in args:
        print("Hello, " + name + "!");
greet("Usman", "Ali", "Sara"); 
print();

#Combinations of Simple and Arbitrary Arguments
def introduce(greeting,*args):
    for name in args:
        print(greeting+" "+name+"!");
introduce("Hello", "Abdullah", "Anhar", "Ahtisham");
print();

introduce("Greetings","Lucky", "Paras", "Haider");
print();


print("4)Keyword arguments(age=12)");
#Keyword Arguments
def greeting(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Using keyword arguments
greeting(name="Usman", age=21)
print();
greeting(age=25, name="Ali")  # Order doesn't matter when using keyword arguments
print();


print("5)Arbitrary Keyword Arguments(**kwArgs)");
#Arbitrary Keyword Arguments(**kwargs)
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Passing keyword arguments
person_info(name="Usman", age=21, profession="Software Engineer")
print();



#Passing List as Arguments
weapons=["AK-47","AWP","UZI","GLOCK","WOMEN"];
def display_weapons(weapons):
    for weapon in weapons:
        print(weapon,end=",");
display_weapons(weapons);

print();


print("6)Return Functions");
#Return Values
#To let a function return a value, use the return statement:

def sum(*args):
    sum=0;
    for x in args:
        sum+=x;
    return sum;
print("Sum of given numbers:",sum(1,2,3,4,5));

print();

print("7)Positional Only Arguments(/)");
#Positional Only Arguments
def add(a, b, /):
        # a and b must be passed positionally
        # No Keyword arguments allowed
    return a + b
print(add(5, 3))  # Valid
#print(add(a=5, b=3))  # Invalid: TypeError
print();

print("8)Keyword Only Arguments(*)");
#Keyword Only Arguments
def greet2( *, country="USA",name, age):
    # No Positional Argument Allowed
    # Keyword Argument Must
    print(f"Hello {name}, you are {age} years old, and you live in {country}.")

# Valid calls
greet2(name="Usman", age=21, country="Pakistan")
print();
greet2(name="Usman", age=21) # With Default Parameters
print();

# Invalid call: TypeError as 'country' is a keyword-only argument
#greet2("Sara", 25, "Canada")  # Invalid: 'country' must be passed as a keyword

#Combining Positional and Keyword Argument
def my_combined_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_combined_function(5, 6, c = 7, d = 8)


