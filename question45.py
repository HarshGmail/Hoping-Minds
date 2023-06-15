""" Maximum repeating substring
Input :
sequence = 'ababc'
word= 'ab'
 Output :
2
For a string sequence, a string word is K-repeating if the word concatenated K times is a substring of sequence. The word's maximum k-repeating value is the highest value k where the word is k-repeating in sequence. if a word is not a substring of sequence, the word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""
def maxRepeating(sequence, word):
    max_repeat = 0
    i = 1
    while word * i in sequence:
        max_repeat = i
        i += 1
    return max_repeat

# Example usage
sequence = 'ababc'
word = 'ab'
result = maxRepeating(sequence, word)
print(result)  # Output: 2
