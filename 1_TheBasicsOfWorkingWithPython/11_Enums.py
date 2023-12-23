# Import enum.
from enum import Enum

# Weekday class created by inheriting Enum.
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Example usage of the Weekday enum
current_day = Weekday.SATURDAY

# Print the enum member (will print Weekday.WEDNESDAY)
print(f"Today is {current_day}") # Weekday.SATURDAY

# Access the value using the .value attribute
print(f"Numeric representation: {current_day.value}")  # Output: 6

# Access the enum member using the value (reverse lookup)
new_day = Weekday(6)
print(f"Corresponding day for value 6: {new_day}")  # Output: Weekday.SATURDAY

# Access the enum member using square bracket notation
another_day = Weekday['SATURDAY']
print(f"Corresponding value for SATURDAY: {another_day.value}")  # Output: 6

# List all possible values of the enum
all_days = list(Weekday)
print(f"All days of the week: {all_days}")

# Count the number of enum members
num_days = len(Weekday)
print(f"Number of days in the week: {num_days}")
