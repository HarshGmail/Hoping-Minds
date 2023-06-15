""" Given an integer K and an array[] of N integers which contains the ids of the opened apps in a system where 
1. arr[0] is the app currently in use
2. arr[1] is the app that was most recently used
3. arr[N-1] is the app that was least recently used
The task is to print the contents of the array when the user using the system presses Alt+Tab exactly K number of times. Note that after pressing the Alt+Tab key, the app opening pointer will move through apps from the 0th index towards the right, depending upon the number of presses, so the app on which the press ends will shift to the 0th index because that will become the most recently opened app.
Input: arr[] ={3,5,2,4,1}
K=3
output: 4 3 5 2 1 


3   5  2  4  1
k= 2


Output - 2  3  5  4 1 


K =4
 1  2  3  5  4 


K =1 

2  1  3  5  4
"""
def altTab(arr, k):
    n = len(arr)
    k %= n  # Adjust k to ensure it is within the range of the array size

    # Rotate the array to shift the most recently used app to the 0th index
    arr = arr[-k:] + arr[:-k]

    return arr

# Example usage:
arr = [3, 5, 2, 4, 1]
k = 3
result = altTab(arr, k)
print("Output:", ' '.join(map(str, result)))
