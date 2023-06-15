"""
remove Outermost parentheses
Input : (()())(())
Output: ()()()
"""
def removeOuterParentheses(s):
    stack = []
    result = ""

    for char in s:
        if char == "(":
            if stack:
                result += char
            stack.append(char)
        elif char == ")":
            stack.pop()
            if stack:
                result += char

    return result

# Example usage:
input_string = "(()())(())"
output_string = removeOuterParentheses(input_string)
print("Output:", output_string)
