"""String matching in an array
Input :
words=["mass", "as","hero","superhero"]
output :
["as", "hero"]

Given an array of string words. return all strings in words which are a substring of another word in any order.
String words[i] is a substring of words[j] that can be obtained by removing some characters to the left and/or right side of words[j].
"""
def stringMatching(words):
    result = []
    n = len(words)

    for i in range(n):
        for j in range(n):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break

    return result

# Example usage
words = ["mass", "as", "hero", "superhero"]
result = stringMatching(words)
print(result)  # Output: ['as', 'hero']
