"""How many times a substring contains in a string.
Input:
Text= abxabcabcaby
Pattern= abcaby
Output:
1

 Input : aaaa
3 repetition of patterns
Pattern = aa
aaaa
aaaa
aaaa
Output : 3 
"""
def countSubstringOccurrences(text, pattern):
    count = 0
    start_index = 0

    while True:
        index = text.find(pattern, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1

    return count

# Example usage
text = "abxabcabcaby"
pattern = "abcaby"
occurrences = countSubstringOccurrences(text, pattern)
print(occurrences)  # Output: 1
