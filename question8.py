"""
Q8. Neon no.
9= 9*9 = 81
8+1=9
"""
def is_neon_number(num):
    square = num * num
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == num


# Example usage:
number = 9
is_neon = is_neon_number(number)
print(f"The number {number} is a Neon number: {is_neon}")
