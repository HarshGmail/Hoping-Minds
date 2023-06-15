""" Generate a string with characters that have odd counts.
Input :
n=4
Output:
'pppz'

given an integer n return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiple valid strings, return any of them.
"""
def generateString(n):
    result = 'a' * n
    return result

# Example usage
n = 4
odd_string = generateString(n)
print(odd_string)  # Output: 'aaaa'
