"""Write a program to find the difference between smallest and largest numbers in an array of positive integers.
Eg : - 2,4,7,9,11,12,30,15
Ans:  - 28
"""
def findDifference(arr):
    smallest = float('inf')
    largest = float('-inf')

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return largest - smallest

# Example usage:
arr = [2, 4, 7, 9, 11, 12, 30, 15]
result = findDifference(arr)
print("Difference between smallest and largest numbers:", result)
