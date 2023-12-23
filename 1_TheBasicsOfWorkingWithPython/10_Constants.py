# Python has no way to enforce a variable to be a constant.

# Way 1: We can use all capital letters. It will tell the programmer that it ia constant.
# It will allow it to rewrite the constant.

PI = 3.14
print(PI)
PI = 3.15
print(PI)

# Way 2: Inherit Enum class.

from enum import Enum

class MyExperimentVariables(Enum):
    CHEMISTRY_VARIABLE_1 = 3.0
    CHEMISTRY_VARIABLE_2 = 6.0
    CHEMISTRY_VARIABLE_3 = 9.0

print(MyExperimentVariables.CHEMISTRY_VARIABLE_1.value)
print(MyExperimentVariables.CHEMISTRY_VARIABLE_2.value)
print(MyExperimentVariables.CHEMISTRY_VARIABLE_3.value)

print(list(MyExperimentVariables))

# Cant reassign will throw an error. 
# Error : AttributeError: <enum 'Enum'> cannot set attribute 'value'
# MyExperimentVariables.CHEMISTRY_VARIABLE_3.value = 7 # This is not possible.
