
# Coding questions for interview.
"""
1. Reverse a List: Write a function to reverse a given list in-place, without using any built-in functions or creating a new list.

2. Find the Missing Number: Given a list of integers from 1 to n, with one number missing, write a function to find the missing number.

3. Merge Sorted Lists: Given two sorted lists, write a function to merge them into a single sorted list.

4. Remove Duplicates: Write a function to remove duplicates from a list while preserving the original order of elements.

5. Find the Second Largest Number: Write a function to find the second largest number in a list of integers.

6. Rotate List: Given a list and an integer k, write a function to rotate the list k times to the right.

7. Find Common Elements: Given two lists, write a function to find the common elements between them.

8. Largest Continuous Sum: Write a function to find the largest sum of contiguous subarray within a list of integers.

9. Find the Majority Element: Given a list of integers, write a function to find the majority element (an element that appears more than n/2 times).

10. Sort List of 0s, 1s, and 2s: Given a list containing only 0s, 1s, and 2s, write a function to sort the list in linear time.


"""

# Problem 1: 
# Reverse a List: Write a function to reverse a given list in-place, without using any built-in functions or creating a new list.
# Important note: Without using any built-in functions or creating a new list.

# Way 1: Approach by creating a new list. - Wrong approach
def reverse_list(input_list):
    return input_list[::-1]

#  The task is to reverse the list in-place, without using any built-in functions or creating a new list.
# Way 2: Two pointer approach.
def reverse_list_two_pointer(input_list):
    left = 0
    right = len(input_list) - 1

    while left < right:
        temp = input_list[left]
        input_list[left] = input_list[right]
        input_list[right] = temp

        left += 1
        right -= 1

    return input_list

# There is another concept in Python for swapping variables.
# This is a feature of Python called "tuple packing and unpacking." 
# It allows you to assign multiple values simultaneously.

# In this case, the values of input_list[left] and input_list[right] are packed into a tuple (input_list[right], input_list[left]). 
# Then, the tuple is unpacked and assigned back to input_list[left] and input_list[right], effectively swapping their values.

def reverse_list_two_pointer(input_list):
    left = 0
    right = len(input_list) - 1

    while left < right:
        input_list[left],input_list[right] = input_list[right],input_list[left]

        left += 1
        right -= 1

    return input_list

# Problem 2
# Find the Missing Number: Given a list of integers from 1 to n, with one number missing.
# write a function to find the missing number.
# Note: missing number in a sorted list of integers.

# Mathematical approach - Uses inbuilt function sum()
def find_missing_number(input_list):
    n = len(input_list) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(input_list)
    missing_number = total_sum - actual_sum
    return missing_number

# Short form
def find_missing_number(input_list):
    n = len(input_list) + 1
    return (n * (n + 1)) // 2 - sum(input_list)

# Two pointers aprroach - without sum()
# O(n) solution
def find_missing_number(input_list):
    left = 0
    right = len(input_list) - 1
    while left < right:
        if input_list[left] == left + 1:
            left +=1
        else:
            return left + 1
    # last number
    return right + 2

#  O(log n) time complexity, you can use a binary search approach.
def find_missing_number(input_list):
    left = 0
    right = len(input_list) - 1

    while left < right:
        mid = (left + right) // 2

        if input_list[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid

    return left + 1

# Problem 3:
# Merge Sorted Lists: Given two sorted lists, write a function to merge them into a single sorted list.

# The time complexity of the merge_sorted_lists function is O(n), where n is the total number of elements in both input lists.
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0 # Set pointers for list1 and list2
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append remaining elements from list1 or list2
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


# Notes:
# The line merged.extend(list1[i:]) in the merge_sorted_lists function will not throw an error even if the index i is out of bounds for list1.

# Problem 4
# Remove Duplicates: Write a function to remove duplicates from a list while preserving the original order of elements.

# Unordered way - Convert to aset and back to alist and sort.
# This way is not recommended because the oder of the list is not preserved.

def unordered_duplicates(input_list):
    return sorted(list(set(input_list)))

# Code should preserve the original order of elements while removing duplicates. 

# O(n) solution.
# So have as set seen and append accordingly.

def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for num in input_list:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
    return unique_list

# Notes
"""
Yes, in terms of time complexity:
O(n) is better than O(n log n) because it scales linearly with the size of the input, while O(n log n) grows faster as the input size increases.
For example, if you have an input of size 100, an O(n) algorithm will take 100 steps, while an O(n log n) algorithm will take about 200 steps. If you have an input of size 1000, an O(n) algorithm will take 1000 steps, while an O(n log n) algorithm will take about 3000 steps.
"""

# Problem 5
# Find the Second Largest Number: Write a function to find the second largest number in a list of integers.

def find_second_largest(unsorted_list):
    # Handle the condition if the len of the list is less than 2.
    if len(unsorted_list) < 2:
        return "List must have at least two elements"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for integer in unsorted_list:
        if integer > largest:
            second_largest = largest
            largest = integer
        elif integer > second_largest and integer != largest:
            second_largest = integer

    if second_largest == float('-inf'):
        return "There is no second largest number."
    
    return second_largest

# Notes:
"""
No, it's not possible to find the second-largest element in an unsorted list of integers in O(log(n)) time complexity. 
The best achievable time complexity for this problem is O(n) because you need to examine each element in the list at least once to determine the second-largest element, which requires a linear scan of the list.
"""

"""
If it is sorted:
There is no way to avoid this linear scan unless the list is already sorted, in which case you could use a binary search algorithm to find the second-largest element in O(log(n)) time.
"""

# Problem 6
# Rotate List: Given a list and an integer k, write a function to rotate the list k times to the right.
# of O(k * n), where 'n' is the length of the list.
def rotate_list(list_given , k):
    while k > 0:
        list_given.insert(0,list_given[-1])
        del list_given[-1]
        k -= 1
    return list_given


# alternative approach that can be more efficient for large values of 'k' by using slicing. 
# You can achieve the same result with a time complexity of O(n), regardless of the value of 'k'. 
# Using slicing method.
def rotate_list(input_list,k):
    if not input_list or k == 0:
        return input_list
    else:
        k = k  % len(input_list)
        return input_list[-k:] + input_list[:-k]

# Problem 8
# 8. Largest Continuous Sum: Write a function to find the largest sum of contiguous subarray within a list of integers.

# Using Kadane's algorithm.

def largest_contiguous_sum(arr):
    if not arr:
        return arr
    
    current_sum = max_sum = arr[0] # Same as current_sum,max_sum = arr[0],arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
# Note:
# The problem of finding the largest sum of a contiguous subarray within a list can be solved efficiently using the Kadane's algorithm.
# One other algorithm that can be used is the divide-and-conquer algorithm. This algorithm works by recursively dividing the list into two halves, finding the largest sum of a contiguous subarray in each half, and then combining the two results to find the largest sum of a contiguous subarray in the entire list.

# Another question: Modify the function to return both the maximum sum and the corresponding subarray.

