"""
A valid parentheses sequence is a non empty string where each character is either '(' or  ')'  ,   which satisfies the following constraint :
You can find a way to repeatedly erase adjacent pairs of parentheses '()' until it becomes empty.
For example : - '(())'   and '()((()()))'  are valid parentheses sequences, but ')()('  and  '(()' are not .

Input : ()((()()))
Output : ((()))

(())) - invalid 
)(())( - invalid
 ((()))
"""
def validateParentheses(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    return ''.join(stack)

# Example usage:
sequence = "(()((()()))"
result = validateParentheses(sequence)
print("Output:", result)
