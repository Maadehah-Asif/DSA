#--------------------------------------------------------------------------------------------------------------
# <Method>	       <Description>
# append()	       Adds an element at the end of the list
# clear()	       Removes all the elements from the list
# copy()           Returns a copy of the list
# count()	       Returns the number of elements with the specified value
# extend()	       Add the elements of a list (or any iterable), to the end of the current list
# index()	       Returns the index of the first element with the specified value
# insert()	       Adds an element at the specified position
# pop()	           Removes the element at the specified position
# remove()	       Removes the item with the specified value
# reverse()	       Reverses the order of the list
# sort()	       Sorts the list
#--------------------------------------------------------------------------------------------------------------

List=[1,2,3];

#Append
List.append(4);
print(List);#Output:[1,2,3,4];

#Insert
List.insert(0,-1);
print(List);#Output:[-1,1,2,3,4];
List.insert(5,5);
print(List);#Output:[-1,1,2,3,4,5];

#Extend
List2=[6,7];
List.extend(List2);
print(List);#Output:[-1,1,2,3,4,5,6,7];


#remove
List3=[2,2,3];
List3.remove(2); #removes First Occurence
print(List3);#Output:[2,3];
List3.remove(3);
print(List3);#Output:[2];

#pop
List.pop();#Remove Last Element
print(List);#Output:[-1,1,2,3,4,5,6];
List.pop(6);#Removes 6th index
print(List);#Output:[-1,1,2,3,4,5];

#del keyword

del List[0];#Output:[1,2,3,4,5];
print(List);

del List; #Deletes Entire List
#print(List); Gives Error because List doesn't exist

#Clear
List=[x for x in range(5)];
print(List);#Output:[0,1,2,3,4];
List.clear();#Clears the list
print(List);#Output:[]


#sort 
List=[5,4,3,2,1]
List.sort();#Ascending
print(List);#[1,2,3,4,5];
List.sort(reverse=True);#Descending
print(List);#[5,4,3,2,1];
#Sort by key
List=["A","B","C","a","b","c"];
List.sort(key=str.lower);
print(List);#['A', 'a', 'B', 'b', 'C', 'c']
#Sorting by function 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)#[50, 65, 23, 82, 100]

#Reverse
List=[50,40,30,20,10];
List.reverse();
print(List);#[10,20,30,40,50]


#Count
List=[50,40,30,20,10]
count=List.count(10);
print("Count of 10 is: "+str(count));#Output:1

#Index
Index=List.index(20);
print("Index of 10 is: "+str(Index));#Output:3
