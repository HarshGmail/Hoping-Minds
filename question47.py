"""Reverse word in a string
Input :
s='let's do it'
Output:
's'tel od it'
"""
def reverseWords(s):
    words = s.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)  # Join the reversed words with a space
    return reversed_string

# Example usage
s = "let's do it"
result = reverseWords(s)
print(result)  # Output: "s'tel od ti"
