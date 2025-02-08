#Lists  in Python
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets

MYLIST =[1,2,3,"A","B","C",True,False,True,False];
print("\nMYLIST:",MYLIST);

#List Length
length=len(MYLIST);
print("\nLength of MYLIST: "+str(length));

#List Type
#lists are defined as objects with the data type 'list'
print("\nType of MYLIST: ",type(MYLIST)); #<class "list">

#Accessing Elements of a List
print("\nFirst element: ",MYLIST[0]);#First Item
print("\nLast element: ",MYLIST[-1]);#Last Item
#Slicing
print("\nElements in range from index 1(included) to 4(not included): ",MYLIST[1:4]);#1,2,3
print("\nFirst 4 elements: ",MYLIST[:4]);#First 4 elements
print("\nAll Elements from index 2: ",MYLIST[2:]);#All Elements from index 2
print("\n4th Last to 2nd Last Index: ",MYLIST[-4:-1]);#4th Last to 2nd Last Index
#Error on print(MYLIST[9]) #Out of bounds

#Check if Item exists in List 
Item="A"
if Item in MYLIST:
    print("\nItem is in MYLIST");
else: print("\nItem is not in MYLIST");

#Replacing Item
MYLIST[3]=4;
print("\nUpdated List: ",MYLIST);
#Replacing Item in Range
MYLIST[4:6]=[5,6];
print("\nUpdated List: ",MYLIST);
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
MYLIST[6:7]=[7,8];
print("\nUpdated List: ",MYLIST);
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
MYLIST[7:9]=[9];
print("\nUpdated List: ",MYLIST);


#Copying List
#Shallow Copy (&Reference)
List=[1,2,3];
List2=List;
List2[0]=-1;
print(List);
#Changes in List2 will also change List because of shallow copying
#Deep copy
NewList=[1,2,3];
CopyList=NewList.copy();
CopyList[0]=-1;
print(NewList);
#Changes in CopyList will not reflect NewList because of deep copying


#List Comprehension(List comprehension is a concise and elegant way to create lists in Python.)
#Syntax
#new_list = [expression for item in iterable if condition]

#Examples

#Generate a list of Squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

#even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

#Applying functions
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(5)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16]

