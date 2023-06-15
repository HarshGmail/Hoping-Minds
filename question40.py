"""Remove all adjacent duplicates in string
Input : 
s='abbaca'
Output:
'ca'
"""
def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Get the input string from the user
s = input("Enter a string: ")

# Remove adjacent duplicates
result = removeDuplicates(s)

print("String after removing adjacent duplicates:", result)
