#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets. ()
#Ordered(When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.)
#Unchanageable(Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.)

#Creating a tuple
tuple1=(1, 2, 3);
print(tuple1)

#Creating a tuple using tuple constructor
tuple2=tuple((1,2,3,4));
print(tuple2);

#One Element Tuple
tuple3=(1);#wrong way
print(type(tuple3));#type is int 


tuple4=(1,) #correct way
print(type(tuple4));#type is tuple


#Length of Tuple
tuple4=(1,2,3,4,5);
print(len(tuple4));#Output 5

#Tuple can hold any data type
tuple5=(1, 'a', 3.14, True);
print(tuple5);#Output: (1, 'a', 3.14, True)

#Accessing elements in a tuple
tuple6 = ("apple", "banana", "cherry");
print(tuple6[1]); #banana

#Checking if something exists in the tuple
tuple7 = ("apple", "banana");
if "apple" in tuple7: print("apple exists in the tuple");
else: print("apple does not exist in the tuple");

#Just like List, you can use negative indexing and : operator for accessing elements in a tuple

#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. But there are some workarounds.
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Update
tuple8 = ("apple", "banana", "cherry")
tuple9 = list(tuple8)
tuple9[1] = "kiwi"
tuple8 = tuple(tuple9)

print(tuple8)


#Add
#Method 1(List Conversion)
tuple10=(1,2,3);
print(tuple10);
temp=list(tuple10);
temp.append(4);
tuple10=tuple(temp);
print(tuple10);

#Method 2(Adding Tuple)
tuple11 = ("apple", "banana", "cherry")
temp = ("orange",)
tuple11 += temp

print(tuple11)


#Deleting
tuple12=(1,2,3);
temp=list(tuple12);
temp.pop(0);
tuple12=tuple(temp);
print(tuple12);

#Deleting Whole Tuple
del tuple12;
#print(tuple12); This will throw an exception


#Unpacking a Tuple
fruits = ("apple", "banana", "cherry");

(green, yellow, red) = fruits

print(green);#"apple"
print(yellow);#"banana"
print(red);#"cherry"

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
Alphabets = ("A", "B", "C", "D", "E")

(A, B, *C) = Alphabets

print(A)#A
print(B)#B
print(C)#["C","D","E"]

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red)#cherry


#Looping over a tuple
tuple13 = ("apple", "banana", "cherry")
for x in tuple13:
  print(x)


#Joining Two Tuple
Children=("A","B","C");
Parents=("X","Y");
Family=Parents+Children;
print(Family);#('X', 'Y', 'A', 'B', 'C')

#Multiplying Tuples by an integer
fruits = ("apple", "banana", "cherry")
fruits_X2 = fruits * 2
print(fruits_X2);#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#<Method>	<Description>
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

BigBossTuple=('I','AM','THE','FINAL','BOSS');

print(BigBossTuple.count('THE'));#1
print(BigBossTuple.index('THE'));#2

