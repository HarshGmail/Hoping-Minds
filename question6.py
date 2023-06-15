"""
Harshad / Niven No.
Eg. 156=
1+5+6 = 12
156/12==0
"""
def is_harshad_number(num):
    digits = [int(digit) for digit in str(num)]
    digit_sum = sum(digits)
    return num % digit_sum == 0


# Example usage:
number = 156
is_harshad = is_harshad_number(number)
print(f"The number {number} is a Harshad (Niven) number: {is_harshad}")