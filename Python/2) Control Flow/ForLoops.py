#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#Initialize the array
people=["Osama Bin Laden","General Zia Ul Haq","Professor X","Xin Xon Xiang","Abdullah Gujjar"];

#Printing New Line
print();

#Iterating over people array and printing it and also connecting it with comma using end in print() function
for person in people:
    print(person,end=", ");

#Printing New Line
print("\n");

#Iterating over string and printing it and also connecting it with comma using end in print() function
for letter in 'Khabib':
    print(letter,end=", ");

#Printing New Line
print("\n");


#Iterating over range(5) and printing it and also connecting it with comma using end in print() function
for x in range(5):
    print(x,end=", ");



#Printing New Line
print();


#Iterating over range(-5,1) and printing it and also connecting it with comma using end in print() function
for x in range(-5,1):
    print(x,end=", ");

#Printing New Line
print();

#Iterating over range(0,30,3) and printing it and also connecting it with comma using end in print() function
for x in range(0,30,3):
    print(x,end=", ");

#Printing New Line
print();


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(0,6):
    print(x,end=",");
else:
    print("\nCounting from 1 to 5 finished.");
    

#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x+"-"+y)


#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in range(5):
  pass;
