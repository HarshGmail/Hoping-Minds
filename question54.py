"""Increasing Decreasing String
Input :
s='aaaabbbbcccc'
Output :
'abccbaabccba'

Given a string a. You should re-order the string using the following algorithm:
1. Add the smallest character from s and append it to the result.
2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the largest character from s and append it to the result.
5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, if the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
Return the result string after sorting s with this algorithm.
"""
def sortString(s):
    # Step 1: Create frequency dictionary
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Reorder the string
    result = ''
    while len(result) < len(s):
        # Step 3: Append characters in ascending order
        for char in sorted(frequency.keys()):
            if frequency[char] > 0:
                result += char
                frequency[char] -= 1

        # Step 4: Append characters in descending order
        for char in sorted(frequency.keys(), reverse=True):
            if frequency[char] > 0:
                result += char
                frequency[char] -= 1

    return result

# Example usage
s = 'aaaabbbbcccc'
reordered_string = sortString(s)
print(reordered_string)  # Output: 'abccbaabccba'
