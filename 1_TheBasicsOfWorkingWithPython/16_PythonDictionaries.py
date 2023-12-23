# While lists allow you to create collections of values. 

student_details_1 = ['Leo',16,'Male','Single',123456789]
student_details_2 = ['Mia',16,'Female','Single',123456788]

# name - 0 , age - 1, gender - 2, marital_status -3 , social_security_number -4 

print(student_details_1[4])
print(student_details_2[4])

# Because we know the order the number of items in the list is the same and is of a particular order.

# Dictionaries allow you tocreate collections of key / value pairs. 
# Note: A dictionary can contain multiple key/value pairs:. All keys in a dictionary should be unique otherwise it might overwrite.

# Creating a dictionary.

student_details = {
   
                        1 : {
                            'name': 'Leo',
                            'age' : 18,
                            'gender': 'Male',
                            'marital_status' : 'Single',
                            'social_security_number' : 1234
                        },

                        2 : {
                            'name': 'Mia',
                            'age' : 16,
                            'gender': 'Female',
                            'marital_status' : 'Single',
                            'social_security_number' : 1235,
                            # 'name': 'Miso', # Will over write if you have duplicate keys only unique keys allowed.
                            # 'name' : 'Tina'# Will over write if you have duplicate keys only unique keys allowed.
                        }

}

# Acessing the dictionary.
print(student_details)
print(type(student_details))
# You can access individual key values using this notation. square notations []
print(student_details[1]['name'])
print(student_details[2]['age'])
print(student_details[2]['name'])

# Important note: The key can be any immutable value like a string, a number or a tuple. The value can be anything you want.

albums = {
    'album_name': 'Lady Gaga',
    1994 : 1,
    (1994,1996,1997):[True,False,True],
    1.4 : 'dollars',
    True: 'Yes'
}
print(f"The name of the album is {albums['album_name']} released times {albums[1994]} With each corresponding releases on 1994,1996 and 1997 are  {albums[(1994,1996,1997)]} with a revenue of 1.4 in {albums[1.4]}  and it is {albums[True]}")


# Update the dictionaries.

# Method 1: Using square notations.

print(student_details)
print(student_details[1]['age'])
student_details[1]['age'] = 19
print(student_details)
print(student_details[1]['age'])

# Method 2: Using get() dictionary method.
print(student_details)
print(student_details[2]['age'])

student_details.get(2)['age'] = 12
print(student_details)
print(student_details[2]['age'])

# Advantage of using get method if there is no key it will not throw error.
# print(student_details[3]) # It will throw key error.
print(student_details.get(3)) # If the key is not present it will return None.
# Default value is None othrwise it can be specified as the second parameter.
print(student_details.get(3,'The student id is not present in the database.')) 

# Deleting or removing from the dictionary.

# Method: pop()
# The pop() method retrieves the value of a key, and subsequently deletes the item from the dictionary.

cat_details = {
    'name': 'Tommy',
    'age' : 2,
    'color': 'White',
    'breed': 'Persian cat',
    'health_conditions': ['asthma','eye problems']
}

cat_details['age'] = 3

print(cat_details)

# Function to understand pop method.
def cat_cost(cat_details):
    breed = cat_details.pop('breed')
    if breed == 'Persian cat':
        cat_details['cost_cat'] = 100
    else:
        cat_details['cost_cat'] = None

cat_cost(cat_details)
print(cat_details)

# Method: popitem()
# The popitem() method retrieves and removes the last key/value pair inserted into the dictionary.
print(cat_details)
cat_details.popitem()
print(cat_details)

# In operator checking if somethng is present.
# You can check if a key is contained into a dictionary with the in operator.

print('name' in cat_details) # True - It will check only the key.
print('cost_cat' in cat_details) # False

print(cat_details.keys())
print('name' in cat_details.keys()) # True
# Get a list with the keys in a dictionary using the keys() method, passing its result to the list() constructor.
# To convert dictionary key to a list.
print(type(cat_details.keys())) # <class 'dict_keys'>
cat_keys = list(cat_details.keys())
print(cat_keys)
print(type(cat_keys))

# Get the values using the values() method, and the key/value pairs tuples using the items() method.
print(cat_details.values())
print('White' in cat_details.values()) # True

print(cat_details.items())

# Get a dictionary length using the len() global function, the same we used to get the length of a string or the items in a list.
# Method : len()
print(len(cat_details))

# You can add a new key/value pair to the dictionary in this way:
cat_details['cat_eye_color'] = 'green'
print(cat_details)

# You can remove a key/value pair from a dictionary using the del statement. pop() returns the item value but del does not return.
print(cat_details)
del cat_details['cat_eye_color']
print(cat_details)

# To copy a dictionary, use the copy() method:
# Incorrect way: cat_details_copy = cat_details
cat_details_copy = cat_details.copy()
cat_details_copy['copy_number'] = 1
print(cat_details)
print(cat_details_copy)



