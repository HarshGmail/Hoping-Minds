"""
Q4. Spy no. 
123
1  2   3 
1+2+3 = 6
1*2*3 = 6
"""
def is_spy_number(num):
    digits = [int(digit) for digit in str(num)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    return digit_sum == digit_product


# Example usage:
number = 123
is_spy = is_spy_number(number)
print(f"The number {number} is a spy number: {is_spy}")
