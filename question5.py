"""
Q5 . sample input - 8     3    5      2     4     7     9     1 
Sample output- 198   75   112    20    16    9     0     0
"""
def calculate_output(numbers):
    output = []
    for i in range(len(numbers)):
        left_product = 1
        right_product = 1
        for j in range(i):
            left_product *= numbers[j]
        for j in range(i+1, len(numbers)):
            right_product *= numbers[j]
        output.append(left_product + right_product)
    return output


# Example usage:
input_numbers = [8, 3, 5, 2, 4, 7, 9, 1]
output_numbers = calculate_output(input_numbers)
print("Sample Output:", output_numbers)
