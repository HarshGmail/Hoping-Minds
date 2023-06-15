"""Repeated Substring pattern
Input :
s='abab'
Output:
True

Input :
s='aba'
Output:
False

Original string =
abab
Append it
‘abababab’

i=0
I+1 till last index - 1
‘ a  bababa   b’
We are 
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
Constraints:
1<= s.length <=10^4
s consists of lowercase English letters.
"""
def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False

# Example usage
s = "abab"
result = repeatedSubstringPattern(s)
print(result)  # Output: True

s = "aba"
result = repeatedSubstringPattern(s)
print(result)  # Output: False
