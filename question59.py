"""Number of Good pairs
Input :
nums =[1,2,3,1,1,3]
Output: 4
Given an array of integers nums.
A pair (i,j) is called good if nums[i]==nums[j] and i < j
Return the number of good pairs.
"""
def numIdenticalPairs(nums):
    count = 0
    freq = {}
    for num in nums:
        if num in freq:
            count += freq[num]
        freq[num] = freq.get(num, 0) + 1
    return count

# Example usage
nums = [1, 2, 3, 1, 1, 3]
result = numIdenticalPairs(nums)
print(result)  # Output: 4
