"""
Insertion no.
"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
numbers = [5, 2, 8, 12, 3]
print("Original list:", numbers)

insertion_sort(numbers)
print("Sorted list:", numbers)
