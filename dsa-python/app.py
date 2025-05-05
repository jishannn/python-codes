# Bubble Sort
arr = [100, 80, 30, 25, 10, 90, 12]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]    # Swap
                swapped = True

        if not swapped:
            break    # if array is already sorted then no need to swaps.
    return arr

print(bubble_sort(arr))