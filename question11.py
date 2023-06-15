"""
Bubble Sort
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
numbers = [5, 2, 8, 12, 3]
print("Original list:", numbers)

bubble_sort(numbers)
print("Sorted list:", numbers)
