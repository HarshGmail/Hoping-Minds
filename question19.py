"""
Q19. You are given a number N, you need to find the N-th number whose prime factors include 1,2,3,5 in range 1 to 10^3 inclusive
 if you are given a number 7, then output will be 8.
1 : 1
2 : 1,2
3 : 3
4 : 1,2
5 : 1,5
6 : 1,2,3
8 : 1,2
9 : 1,3

"""

def findNthNumber(n):
    count = 0
    number = 1

    while count < n:
        if isDesiredNumber(number):
            count += 1
        number += 1

    return number - 1

def isDesiredNumber(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number //= 2
    while number % 3 == 0:
        prime_factors.append(3)
        number //= 3
    while number % 5 == 0:
        prime_factors.append(5)
        number //= 5
    return number == 1 and set(prime_factors) == {1, 2, 3, 5}

# Example usage:
n = 7
result = findNthNumber(n)
print("The", n, "th number whose prime factors include 1, 2, 3, and 5:", result)
