"""Trailing Zeroes

5! = 120

10! = 3628800

100! = 24

5/5 = 1 T.Z.1

10/5 = 2 ->T.Z.2

100/5 = 20

20/5 = 4

20+4=24"""

def CountTrailingZeroes(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

# Example usage:
n = 100
result = CountTrailingZeroes(n)
print("Number of trailing zeroes in", n, "!: ", result)
