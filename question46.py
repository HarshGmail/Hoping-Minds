"""Reverse the sentence
Input :
s='i am hungry'
Output:
'hungry am i'

given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one psace.
Return a string of the words in reverse order concatenated by a single space.
"""
def reverseSentence(s):
    words = s.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words with a space
    return reversed_sentence

# Example usage
s = 'i am hungry'
result = reverseSentence(s)
print(result)  # Output: 'hungry am i'
