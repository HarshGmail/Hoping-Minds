"""Remove Duplicates from sorted array
Input : 
nums=[0,0,1,1,1,2,2,3,3,4]
Output : 
nums=[0,1,2,3,4]

Given an integer array nums sorted array in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
"""
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    # Use two pointers
    i = 0  # Pointer for unique elements
    j = 1  # Pointer to iterate through the array
    
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    
    # Return the length of the unique elements
    return i + 1

# Example usage:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

length = removeDuplicates(nums)
print("Unique elements:", nums[:length])
