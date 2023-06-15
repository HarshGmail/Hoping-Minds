"""
Q18. Given an array of integers, find the maximum sum of a contiguous subarray 
(a subarray with consecutive elements) within the array. Write a function maxSubarraySum 
that takes an array of integers as input and returns the maximum sum of a contiguous 
"""
def maxSubarraySum(arr):
    current_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubarraySum(arr)
print("Maximum sum of a contiguous subarray:", result)

