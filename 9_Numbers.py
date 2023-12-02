# Three types.

# Type 1: int
print("Integer numbers / Whole numbers")

# Method 1: Directly assign.
score = 10
# Method 2: int() constructor
score = int(9)

# To know type.
print(type(score)) # <class 'int'>
print(isinstance(score,int)) # True

# Type 2: float
print("Float point numbers / Decimal numbers")

# Method 1: Directly assign.
pi = 3.141
# Method 2: float() constructor
pi = float(3.141)

# To know type.
print(type(pi)) # <class 'float'>
print(isinstance(pi,int)) # False
print(isinstance(pi,float)) # True

# type 3: complex
print("Complex numbers.")

# Method 1: Directly assign.
string_function = 3 + 9j
print(string_function)
print(string_function.real)
print(string_function.imag)

# Method 2: complex() constructor.
string_function = complex(3 , 9)
print(string_function)
print(string_function.real)
print(string_function.imag)

# To know the type or instance.
print(type(string_function)) # <class 'complex'>
print(isinstance(string_function,complex)) # True

# Arithmetic operations on numbers.
# Addition
print(f"Addition: {1 + 1}") #2
# Subtraction
print(f"Subtraction: {2 - 1}") #1
# Multiplication
print(f"Multiplication: {2 * 2}") #4
# Division
print(f"Divison: {4 / 2}") #2
# Remainder or Modulus
print(f"Modulus: {4 % 3}") #1
# Exponentiation
print(f"Exponentiation or Power: {4 ** 2}") #16
# Floor Divison
print(f"Floor Division: {4 // 2}") #2


# Compound assignment operators , rewriting the variable so it changes.
print("Compound assignment operators")
score = 9
score += 1 # score = score + 1
print(score) # 10
score -= 1 # score = score - 1
print(score) # 9
score *= 2 # score = score * 2
print(score) # 18

"""
Other examples:
/=
%=
..and so on
"""

# numbers built in functions.

# function 1: abs() returns the absolute value of a number
print("abs() function.")
score = 9.7
print(abs(score)) # 9.7 , positive gives positive.
score = - 9.7
print(abs(score)) # 9.7 , negative gives positive.

# function 2: given a number, returns its value rounded to the nearest integer.
print("round() function")
pi = 3.717
print(round(pi)) # 4
pi = 3.417
print(round(pi)) # 3
pi = 3.512
print(round(pi)) # 4

# We can control the precision, second parameter to set the decimal points precision.
# The below examples should be controlled to the second decimal.
pi = 3.717
print(round(pi,2)) # 3.72
pi = 3.417
print(round(pi,2)) # 3.42
pi = 3.512
print(round(pi,2)) # 3.51

"""
Notes:
the math package provides general math functions and constants
the cmath package provides utilities to work with complex numbers.
the decimal package provides utilities to work with decimals and
floating point numbers.
the fractions package provides utilities to work with rational numbers

"""
# Undersatnding Constructor.
score = int(9)
class Integer:
    def __init__(self,value) -> None:
        self.value = value
    
    def print_value(self):
        print(self.value)

integer_1 = Integer(7)
integer_1.print_value()