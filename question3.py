"""Q 3 . Special no.
59
5 9
5+9= 14
5*9=45
14+45=59
"""
def is_special_number(num):
    digits = [int(digit) for digit in str(num)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    return digit_sum + digit_product == num


# Example usage:
number = 59
is_special = is_special_number(number)
print(f"The number {number} is special: {is_special}")
