"""Write a program to  print all Armstrong numbers between the intervals entered by the user.
"""
def isArmstrongNumber(num):
    # Convert the number to string to calculate the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    if sum_of_powers == num:
        return True
    else:
        return False

# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if isArmstrongNumber(num):
        print(num)
