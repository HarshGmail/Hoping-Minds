"""
You are required to implement the following function:

int CountSpecificNumbers(int m, int n);

The function accepts two arguments m and n which are integers. You are required to calculate the count of numbers having only 1.4 and 9 as their digits between the numbers Iving in the range m and n both inclusive, and return the same. Return -1 if m>n.

Sample Input:

I

100

200

ว

Sample Output:

9

Explanation:

The numbers between 100 and 200, both inclusive having only 1,4 and 9 as their digits are 111, 114, 119, 141, 144, 149, 191, 194, 199. The count is 9 hence 9 is returned
"""

def CountSpecificNumbers(m, n):
    if m > n:
        return -1

    count = 0
    for num in range(m, n + 1):
        digits = set(str(num))
        if all(digit in ['1', '4', '9'] for digit in digits):
            count += 1

    return count

# Example usage:
m = 100
n = 200

result = CountSpecificNumbers(m, n)
print("Count of numbers with only 1, 4, and 9 digits:", result)
