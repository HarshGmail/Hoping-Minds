"""Write a program to count the occurrence of digits in a range.
Input 1: starting point - 1
         Ending point - 20
Input 2: Digit: - 1
Output : 12
"""
def countDigitOccurrence(start, end, digit):
    count = 0
    for num in range(start, end+1):
        count += str(num).count(str(digit))
    return count

# Example usage:
start_point = 1
end_point = 20
digit = 1
occurrence = countDigitOccurrence(start_point, end_point, digit)
print("Occurrence:", occurrence)
