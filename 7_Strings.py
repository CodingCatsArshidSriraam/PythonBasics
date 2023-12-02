# A string in Python is a series of characters enclosed in single quotes or double quotes.
# We can assign a string to a variable.

subject = "python";
print(subject);
print(type(subject)); # output: <class 'str'>

# Concatenate two strings using the + operator.
print("Hello" + " " + "World"); # output: Hello World

# Appending to a string is possible.
subject += " is an easy subject." # subject = subject + " is a easy subject."
print(subject) # output: python is a easy subject.

#  Convert a number to a string using the str class constructor.
# print("My age is " + 28); # Output: TypeError: can only concatenate str (not "int") to str
print("My age is " + str(28)); # We can use data type conversion or casting. Output: My age is 28

# Multi line strings.

message = """
Hi Everyone,
I welcome you to this course.
Have a great day......
""";
print(message);


message = "Hi Everyone,\nI welcome you to this course. \nHave a great day......\n";
print(message);

# Built in methods.

# Important Note: None of those methods alter the original string. They return a new, modified string instead.
tv_show = "Big Boss";

print(tv_show.lower()); # Output: "big boss" , these methods will not alter the original string.
print(tv_show); # Output: "Big Boss", original string will not change.

# If you want to change the original string.
tv_show = tv_show.lower();
print(tv_show); # Output: big boss

# String function 1: isalpha() to check if a string contains only characters and is not empty
print("isalpha string function.")
string_1_1 = "hello";
string_1_2 = "";
string_1_3 = "sriram178909"
print(string_1_1.isalpha()) # True
print(string_1_2.isalpha()) # False
print(string_1_3.isalpha()) # False

# String function 2: isalnum() to check if a string contains characters or digits and is not empty.
print("isalnum string function.")
string_1_1 = "hello";
string_1_2 = "";
string_1_3 = "sriram178909"
print(string_1_1.isalnum()) # True
print(string_1_2.isalnum()) # False
print(string_1_3.isalnum()) # True

# String function 3: isdecimal() to check if a string contains digits and is not empty.
print("isdecimal string function.")
string_1_1 = "hello";
string_1_2 = "";
string_1_3 = "sriram178909"
string_1_4 = "988890"
print(string_1_1.isdecimal()) # False, because it should have only digits.
print(string_1_2.isdecimal()) # False, because empty string.
print(string_1_3.isdecimal()) # False, because it contains also alphabets along with the digits.
print(string_1_4.isdecimal())  # true, because it contains only digits.

# String function 4: lower() to get a lowercase version of a string
print("String function: lower");
string_1_1 = "JiMin"
print(string_1_1.lower()); # Output: jimin

# String function 5: islower() to check if a string is lowercase
print("String function: islower()");
string_1_1 = "JiMin"
print(string_1_1.islower()); # Output: False, because of capital letters J and M.
print(string_1_1.lower().islower()) # Output: True, because we changed it to lowercase and then we are checking.

# String function 6:
#  upper() to get an uppercase version of a string
print("String function: upper() and isupper()");
string_1_1 = "JiMin"
print(string_1_1.upper()); # Output: JIMIN
#  isupper() to check if a string is uppercase
print(string_1_1.isupper()); # Output: False, because it contains lower case characters.

# String function 7: title() to get a capitalized version of a string
# Starting letter of every word is Capital.
print("String function: title()");
movie_name = "ponniyin selvan 2";
print(movie_name.title()); # Output: Ponniyin Selvan 2

# String function 8: startsswith() to check if the string starts with a specific substring
print("String function: startswith()");
movie_name = "ponniyin selvan 2";
print(movie_name.startswith("po")); # Output: True
print(movie_name.startswith("ponn")); # Output: True
print(movie_name.startswith("poni")); # Output: False

# String function 9: endswith() to check if the string ends with a specific substring
print("String function: endswith()");
movie_name = "ponniyin selvan 2";
print(movie_name.endswith("2")); # Output: True
print(movie_name.endswith("n 2")); # Output: True
print(movie_name.endswith("n")); # Output: False

# String function 10: replace() to replace a part of a string
print("String function: replace()");
movie_name = "ponniyin selvan 2";
print(movie_name.replace('p' , 'z')); # Output: zonniyin selvan 2
print(movie_name);# Original string is not modified.

# String function 11: split() to split a string on a specific character separator.
print("String function: split()");
movie_name = "ponniyin selvan 2";
name_split = movie_name.split(" "); 
print(movie_name.split(" "));
print(name_split); # ['ponniyin', 'selvan', '2']
print(movie_name); # Original string will not be modified. Output: ponniyin selvan 2

# String function 12: strip() to trim the whitespace from a string
# Note: Remove spaces at the beginning and at the end of the string:
print("String function: strip()")
movie_name = "ponniyin selvan 2";
print(movie_name.strip()); # Output: ponniyin selvan 2 , spaces in between are not remove only athe begining and end of the word it is removed.
movie_name = "   ponniyin selvan 2 ";
print(movie_name.strip());  # output: ponniyin selvan 2
# Use case: Data cleaning, NLP - Natural Language Processing

# String Function 13: join() to append new letters to a string
print("String function: join()");
movie_name_array = ['ponniyin', 'selvan', '2'];
movie_name = "**".join(movie_name_array); 
print(movie_name); # output: ponniyin**selvan**2
movie_name = " ".join(movie_name_array);
print(movie_name); # output: ponniyin selvan 2

# String Function 14: find() to find the position of a 
# Refrence: https://www.w3schools.com/python/ref_string_find.asp
movie_name = "Aayirathil Oruvan";
# Note: Case sensitive first occurence.
print(movie_name.find("a"));  # Output: 1
print(movie_name.find("o"));  # Output: -1 , Not found.
print(movie_name.find("O"));  # Output: 11

# Global Functions
# len()
print("Global functions: len()")
movie_name = "Aayirathil Oruvan";
print(len(movie_name));

# in operator
# The in operator lets you check if a string contains a substring.
print("In operator:")
country = "south korea"
print("s" in country) # True
print("si" in country) # False
print(" ko" in country) # True
print("korea" in country) # True
print("Korea".lower() in country.lower()) # True 

# Add special charcters to a string.
# Escaping is a way to add special characters into a string.
# name = "Kim Yoon"s son" # Wd cant use double quotes inside double quotes in Python. - Error
# Way 1: Backslash
name = "Kom Yoon\"s son"
print(name)
name = 'Kom Yoon\'s son'
print(name)
# Way 2 : Single quotes inside double qutes , double quotes inside single quotes.
name = "Kim Yoon's son"
print(name)
name = 'Kim Yoon"s son'
print(name)

# special formatting characters
print("special formatting characters")
#\t for tab
print("Yuun\t34\tmale")

#  \n for new line 
print("Welcome to the ATM\nPlease enter your pin number")

# \\ for the backslash, If you want to use backslash in the string.
print("6\\3") # 1 blackslash - give 2 backslash
print("6\\\\3") # 2 blackslashes - give 4 backslashes

print("6\\\3") # Heart

# Indexing
print("Indexing")
# String is indexed like an array or Python list.
# Using square brackets.
# Positive indexing starts from zero (First item).
# Negative indexing starts from last item which is -1.
country = "United States of America"
print(country[0]) # U, Space is also a character.
# Start index , Stop index, Step index
print(country[0:6]) # united
print(country[0:6:1]) # United
print(country[0:6:2]) # Uie
# Start index is not mentioned then the default is zero.
# Stop index it will to the last character of the string.
# Step index is not mentioned then the default is 1.
print(country[:6])# United
print(country[0:]) # United States of America
print(country[0:6]) # united
print(country[:]) # United States of America
print(country) # United States of America
# Last character or Last item , Stack.
print(country[-1]) # a , last character


