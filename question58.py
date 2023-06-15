"""Shuffle the Array
Input :
nums = [2,5,1,3,4,7]
n=3
Output :
[2,3,5,4,1,7]

Given the array nums consisting of 2n elements in the form [x1,x2,......,xn,y1,y2,......,yn]
Return the array in the form [x1,y1,x2,y2,......,xn,yn]
"""
def shuffle(nums, n):
    shuffled_nums = []
    for i in range(n):
        shuffled_nums.append(nums[i])
        shuffled_nums.append(nums[i+n])
    return shuffled_nums

# Example usage
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
