"""
Write a program to return the difference between the sum of odd and even numbers from an array of positive integers.
eg. : - 
input 1: - 5
input 2: - 10,11,7,12,14
output : - -18

"""
def findDifferenceOddEven(arr):
    sum_odd = 0
    sum_even = 0

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_odd - sum_even

# Example usage:
arr = [10, 11, 7, 12, 14]
result = findDifferenceOddEven(arr)
print("Difference between sum of odd and even numbers:", result)
