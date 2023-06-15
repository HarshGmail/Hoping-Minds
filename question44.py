"""Quick sort"""
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot with element at correct position
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively call quickSort on the two partitions
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


# Example usage
arr = [8, 3, 1, 9, 2, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)  # Output: [1, 2, 3, 5, 8, 9]
