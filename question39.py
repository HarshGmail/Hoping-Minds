"""Write a program to  print all Strong numbers between the intervals entered by the user.

123
1! + 2! + 3! = 
1 + 2 + 6 = 9
123 == 9 NO


2. 
145
1! +  4!  +  5!
1  +  24  +  120 = 145
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def isStrongNumber(num):
    # Convert the number to a string to access each digit
    num_str = str(num)
    # Calculate the sum of factorials of each digit
    factorial_sum = sum(factorial(int(digit)) for digit in num_str)
    # Check if the sum is equal to the number
    if factorial_sum == num:
        return True
    else:
        return False

# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Strong numbers between", start, "and", end, "are:")
strong_numbers = []
for num in range(start, end + 1):
    if isStrongNumber(num):
        strong_numbers.append(num)

if len(strong_numbers) == 0:
    print("No strong numbers found in the given range.")
else:
    for strong_num in strong_numbers:
        print(strong_num)
