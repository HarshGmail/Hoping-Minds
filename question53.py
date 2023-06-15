"""String halves are alike?
Input :
s="bo ok"  
a=bo 
b=ok

Output :
true

You are given a string s of even length. split this string into two halves of equal lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a','e','i','o','u','A','E','I','O','U')
Return true if a and b are alike. Otherwise , return false
"""
def countVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def halvesAreAlike(s):
    length = len(s)
    a = s[:length//2]
    b = s[length//2:]
    
    count_a = countVowels(a)
    count_b = countVowels(b)
    
    return count_a == count_b

# Example usage
s = "bo ok"
result = halvesAreAlike(s)
print(result)  # Output: True
