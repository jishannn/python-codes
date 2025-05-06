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