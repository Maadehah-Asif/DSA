# <Method>	                <Description>
# clear()	                Removes all the elements from the dictionary
# copy()	                Returns a copy of the dictionary
# fromkeys()	            Returns a dictionary with the specified keys and value
# get()	                    Returns the value of the specified key
# items()               	Returns a list containing a tuple for each key value pair
# keys()	                Returns a list containing the dictionary's keys
# pop()                    	Removes the element with the specified key
# popitem()	                Removes the last inserted key-value pair
# setdefault()	            Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	                Updates the dictionary with the specified key-value pairs
# values()	                Returns a list of all the values in the dictionary


# Creating a sample dictionary for demonstration
dict1 = {"name": "Alice", "age": 25, "city": "New York"}

# 1. clear() - Removes all the elements from the dictionary
dict1.clear()
print("After clear():", dict1)  # Output: {}

# Creating a new dictionary for the following methods
dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
    }

# 2. copy() - Returns a copy of the dictionary
dict_copy = dict1.copy()
print("After copy():", dict_copy)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 3. fromkeys() - Returns a dictionary with the specified keys and a default value
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("After fromkeys():", new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# 4. get() - Returns the value of the specified key
age = dict1.get("age")
print("After get('age'):", age)  # Output: 25

# 5. items() - Returns a list containing a tuple for each key-value pair
items = dict1.items()
print("After items():", list(items))  # Output: [('name', 'Alice'), ('age', 25), ('city', 'New York')]

# 6. keys() - Returns a list containing the dictionary's keys
keys = dict1.keys()
print("After keys():", list(keys))  # Output: ['name', 'age', 'city']

# 7. pop() - Removes the element with the specified key
removed_item = dict1.pop("city")
print("After pop('city'):", dict1)  # Output: {'name': 'Alice', 'age': 25}
print("Removed item:", removed_item)  # Output: New York

# 8. popitem() - Removes the last inserted key-value pair
last_item = dict1.popitem()
print("After popitem():", dict1)  # Output: {'name': 'Alice'}
print("Removed last item:", last_item)  # Output: ('age', 25)

# 9. setdefault() - Returns the value of the specified key. If the key does not exist: inserts the key with the specified value
# If 'gender' is not in dict1, it will insert 'gender' with the value 'Female'
gender = dict1.setdefault("gender", "Female")
print("After setdefault('gender', 'Female'):", dict1)  # Output: {'name': 'Alice', 'gender': 'Female'}
print("Gender:", gender)  # Output: Female

# 10. update() - Updates the dictionary with the specified key-value pairs
dict1.update({"age": 26, "city": "Los Angeles"})
print("After update():", dict1)  # Output: {'name': 'Alice', 'gender': 'Female', 'age': 26, 'city': 'Los Angeles'}

# 11. values() - Returns a list of all the values in the dictionary
values = dict1.values()
print("After values():", list(values))  # Output: ['Alice', 'Female', 26, 'Los Angeles']



#Looping through the dictionary
Person={
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

#Looping Keys Only
for keys in Person:
    print(keys,end=",")


#Looping Values Only
for values in Person.values():
    print(values,end=",")

print()
#Looping Keys Value Pair 
for key,values in Person.items():
    print(key,": ",values)


# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25, "city": "New York"},
    "person2": {"name": "Bob", "age": 30, "city": "Los Angeles"},
    "person3": {"name": "Charlie", "age": 35, "city": "Chicago"}
}

# Looping through the outer dictionary (the main keys: person1, person2, person3)
for person, details in nested_dict.items():
    print("Details for:"+person)
    
    # Looping through the inner dictionary (name, age, city)
    for key, value in details.items():
        print(key+":"+str(value))
    print()  # Adding an empty line for better readability
