# Question 1: Dictionary Operations
# 1. Create a dictionary to store information about a person: name, age, and city.
#    - Add a new key-value pair for "email".
#    - Remove the "age" key from the dictionary.
#    - Use the 'get()' method to retrieve the person's name.
#    - Use the 'update()' method to update the person's city.
#    - Print the final dictionary.


info={

"name":"me",
"age": -90,
"city": "hell"

}

print(info);

info.update({"email":"bzzz","money":0});

print(info);

val=info.values();

print  (val);
print  (list(val)); #same thing as above just diff presnattion of output on terminal 

print()
for val in info.values():
    print(val,end=",");




info.pop("age");

print(info.get("name"));


info.update({"city":"isloooooo"});
print(info);


