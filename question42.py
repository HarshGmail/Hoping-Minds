"""Haystack and needle problem
Input :
haystack='happy'
needle='pp'
output :
2
 haystack='happy'
needle='ll'
output :
-1


haystack='happy'
needle=’ '
output :
0



return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
haystack and needle consist of only lower case english characters
"""
def strStr(haystack, needle):
    if needle == "":
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# Example usage
haystack = "happy"
needle = "pp"
result = strStr(haystack, needle)
print(result)  # Output: 2

haystack = "happy"
needle = "ll"
result = strStr(haystack, needle)
print(result)  # Output: -1

haystack = "happy"
needle = " "
result = strStr(haystack, needle)
print(result)  # Output: 0
