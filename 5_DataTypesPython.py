# Basic Data types.
# Data Type 1: String.
favourite_tv_show = 'Big Boss'; # We represent strings with single quotes or double quotes.
print(id(favourite_tv_show));
print(favourite_tv_show);

# We can check which type a variable is using type function.
print(type(favourite_tv_show));

# Validate a variable datatype.
# Method 1: type() function
print(type(favourite_tv_show)== str);
# Method 2: .isinstance.
# In Python all are objects.
print(isinstance(favourite_tv_show,str));

# Same with int.
age = 20;
print(type(age) == int);

# Same with float as well.
temperature = 98.9;
print(type(temperature) == float);

# Dynamic typing:  Python automatically detects the type from the value type.
# Java: integer num = 10;
num = 10; # instead int num = 10 like in Java.



# Casting in Python.

# Create a string- Method 1.
message = 'Hi';
print(message);

# Create a string- Method 2. Casting ,class constructor way
message = str('Hey');
print(message);

# Casting
age = '23';
print(type(age));
print(type(int(age)));

# invalid 
# Error: ValueError: invalid literal for int() with base 10: '23a'
# age = '23a';
# print(type(age));
# print(type(int(age)));

age = '23';
experience = '5';
print(age + experience); # String concatenation of string will happen.
print(int(age) + int(experience)); # Casting is done now so the answer is an arithmetic calculation.

# Convert fraction to int. It ignores the decimal.
pi = 3.141;
print(int(pi));


# Data Type 2: Integer
# Whole numbers
positive_marks = 1;
print(f"Positive marks: {positive_marks}")
negative_marks = -2;
print(f"Negative marks: {negative_marks}")

# Data Type 3: float 
# Decimal numbers or Fractions.
percentage = 94.57;
print(f"Decimal number: {percentage}");

# Data Type 4: Boolean 
is_good = True # Other languages: true, True in Python.
print(f"True: {is_good}")
is_bad = False # Other language: true, False in Python.
print(f"False: {is_bad}")

"""
Advanced data types:

list for lists
tuple for tuples
range for ranges
dict for dictionaries
set for sets

"""