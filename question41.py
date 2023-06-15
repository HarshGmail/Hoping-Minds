"""
 Write a program to find Strong Prime number taking the interval from the user - 
Pn>Pn+1 + Pn-12
P = prime no.
n= position of P
"""
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_strong_prime(num):
    if not is_prime(num):
        return False
    position = 0
    prev_prime = 0
    curr_prime = 2
    while curr_prime <= num:
        if curr_prime > prev_prime + position + 1:
            return False
        prev_prime = curr_prime
        position += 1
        curr_prime = next_prime(curr_prime)
    return True

def next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

# Get the interval from the user
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

# Find strong prime numbers within the interval
strong_primes = []
for num in range(start, end + 1):
    if is_strong_prime(num):
        strong_primes.append(num)

# Print the strong prime numbers
print("Strong prime numbers in the interval:", strong_primes)
