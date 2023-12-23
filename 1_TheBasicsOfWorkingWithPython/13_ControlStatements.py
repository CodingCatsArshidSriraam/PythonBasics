# Problem: Adult Visa verification.
# verification 1: 18 yrs less ---> not eligible, 18 to 55 ---> Long Stay Visa, Above 55 ----> Tourist Visa
# Verification 2: Vaccinated: Yes -----> Eligible , No -----> Not eligible.
# Inputs: age, is_vaccinated_status
# output: "visa_status": True

def adult_visa_verification(age,is_vaccinated):
    if age < 18:
        return {"visa_status":False, "message":f"Not eligible for Age {age}"}
    
    elif age > 18 and age < 56 :
        if is_vaccinated:
            return {"visa_status":True, "message":f"Eligible for Age {age} and vaccination status {is_vaccinated}"}

        else:
            return {"visa_status":False, "message":f"Not eligible for Age {age} and vaccination status {is_vaccinated}"}

    else:
        if is_vaccinated:
            return {"visa_status":True, "message":f"Eligible for Age {age} and vaccination status {is_vaccinated}"}

        else:
            return {"visa_status":False, "message":f"Not eligible for Age {age} and vaccination status {is_vaccinated}"}

    
# Function calls
print(adult_visa_verification(11,True))
print(adult_visa_verification(19,True))
print(adult_visa_verification(51,False))
print(adult_visa_verification(59,True))
print(adult_visa_verification(59,False))

# Important points:
# Point 1: We can make decisions and take different roads depending on True or False values (Booleans). We can use if , elif and else statements to make decisions in Python.
# Point 2: Block: Belongs to a condition which is indented to that condition and is exectued if it is True.
# Point 3: Another definition of block: A block is that part that is indented one level (4 spaces usually) on the right:


# Inline format
# if and else can also be used in an inline format, which lets us return a value or another based on a condition.

def gender_pronoun(gender):
    return "Mrs" if gender == "female" else "Mr"

gender = input("Enter the gender:")

print(gender_pronoun(gender))


# Reverse a list problem

origin_list_odd = [1,2,3,4,5] # Output: [5,4,3,2,1]
origin_list_even = [1,2,3,4,5,6] # Output: [6,5,4,3,2,1]
origin_list_miscellanous = [5,2,3,7,8,9] # Output: [9,8,7,3,2,5]

def reverse_list_two_pointer(input_list):
    left = 0 # first index
    right = len(input_list) - 1 # last index

    while left < right:
        left_value = input_list[right] 
        right_value = input_list[left]
        input_list[left] = left_value
        input_list[right] = right_value
        # Short form: Packing, Unpacking input_list[left],input_list[right] = input_list[right],input_list[left]

        left += 1 # left = left + 1
        right -= 1 # right = right -1 

    return input_list

print(reverse_list_two_pointer(origin_list_odd))
print(reverse_list_two_pointer(origin_list_even))
print(reverse_list_two_pointer(origin_list_miscellanous))

