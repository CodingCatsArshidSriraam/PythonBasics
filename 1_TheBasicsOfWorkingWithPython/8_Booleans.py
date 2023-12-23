# Boolean Data type.

age = 25
is_age = True if age > 18 else False
print(is_age) # True

age = 16
is_age = True if age > 18 else False
print(is_age) # False

# Python Boolean Reserved keyword.: True, False ; Java : true, false

print(type(is_age)) # <class 'bool'>

print("Boolean Example")
# Mainly used in conditional statements.
def password_validator(input_password):
    lower_case_validation = input_password.islower()
    alpha_numeric_validation = input_password.isalnum()

    if lower_case_validation and alpha_numeric_validation:
        return "Password is Ok"
    else:
        return "Wrong password, password should contain only lower case and alpha numeric characters."
    
# Short form
def password_validator(input_password):
    if input_password.islower() and input_password.isalnum():
        return "Password is Ok"
    else:
        return "Wrong password, password should contain only lower case and alpha numeric characters."
    
print(password_validator("Seera123")) # " Wrong password, password should contain only lower case and alpha numeric characters."
print(password_validator("seera123")) # "Password is Ok"
print(password_validator("seera@#123")) # " Wrong password, password should contain only lower case and alpha numeric characters."

# If the data type is not bool there are certain rules to access a particular data type.

# Condition 1: Int and Float data type: 0 is considered False, all other numbers are considered True
print("Condition 1: 0 is considered False, all other numbers are considered True")

def machine_state_alert(input_current):
    if input_current:
        return True
    else:
        return False
    
print(machine_state_alert(0)) # False
print(machine_state_alert(9)) # True
print(machine_state_alert(-7)) # True
print(machine_state_alert(0.0)) # False
print(machine_state_alert(9.9)) # True

# Condition 2: String data type: False = If the string is empty.
print("Condition 2: String data type: False = If the string is empty.")

def user_password(password):
    if password:
        return "Password is not empty."
    else:
        return "Password is empty"
    
print(user_password("")) # "Password is empty"
print(user_password(" ")) # "Password is not empty.", because space is also a character.
print(user_password("seri122&&@###")) # # "Password is not empty."

# Condition 3: Lists, Tuples, Dicts, Sets Data Structures: False = Only when empty
print("Condition 3: Lists, Tuples, Dicts, Sets Data Structures: False = Only when empty")
empty_list = []
print(True if not empty_list else False) # true

empty_tuple = ()
print(True if not empty_tuple else False) # true

empty_set = set()
print(True if not empty_set else False) # true

empty_dict = {}
print(True if not empty_dict else False) # true

# To check if the data type is bool.
# Way 1: Using global type() - Polymorphism method.
is_expert_python = True
print(type(is_expert_python)) # <class 'bool'>

# Way 2:  using isinstance() 
print(isinstance(is_expert_python,bool)) # True
print(isinstance(is_expert_python,str)) # False

# all() function.
print("All function")
# It checks if all the elements are True.
physics_marks = [1,3,None,8,9,10,0] # 0 and None means amrk is not entered dproperly.

def marks_teacher_validator(mark_list):
    return all(mark_list)

print(marks_teacher_validator(physics_marks)) # False

physics_marks = [1,3,1,8,9,10,0] 
print(marks_teacher_validator(physics_marks)) # False, because of 0
physics_marks = [1,3,1,8,9,10,10] 
print(marks_teacher_validator(physics_marks)) # True

# any() function.
print("Any function")
# It checks for atleast one element to be True to return True.
def church_marriage_vaidator(church_marriage_vote_list):
    objection = any(church_marriage_vote_list)
    if objection:
        return "Someone has objected."
    else:
        return "All agree to the ceremony."

church_vote_list = [False,False,False,False,False]
print(church_marriage_vaidator(church_vote_list)) # "All agree to the ceremony."

church_vote_list = [False,False,True,False,False]
print(church_marriage_vaidator(church_vote_list)) # "Someone has objected."

