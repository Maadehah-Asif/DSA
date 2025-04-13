#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are written with curly brackets. {}
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered(Set items can appear in a different order every time you use them, and cannot be referred to by index or key.)
#Unchangeable(Set items are unchangeable, meaning that we cannot change the items after the set has been created.)
#Sets cannot have two items with the same value.(for example,If set have duplicate values,they  will be ignored.)


#Creating a set
Set1={1,2,3};
print(Set1);
#Through Constructor
Set2=set({4,5,6});
print(Set2);


#Duplicate values will be ignored
Set3={1,2,2,3,3,3};
print(Set3); #{1,2,3}

#True and 1 and False and 0 are considered duplicate values in set
Set4={True,1,False,0};
print(Set4); #{1,0}

#Set Type <class 'set'>
print(type(Set1));

#Set can hold multiple data types
Set5={"A",1,1.2,False};
print(Set5);

#Length of Set
print(len(Set5));


#Accessing elements of set
#You cannot access items in a set by referring to an index or a key.
Set6={1,2,3,4};
#Looping over elements in sets
for x in Set6:
    print(x,end=",");
#Checking If Some Element Exists in Set
if 1 in Set6:
    print("\nElement 1 is present in Set6");