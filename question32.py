"""
You are given a string allowed consisting of distinct characters and an array of string words. A string is consistent if all characters in the string appear in the string allowed
Return the number of consistent strings in the array of words
Input : allowed = 'ab', words = ['ad','bd','aaab','baa','badab']
Output : 2

Count 1
Count 2
"""
def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    count = 0
    for word in words:
        if all(char in allowed_set for char in word):
            count += 1
    return count

# Example usage:
allowed = 'ab'
words = ['ad', 'bd', 'aaab', 'baa', 'badab']
result = countConsistentStrings(allowed, words)
print("Output:", result)
