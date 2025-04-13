# Question 4: Input and Type Conversion
# 4. Write a program that:
#   - Asks the user for their first name, last name, and age using the input() function.
#   - Converts the age input to an integer and then calculates the year they were born by subtracting their age from the current year (use 2025 as the current year).
#   - Print a sentence that includes their full name and the year they were born.

fname=input("enter first name:");
lname=input("enter last name:");
age=input("enter age:");

age=int(age);
print(age);
year=2025-age;
print (year);
year=str(year);
print(" first name  " +  fname +" last name " + lname +" year  "+ year);