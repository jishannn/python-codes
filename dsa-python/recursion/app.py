# Writing a function that counts from 5 to 1
"""def countdown(n):
    if n == 0:         # base case: when to stop. otherwise, recursion would be infinite and crash the program.
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)"""


# Recursive Binary Search
def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)


arr = [2, 4, 6, 8, 10]
print(recursive_binary_search(arr, 10, 0, len(arr) - 1))