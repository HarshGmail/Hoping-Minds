"""
Q7. Duck no. = containing 0
Eg. 2008,7088,010….
"""
def is_duck_number(num):
    digits = [digit for digit in str(num)]
    return '0' in digits and digits[0] != '0'


# Example usage:
number = 2008
is_duck = is_duck_number(number)
print(f"The number {number} is a Duck number: {is_duck}")
