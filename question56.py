"""The running sum of 1d Array
Input : 
nums=[3,1,2,10,1]
Output : [3,4,6,16,17]

Given an array nums. We define a running sum of an array as runningSum[i]=sum(nums[0].....nums[i])
Return the running sum of nums.
"""
def runningSum(nums):
    running_sum = []
    sum_so_far = 0
    for num in nums:
        sum_so_far += num
        running_sum.append(sum_so_far)
    return running_sum

# Example usage
nums = [3, 1, 2, 10, 1]
result = runningSum(nums)
print(result)  # Output: [3, 4, 6, 16, 17]
