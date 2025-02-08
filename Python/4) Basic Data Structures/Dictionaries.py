#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values{key, value}
#Ordered(When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.)
#Changeable(Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.)
#Duplicates(Dictionaries cannot have two items with the same key)

#Creating a dictionary
person={
    "name":"Usman",
    "email":"usmancodepro@gmail.com",
    "age":21,
    "city":"Karachi"
}
print(person);
#Creating a dictionary using dict keyword
person2=dict({
    "name":"RDJ",
    "email":"RDJ@gmail.com",
    "age":50,
    "age":20,#Duplicate will be overwritten
    "city":"NYC"
});
print(person2);

#Type of Dictionary <class 'dict'>
print(type(person2))

#Length of Dictionary 
print(len(person2));


#Nested Dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


