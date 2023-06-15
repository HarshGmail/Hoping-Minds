"""How many numbers are smaller than the current number
Input :
nums= [8,1,2,2,3]
Output :
[4,0,1,1,3]
Given the array nums, for each nums[i]
"""
def smallerNumbersThanCurrent(nums):
    result = []
    for num in nums:
        count = 0
        for otherNum in nums:
            if otherNum < num:
                count += 1
        result.append(count)
    return result

# Example usage
nums = [8, 1, 2, 2, 3]
result = smallerNumbersThanCurrent(nums)
print(result)  # Output: [4, 0, 1, 1, 3]
