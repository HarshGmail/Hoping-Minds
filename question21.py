"""
Write a program to find the  maximum difference between two adjacent numbers in an array of positive integers.
Input 1: 5
Input 2: 10,11,7,12,14
Output: 4
 10 - 11 = -1
11-7 = 4
7-12= -5
12-14= -2

"""

def findMaxAdjacentDifference(arr):
    max_difference = float('-inf')

    for i in range(len(arr) - 1):
        difference = arr[i] - arr[i+1]
        if difference > max_difference:
            max_difference = difference

    return max_difference

# Example usage:
arr = [10, 11, 7, 12, 14]
result = findMaxAdjacentDifference(arr)
print("Maximum difference between adjacent numbers:", result)
