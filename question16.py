"""
input1:3

Input2: {1,2,3}

Output: 2

Explanation:

The order that incurs the minimum penalty is 1,2,3. The penalty is abs(2-1)+abs(3-2)=2

Input1:4

Input2: (-2,1,4,6}

Output: 8
"""
def CalculateMinimumPenalty(n, arr):
    penalty = 0
    for i in range(1, n):
        penalty += abs(arr[i] - arr[i - 1])
    return penalty

# Example usage:
n = 3
arr = [1, 2, 3]
result = CalculateMinimumPenalty(n, arr)
print("Minimum penalty:", result)

n = 4
arr = [-2, 1, 4, 6]
result = CalculateMinimumPenalty(n, arr)
print("Minimum penalty:", result)
