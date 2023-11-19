# 1. Assignmnent Operator.

print("Assignment Operator");

# The assignment operator is used to assign a value to a variable:
age = 20;

# To assign a variable value to another variable:
my_age = age;
print(age);
print(my_age);
age = 21;
print(age);
print(my_age);

# walrus operator
# Without walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared = num ** 2
    squared_numbers.append(squared)

print(squared_numbers)

# With walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = [squared := num ** 2 for num in numbers]

print(squared_numbers)

# 2. Arithmetic Operator.

print("Arithmetic Operator");

# Addition
print(f"Addition: {5 + 2}");

# Subtraction
print(f"Subtraction: {5 - 2}");

# Multiplication
print(f"Multiplication: {5 * 2}");

# Division and Floor Division
print(f"Division: {5 / 2} , Floor Division: {5 // 2}");

# Exponentiation or Power
print(f"Exponentiation: {5 ** 2}");

# Remainder or modulus.
print(f"Modulus: {5 % 2}");

#  unary minus operator
print(f"Unrinary Minus Operator: {-5 + 4}");

# Arithemetic operator + can be used to concatenate string values.
print(f"Conactenate two strings: {'United States ' + 'America'}");

# We can combine the assignment operator with arithmetic operators:

print("We can combine the assignment operator with arithmetic operators.")
age = 1

age += 1; # age = age + 1
print(age) # 2

age -= 1; # age = age - 1
print(age) # 1

age *= 1; # age = age * 1
print(age) # 1

age /= 1; # age = age / 1
print(age) # 1.0 Result in division is always float.

age **= 1; # age = age ** 1
print(age) # 1.0 

age //= 1; # age = age // 1
print(age) # 1.0

age %= 1; age = age % 1
print(age); # 0.0

print(f"Float Floor Division: {1.5 // 1}") 
# print(f"Int Floor Division: {6 // }") 

# 3. Comparison Operators.

print("Comparison Operators")

# You can use those operators to get a boolean value ( True or False ) depending on the result.
# Equal operator (==)
print(f"Equal to Operator: {5 == 5}"); # output: True

# Not Equal operator (!=)
print(f"Not Equal to Operator: {2 != 3}"); # output: True
print(f"Not Equal to Operator: {2 != 2}"); # output: False

# Greater than Operator
print(f"Greater than Operator: {5 > 3}"); # Output: True
print(f"Greater than Operator: {5 > 10}"); # Output: False

# Greater than or Equal to Operator
print(f"Greater than Equal to Operator: {5 > 5}"); # Output: False
print(f"Greater than Equal to Operator: {5 >= 5}"); # Output: True

# Lesser than Operator
print(f"Lesser than Operator: {5 < 6}"); # Output: True
print(f"Lesser than Operator: {5 < 3}"); # Output: False

# Lesser than or equal to operator.
print(f"Lesser than Equal to Operator: {5 < 5}"); # Output: False
print(f"Lesser than Equal to Operator: {5 <= 5}"); # Output: True

# Another example
print("Another Example");

a = 10;
b = 5;

print(a == b); # Output: False
print(a != b); # Output: True
print(a > b); # output: True
print(a < b); # Output: False

# 4. Boolean Operators

# OR gate: 
"""
Input 1  Input 2     Result
True     True         True
False    True         True
True     False        True
False    False        False
"""
# python: or keyword , Java: ||

print(f"OR logic gate: {5 > 6 or 6 == 6}"); # Output: False or True , result is True.
print(f"OR logic gate: {4 > 3 or 4 != 5}"); # Output: True or True, result is True. 
# Any number of input is possible.
print(f"OR logic gate: {4 > 3 or 4 != 5 or 5 > 6 or 6 == 6}"); # Output: True or True or False or True, result is True. 

# AND gate
"""
Input 1    Input 2    Result
True       True       True
False      True       False
True       False      False
False      False      False
"""
# python: and keyword , Java: &&

print(f"AND Gate operator: {5 < 10 and 5 == 5}"); # Output: True and True , result is True.
print(f"AND Gate operator: {30 < 10 and 5 != 5}"); # Output: False and False , result is False.

# NOT gate
"""
Input      Output
True      False
False     True
"""
# python: not keyword , Java: !
print(f"NOT Boolean operator: {5 == 5}"); # Output: True
print(f"NOT Boolean operator: {not(5 == 5)}"); # Output: False

# Falsy values: What all values are considered as False.
# Boolean: False
# String: Empty string : ''
# Integer: 0
# Float: 0.0
# Python list: Empty list [], empty tuple (), empty set(), empty dict {}.
# Anything empty is considered False.

print("Falsy Values");

print(0 or 1) # 1 , 0 is considered False
print(0 and 1) # 1 , 0 is considered False,0

print(False or 'hey') # 'hey' , because of False boolean
print(False and 'hey') # False

# String booleans
# Condition for OR: or used in an expression returns the value of the first operand that is not a falsy value ( False , 0 , '' , [] ..). Otherwise it returns the last operand.
# The Python docs describe it as if x is false, then y, else x .

print('hi' or 'hey') # 'hi', first value both are True because they are not empty strings.
print('hi' or 'hey' or 'tins') # 'hi', All three are Tue then first string is returned.
print([] or False) # False, Empty list is False
print(False or []) # []

# Condition for AND: and only evaluates the second argument if the first one is true. 
# So if the first argument is falsy ( False , 0 , '' , [] ..), it returns that argument.
# Otherwise it evaluates the second argument and so on.
# The Python docs describe it as if x is false, then x, else y .

print('hi' and 'hey') # 'hey'
print(0 and 'hi' and 'hey') # 0

print('hi' and 'hey' and 'tins' and 'i') # 'i', not word length.
print('hi' and 'hey' and 'tins' and 0.0 and 'i') # 0.0
print([] and False) # [], Empty list is False

# 5. Bitwise Operators
# Bitwise operators are rarely used so not explaining.

# 6. is and in Operator.

# in operator: Check if something is avaliable. Also known as membership operator.
# String.
name = "Vincent";
print(f"In operator: {'n' in name}"); # Output: True
print(f"In operator: {'a' in name}"); # Output: False

# Python - list or Arrays.
student_info = ["Vincent", 12, 'doctor', 4]
print(f"In Operator: Student Info {'n' in student_info}"); # Output: False
print(f"In Operator: Student Info {'doctor' in student_info}"); # Output: True
print(f"In Operator: Student Info {4 in student_info}"); # Output: True
print(f"In Operator: Student Info {3 in student_info}"); # Output: False

# Python - dictionary
student_info = {
    "name" : "Vincent",
    "age" : 12,
    "profession": "doctor"
}
# If you passs the dic directly then it will consider dictionary keys.
print(f"In Operator - Dict Example: {'name' in student_info}"); # Output: True
print(f"In Operator - Dict Example: {'Vincent' in student_info}"); # Output: False
# If you v=want to check in dict values.
print(student_info.values());
print(f"In Operator - Dict Example: {'Vincent' in student_info.values()}"); # Output: True


# is operator. Also known as identity operator. 
# It is used to compare two objects and returns true if both are the same object.

tv_shows = ["Big boss","Cook with Comali","Super Singer"] # id: Array object
print(id(tv_shows))
a = tv_shows 
print(id(a))

print(tv_shows is a)# Output: True , because both objects are same.

u = ["x", "y", "z"]
v = ["x", "y", "z"]
w = ["x", "y", "a"]
x = ["X", "y", "z"]
#  Note: Case Sensitive.
print("u, v, and w example");
print(u is w); # Output: False
print(u is x); # Output: False

# Note: Test two objects that are equal, but not the same object.
print(id(u));
print(id(v));
print(u is v); # Output: False

# Note: Check if two objects are the same object.
v = u;
print(id(u));
print(id(v));
print(u is v); # Output: True

# Reference: https://www.w3schools.com/python/ref_keyword_is.asp

# 7. Ternary Operator

# function is a reusable code.
# Without ternary operator.
def age_identifier(age):
    if age >= 18:
        return "The person is an adult."
    else:
        return "The person is young."
    
# With Ternary operator. (Short form)
# Format: <result_if_true> if <condition> else <result_if_false>

def age_identifier(age):
    return "The person is an adult." if age >= 18 else "The person is young."

print(age_identifier(16)); #  Output: "The person is young."
print(age_identifier(21)); #  Output: "The person is an adult."

# Another function example.
def tax_calculator(salary):
    tax_amount = (salary / 100) * 10 
    return "High tax" if tax_amount >= 10000 else "Low Tax"

print(tax_calculator(100000))# output: High tax
print(tax_calculator(90000))# output: Low tax

# Another function example.
def fever_estimator(temperature):
    return "High Fever" if temperature >= 99.9 else "Normal temperature."

print(fever_estimator(98.9)); # Output: Normal temperature.
print(fever_estimator(101)); # Output: High Fever

