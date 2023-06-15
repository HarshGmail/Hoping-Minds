"""
Given an array of integers representing measurements in inches. Write a program to calculate the total measurements in feet. Ignore the measurements that are less than a feet.
eg. - 
input 1: - 5
Input 2: - 18,11,27,12,14
Output: - 5

"""
def calculateTotalFeet(arr):
    total_feet = 0

    for measurement in arr:
        if measurement >= 12:
            total_feet += measurement // 12

    return total_feet

# Example usage:
arr = [18, 11, 27, 12, 14]
result = calculateTotalFeet(arr)
print("Total measurements in feet:", result)
