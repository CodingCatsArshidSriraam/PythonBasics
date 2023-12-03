# List is an essential data structure (array).

# Characteristics of list.
# It allows you to group together multiple values and reference them all with a common name.
# Easiest way to create a list is to use square brackets.
print('It allows you to group together multiple values and reference them all with a common name.')
stationary_items = ['pencil','pen','notebook','sticky notes']
print(stationary_items) # ['pencil', 'pen', 'notebook', 'sticky notes']
print(type(stationary_items)) # <class 'list'>

# Python lists are designed to hold values of different types (str, int, bool, float, list, tuple, dict, set and so on.)
print('Python lists are designed to hold values of different types (str, int, bool, float, list, tuple, dict, set and so on.)')
mixed_list = [1, 'hello', 3.14, True, [5, 6, 7], {'key': 'value'}, (8, 9), set([10, 11])]
print(mixed_list[0])       # Output: 1 , int 
print(mixed_list[1])       # Output: 'hello' , str
print(mixed_list[2])       # Output: 3.14 , float
print(mixed_list[3])       # Output: True , bool
print(mixed_list[4])       # Output: [5, 6, 7] , list
print(mixed_list[5])       # Output: {'key': 'value'} , dict
print(mixed_list[6])       # Output: (8, 9) , tuple
print(mixed_list[7])       # Output: {10, 11} , set

# in operator in Python lists. You can check if an item is contained into a list with the in operator.
print('in operator in Python lists. You can check if an item is contained into a list with the in operator')
print(3.14 in mixed_list) # True
print('pen' in stationary_items) # True
print(False in mixed_list) # False
print([5,6,7] in mixed_list) # True
print([5,6,8] in mixed_list) # False

# Empty list: A list can also be defined as empty and it has the corresponding boolean to be false.
print('Empty list: A list can also be defined as empty and it has the corresponding boolean to be false.')
empty_list = []
print(empty_list)
print(type(empty_list))
print(True if not empty_list else False)

# Referencing (Read) You can reference the items in a list by their index, starting from zero. (Positive index)
print('Referencing (Read) You can reference the items in a list by their index, starting from zero. (Positive index)')
mixed_list = [9, 'hello', 3.14, True, [5, 6, 7], {'key': 'value'}, (8, 9), set([10, 11])]
print(mixed_list[0])       # Output: 9 , int 
print(mixed_list[1])       # Output: 'hello' , str
print(mixed_list[2])       # Output: 3.14 , float
print(mixed_list[3])       # Output: True , bool
print(mixed_list[4])       # Output: [5, 6, 7] , list
print(mixed_list[5])       # Output: {'key': 'value'} , dict
print(mixed_list[6])       # Output: (8, 9) , tuple
print(mixed_list[7])       # Output: {10, 11} , set

# Updating (changing) the value in a Python list.
print('Updating (changing) the value in a Python list.')
music_bands = ['bts','black pink','xo','stray kids']
print(music_bands)

# Method 1: Using square notations.
print('Square notations')
music_bands[2] = 'new jeans'
print(music_bands)

# Method 2: Using index() method.
print('index() method.')
print(music_bands.index('stray kids'))
music_bands[music_bands.index('stray kids')] = 'exo'
print(music_bands)

# Method 3: Negative Index.
print('Negative Index.')
# Note: To get the last items or stacks or itterate in reverse.
print(music_bands[-1]) # return the last item.  Output: 'exo'
print(music_bands[-2]) # return the second last item. Output: 'new jeans'

# Method 4: Slicing in lists.
print('Slicing in lists.')
# format: list_name[start index : stop index : step index]
print(music_bands[0:2]) 
# If I dont mention the start index the default is 0.
print(music_bands[:3]) 
# If I dont mention the stop index the default is length of the list - 1.
print(music_bands[0:]) 
# If I dont metion the step index the default is 1.
# Commonlu=y used to reverse.
print(music_bands[::-1]) 

# To get the length of the Python list. len() method.
print('To get the length of the Python list. len() method.')
print(len(music_bands))

# append() - Add item at the end of the list.
print('append() - Add item at the end of the list.')
print(music_bands)
music_bands.append('sia')
print(music_bands)

# Special case if you are append list tuple , dict.
music_bands.append(['taylor swift', 'lady gaga'])
print(music_bands)
print(music_bands[5])
print(music_bands[5][1])
music_bands.append(('beyonce','iu'))
print(music_bands)
print(music_bands[6])
print(music_bands[6][0])
# Note: Appending sets are little bit complicated.
music_bands.append({'name': 'Miley Cyrus', 'genre': 'Pop'})
print(music_bands)
print(music_bands[7])
print(music_bands[7]['name'])
print(music_bands[7]['genre'])

# extend() Add items to the end of the list , individually adds the items.
print('extend() Add items to the end of the list , individually adds the items.')
music_bands = ['bts','black pink','xo','stray kids']

print(music_bands)
music_bands.extend('sia')
# Strings characters are individually added when we use extend.
print(music_bands)
print(music_bands[4] + music_bands[5] + music_bands[6]) # Output: Sia

# Special case if you are append list tuple , dict.
music_bands.extend(['taylor swift', 'lady gaga'])
print(music_bands)
print(music_bands[7])
print(music_bands[8])

music_bands.extend(('beyonce','iu'))
print(music_bands)
print(music_bands[9])
print(music_bands[10])

# # Note: Extending sets are little bit complicated.
music_dict = {'name': 'Miley Cyrus', 'genre': 'Pop'}
music_bands.extend(music_dict.values())
print(music_bands)
print(music_bands[11])

# Important Note:
"""
with extend() or += don't forget the square brackets. Don't do
items += "Test" or items.extend("Test") or Python will add 4
individual characters to the list, resulting in ['Roger', 1, 'Syd', True,
'T', 'e', 's', 't']
"""
print(music_bands)
music_bands.extend(['sia'])
print(music_bands)
print(music_bands[-1])

# Similar to extend we can use urnary operator.
music_bands += ['ar rahman']
print(music_bands)
print(music_bands[-1])

# Deleting items from the Python lists.
print('Deleting items from the Python lists.')

# Method 1: pop() - Removes the last item and return sit.
print(music_bands)
print(music_bands.pop())
print(music_bands)

# Method 2: Remove the value from the list, if there are duplicates removes the first in the list.
music_bands += ['kr','sia']
print(music_bands)
music_bands.remove('sia') #Note: If there are duplicates it removes the first found value.
print(music_bands)

# Extend VS urnary operator
music_bands += ['ar rahman', 'ar rahman'] # Similar to extend , Code : music_bands.extend(['ar rahman', 'ar rahman'])
print(music_bands)
print(music_bands[-1])

# insert() : Used to add at a specific index.
subjects = ['physics','chemistry','biology']
print(subjects)
subjects.insert(1,'mathematics') # Parameter 1: index, Parameter 2: value
print(subjects)
subjects.insert(4,'geography')
print(subjects)
subjects.insert(len(subjects),'english') # len(subjects) = last_index + 1
print(subjects)
# Note: Works for only positive index , -1 is not working. Negative index does not give i=us the proper behaviour,

# Slicing - To insert items in between the Python lists.
print('Slicing - To insert items in between the Python lists.')
print(subjects)
subjects[3:3] = ['tamil','french']
print(subjects)

print('Sort')
# sort() vs sorted() global function.
# Sort() is a list method that alters the original list so we have to copy it before perfoeming sort.
# Note: If you want to alter the original list use sort() list method.
numbers = [4,1,3,2,1]
print(numbers)
numbers.sort()
print(numbers) # Original list will be modified when we use sort() list method.

# Note: If you dont want to alter the original list use sorted() global function.
# sorted() is a global function that creates a snap of the original list and does not alter the original list.
numbers = [4,1,3,2,1]
print(numbers)
print(sorted(numbers))
print(numbers) # Original list will not be modified when we use sorted() global function.

# Sort only strings or integers , we cant sort combinations.
# We can sort a list containing only integers.
numbers = [4,1,3,2,1]
numbers.sort()
print(numbers)

# We can sort strings, remomeber to change it to lower case because the sort() methods orders uppercase letters first, then lowercased letters
vijay_movies = ['leo','gilli','master','Pulli']
print(vijay_movies)
vijay_movies.sort()
print(vijay_movies) # uppercase first in alphabetical order then lower case in alphabetical order.

# If you want to emphasize only alphabetical order.
vijay_movies.sort(key=str.lower) # similar to vijay_movies.lower.sort()
print(vijay_movies)

# Copy lists.
print("Copying lists.")

# Method 1: Slicing
vijay_movies_copy = vijay_movies[:]
print(vijay_movies_copy)# If you alter the copy the original list will not be altered.

# Method 2: copy() method.
vijay_movies_copy = vijay_movies.copy()
print(vijay_movies_copy)# If you alter the copy the original list will not be altered.