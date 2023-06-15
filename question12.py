"""
Selection sort
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
numbers = [5, 2, 8, 12, 3]
print("Original list:", numbers)

selection_sort(numbers)
print("Sorted list:", numbers)
