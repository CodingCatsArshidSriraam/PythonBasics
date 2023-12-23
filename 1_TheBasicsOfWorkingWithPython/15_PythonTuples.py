# There is only one difference between Python Lists and Python Tuples.
# Python tuples are immutable: Not changeable/ modifiable after the ceation of the tuple.

# They allow you to create immutable groups of objects. This means that once a
# tuple is created, it can't be modified. You can't add or remove items.

# Craeting tuples: They are created in a way similar to lists, but using parentheses instead of square brackets.
# Unchangeable information.
# Example: Coordinates of famou monumnets.

# Coordinates of Famous Monuments
eiffel_tower_coordinates = (48.858844, 2.294350)  # Eiffel Tower, Paris, France
taj_mahal_coordinates = (27.1751, 78.0421)        # Taj Mahal, Agra, India
statue_of_liberty_coordinates = (40.689247, -74.044502)  # Statue of Liberty, New York City, USA
colosseum_coordinates = (41.8902, 12.4924)         # Colosseum, Rome, Italy
sydney_opera_house_coordinates = (-33.8568, 151.2153)  # Sydney Opera House, Sydney, Australia

# Accessing individual coordinates
print("Eiffel Tower Coordinates:", eiffel_tower_coordinates)
print("Taj Mahal Coordinates:", taj_mahal_coordinates)
print("Statue of Liberty Coordinates:", statue_of_liberty_coordinates)
print("Colosseum Coordinates:", colosseum_coordinates)
print("Sydney Opera House Coordinates:", sydney_opera_house_coordinates)


# Type individual coordinates
print("Eiffel Tower Coordinates:", type(eiffel_tower_coordinates)) # <class 'tuple'>

# creating famous mnumets tuple.
coordinates_famous_monuments = (
{
    "monument_name":"eiffel_tower",
    "monument_coordinates": (48.858844, 2.294350) 
},
{
    "monument_name":"taj_mahal",
    "monument_coordinates": (27.1751, 78.0421)   
},
{
    "monument_name":"statue_of_liberty",
    "monument_coordinates": (40.689247, -74.044502),
},
{
    "monument_name":"colosseum",
    "monument_coordinates": (41.8902, 12.4924),
},
{
    "monument_name":"sydney_opera_house",
    "monument_coordinates": (-33.8568, 151.2153),
}
)

# Property of Tuple.
# Tuple has an index and it is ordered from 0.

# Function to display the coordinates based on user selection.
def coordinate_finder_famous_monuments(coordinates_famous_monuments):
    # Display menu for user selection
    print("Select a monument:")
    for index in range(len(coordinates_famous_monuments)):
        print(f"{index}. {coordinates_famous_monuments[index]['monument_name']}")
    # Get user input for monument selection
    selected_index = int(input("Enter the number of the monument you want to select: ")) 

    # Retrieve selected monument coordinates
    selected_monument = coordinates_famous_monuments[selected_index]
    selected_coordinates = selected_monument["monument_coordinates"]

    # Display selected monument coordinates
    print(f"Coordinates of {selected_monument['monument_name']} are: {selected_coordinates}")

# Calling the famous monuments function.
coordinate_finder_famous_monuments(coordinates_famous_monuments)

# Start with 1 instead of 0 for user interactivity.
# Function to display the coordinates based on user selection.
def coordinate_finder_famous_monuments(coordinates_famous_monuments):
    # Display menu for user selection
    print("Select a monument:")
    for index in range(len(coordinates_famous_monuments)):
        print(f"{index + 1}. {coordinates_famous_monuments[index]['monument_name']}")
    # Get user input for monument selection
    selected_index = int(input("Enter the number of the monument you want to select: ")) - 1

    # Retrieve selected monument coordinates
    selected_monument = coordinates_famous_monuments[selected_index]
    selected_coordinates = selected_monument["monument_coordinates"]

    # Display selected monument coordinates
    print(f"Coordinates of {selected_monument['monument_name']} are: {selected_coordinates}")


# Calling the famous monuments function.
coordinate_finder_famous_monuments(coordinates_famous_monuments)

# Function to calculate the revenue.
sales_data = [
    ("vicco", 10, 20.0),
    ("pepsodent", 5, 25.5),
    ("colgate", 8, 15.0),
]

def calculate_total_revenue(sales_data):
    sum = 0
    for index in range(len(sales_data)):
        sum += sales_data[index][1] * sales_data[index][2]
    return sum

total_revenue = calculate_total_revenue(sales_data)
print("Total Revenue:", total_revenue)

#  index() method in a python tuple.
hr_names = ("tera",'shin','trek')
print(hr_names.index('trek'))
# print(hr_names.index('tek')) # If value not present: ValueError: tuple.index(x): x not in tuple

# As with strings and lists, using a negative index will start searching from the end.
print(hr_names[-1])
print(hr_names[-2])
print(hr_names[-3])

# You can count the items in a tuple with the len() function.
print(len(hr_names)) # Output: 3

# You can check if an item is contained into a tuple with the in operator.
print('tera' in hr_names) # Output: True
print('vn' in hr_names) # Output: False

# Slicing: You can also extract a part of a tuple, using slices:
print(hr_names[:1]) # Output: ("tera") because default start index is 0, stop index is 1.
print(hr_names[1:]) # Output: ('shin','trek') because default value of the stop index is the last index.

# You can create a sorted version of a tuple using the sorted() global function.
print(sorted(hr_names))

# You can create a new tuple from existing tuples using the + operator:
hr_updated_names = hr_names +  ("Vanille", "Tina")
print(hr_updated_names)
print(type(hr_updated_names))

