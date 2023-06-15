""" Remove duplicates from sorted array(duplicates appears atmost twice)
input : 
nums=[1,1,1,2,2,3]
Output :
5

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. the relative order of the elements should be kept the same
"""
def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    # Use two pointers
    i = 0  # Pointer for unique elements
    j = 1  # Pointer to iterate through the array
    count = 1  # Count of current element occurrences
    
    while j < len(nums):
        if nums[i] == nums[j]:
            count += 1
        else:
            count = 1
        
        if count <= 2:
            i += 1
            nums[i] = nums[j]
        
        j += 1
    
    # Return the length of the unique elements
    return i + 1

# Example usage:
nums = [1, 1, 1, 2, 2, 3]

length = removeDuplicates(nums)
print("Unique elements:", nums[:length])
