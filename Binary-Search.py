def binary_search(arr, value):
    left_pointer = 0
    right_pointer = len(arr)

    while left_pointer < right_pointer:
        mid = (left_pointer + right_pointer) // 2
        mid_val = arr[mid]
        if mid_val == value:
            return mid
        if value < mid_val:
            right_pointer = mid
        if value > mid_val:
            left_pointer = mid + 1
    return "Value not in list"
