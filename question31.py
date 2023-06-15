"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so 'a' is considered a different type of stone from 'A'
Input : 
Jewels = 'aA'
Stones = 'aAAbbbb'
output : 3
"""
def countJewelsInStones(Jewels, Stones):
    jewel_set = set(Jewels)
    count = 0
    for stone in Stones:
        if stone in jewel_set:
            count += 1
    return count

# Example usage:
Jewels = 'aA'
Stones = 'aAAbbbb'
result = countJewelsInStones(Jewels, Stones)
print("Output:", result)
