"""Total number of common factors between 2 numbers
Input :
a=12, b=24
Output:
6
"""
def getTotalCommonFactors(a, b):
    smaller = min(a, b)
    count = 0

    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            count += 1

    return count

# Example usage
a = 12
b = 24
total_common_factors = getTotalCommonFactors(a, b)
print(total_common_factors)  # Output: 6
