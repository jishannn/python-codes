""" def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid        # found it
        elif guess < target:
            low = mid + 1     # go right
        else:
            high = mid - 1    # go left

    return -1    # not found


arr = [2, 4, 6, 8, 9, 10, 12, 14, 16]
print(binary_search(arr, 9)) """



"""
# Practice
def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low =  mid + 1
        else:
            high = mid - 1
        
    return -1



arr = [1, 3, 5, 7, 9, 11, 12, 13, 15]
print(binary_search(arr, 12)) """



#Problem 2
"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high =  mid - 1

    return -1
            
arr = [2, 4, 6, 8, 10, 12, 14]
print(binary_search(arr, 6)) """


# Problem 3
""" def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess <= target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 5, 7, 9, 13, 18]
print(binary_search(arr, 20)) """




def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess >= target:
            result =  mid
            high = mid - 1
        else:
            low = mid + 1

    return result

arr = [1, 4, 6, 7, 9, 10, 14, 18]
print(binary_search(arr, 10))