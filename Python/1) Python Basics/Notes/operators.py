operators="""
Operators	                    Description

()	                            Parentheses	
**	                            Exponentiation	
+x  -x  ~x	                    Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                    Multiplication, division, floor division, and modulus	
+  -	                        Addition and subtraction	
<<  >>	                        Bitwise left and right shifts	
&	                            Bitwise AND	
^	                            Bitwise XOR	
|	                            Bitwise OR	
==  !=  >  >=  <  <=            Comparisons, identity, and membership operators
is  is not  in  not in 		
not	                            Logical NOT	
and	                            AND	
or	                            OR
""";

print(operators);


description ="""
1. () - Parentheses
Used for grouping expressions to control the order of evaluation.
Example: (2 + 3) * 4 evaluates 2 + 3 first, then multiplies by 4.

2. ** - Exponentiation
Raises a number to the power of another number.
Example: 2 ** 3 results in 8.

3. +x, -x, ~x - Unary Plus, Unary Minus, Bitwise NOT
+x: Returns x as is.
-x: Negates the value of x.
~x: Inverts all bits of x.
Examples: +3 results in 3, -3 results in -3, ~5 (bitwise NOT) results in -6.

4. *, /, //, % - Multiplication, Division, Floor Division, Modulus
*: Multiplies two numbers.
/: Divides one number by another, returns a float.
//: Performs floor division, returning the integer part.
%: Returns the remainder of division.
Examples: 5 * 2 results in 10, 5 / 2 results in 2.5, 5 // 2 results in 2, 5 % 2 results in 1.

5. +, - - Addition and Subtraction
+: Adds two numbers or concatenates strings.
-: Subtracts one number from another.
Examples: 5 + 3 results in 8, 5 - 3 results in 2.

6. <<, >> - Bitwise Left and Right Shifts
<<: Shifts the bits of a number to the left by a specified number of positions.
>>: Shifts the bits to the right.
Examples: 2 << 1 shifts left to 4, 4 >> 1 shifts right to 2.

7. & - Bitwise AND
Performs a bitwise AND operation on each bit.
Example: 5 & 3 results in 1.

8. ^ - Bitwise XOR
Performs a bitwise XOR (exclusive OR) operation on each bit.
Example: 5 ^ 3 results in 6.

9. | - Bitwise OR
Performs a bitwise OR operation on each bit.
Example: 5 | 3 results in 7.

10. ==, !=, >, >=, <, <= - Comparisons
==: Checks if two values are equal.
!=: Checks if two values are not equal.
>, <, >=, <=: Used for comparisons.
Examples: 5 == 5 is True, 5 != 3 is True, 5 > 3 is True.

11. is, is not, in, not in - Identity and Membership Operators
is: Checks if two variables refer to the same object.
is not: Checks if two variables do not refer to the same object.
in: Checks if an element exists within a sequence.
not in: Checks if an element does not exist within a sequence.
Examples: x is y checks if x and y are the same object, 'a' in 'apple' is True.

12. not - Logical NOT
Negates a boolean value.
Example: not True results in False.

13. and - Logical AND
Returns True if both operands are True.
Example: True and False results in False.

14. or - Logical OR
Returns True if at least one operand is True.
Example: True or False results in True.
""";


#print(description);