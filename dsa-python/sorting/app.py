# Bubble Sort
""" Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted. """

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


# Selection Sort
""" Selection Sort divides the array into two parts: the sorted and unsorted sections. It selects the smallest element from the unsorted section and swaps it with the leftmost unsorted element. """

selection_arr = [100, 80, 30, 25, 10, 90, 12]

def selection_sort(selection_arr):
    n = len(selection_arr)
    for i in range(n):

        # It would find the minimum element in the unsorted part.
        min_element = i   
        for k in range(i+1, n):
            if selection_arr[k] < selection_arr[min_element]:
                min_element = k
        
        # It would swap the found minimum element with the first element.
        selection_arr[i], selection_arr[min_element] = selection_arr[min_element], selection_arr[i]
    return selection_arr

print(selection_sort(selection_arr))


# Insertion Sort
""" Insertion Sort builds the sorted array one element at a time by moving each new element into its correct position. """


insertion_arr = [100, 60, 30, 18, 10, 90, 12]

def insertion_sort(insertion_arr):
    for i in range(1, len(insertion_arr)):
        key = insertion_arr[i]
        m = i - 1

        # It would move elements of selection_arr[0...i-1] that are greater than key.
        while m >= 0 and insertion_arr[m] > key:
            insertion_arr[m + 1] = insertion_arr[m]
            m -= 1
        insertion_arr[m + 1] = key
    return insertion_arr

print(insertion_sort(insertion_arr))


# Merge Sort
""" Merge Sort is a divide and conquer algorithm. It divides the array into halves, recursively sorts them, and merges them back together. """

merge_arr = [90, 50, 30, 20, 10, 80, 12]

def merge_sort(merge_arr):
    if len(merge_arr) > 1:
        mid = len(merge_arr) // 2
        left_half = merge_arr[:mid]
        right_half = merge_arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = p = s = 0   # i for left half, p for right half, s for original array index.
        while i < len(left_half) and p < len(right_half):
            if left_half[i] < right_half[p]:
                merge_arr[s] = left_half[i]
                i += 1
            else:
                merge_arr[s] = right_half[p]
                p += 1
            s += 1

        while i < len(left_half):
            merge_arr[s] = left_half[i]
            i += 1
            s += 1
        
        while p < len(right_half):
            merge_arr[s] = right_half[p]
            p += 1
            s += 1

    return merge_arr

print(merge_sort(merge_arr))


# Quick Sort
""" Quick Sort is another divide and conquer algorithm. It selects a 'pivot' element and partitions the array around the pivot. """

quick_arr = [10, 12, 20, 30, 50, 85, 80]

def quick_sort(quick_arr):
    if len(quick_arr) <= 1:
        return quick_arr
    
    pivot = quick_arr[len(quick_arr) // 2]
    left = [x for x in quick_arr if x < pivot]
    middle = [x for x in quick_arr if x == pivot]
    right = [x for x in quick_arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(quick_arr))