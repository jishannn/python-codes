'''
What is "Two Pointers"?
Two Pointers = using two variables (pointers) to walk through an array from different directions.

'''

def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair_with_sum([1, 3, 4, 6, 8, 9], 10))