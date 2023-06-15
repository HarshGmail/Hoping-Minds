"""Kids with the greatest number of candies
Input :
candies= [2,3,5,1,3] , extraCandies =3
Output :
[true,true,true,false,true]
Given the array of candies and the integer extraCandies, where candies[i] represents the number of candies that the i-th kid has.
For each kid check if there is a way to distribute extraCandies among the kids so that he or she can 
 have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.
"""
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = []

    for candy_count in candies:
        if candy_count + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result

# Example usage
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)  # Output: [True, True, True, False, True]
