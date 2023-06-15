"""
Q10. Automorphic no. 
25 = 25*25 = 625
"""
def is_automorphic_number(num):
    square = num * num
    return str(square).endswith(str(num))


# Example usage:
number = 25
is_automorphic = is_automorphic_number(number)
print(f"The number {number} is an Automorphic number: {is_automorphic}")
