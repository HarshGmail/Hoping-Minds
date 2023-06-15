"""Write a program to  print all Perfect numbers between the intervals entered by the user.


For eg-
Input = 
5
Output = invalid
5 = 1, 5
1+5 = 6
5!=6

Input = 6
Output = perfect no.
6 = 1,2,3
1+2+3 = 6
6==6
"""
def isPerfectNumber(num):
    # Find all the proper divisors of the number
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    
    # Check if the sum of divisors is equal to the number
    if sum(divisors) == num:
        return True
    else:
        return False

# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Perfect numbers between", start, "and", end, "are:")
perfect_numbers = []
for num in range(start, end + 1):
    if isPerfectNumber(num):
        perfect_numbers.append(num)

if len(perfect_numbers) == 0:
    print("No perfect numbers found in the given range.")
else:
    for perfect_num in perfect_numbers:
        print(perfect_num)
