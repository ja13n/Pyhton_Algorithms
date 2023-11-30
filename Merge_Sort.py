def merge_sort(arr: list):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        l_count, r_count, arr_count = 0, 0, 0
        while l_count < len(left_half) and r_count < len(right_half):
            if left_half[l_count] <= right_half[r_count]:
                arr[arr_count] = left_half[l_count]
                l_count += 1
            else:
                arr[arr_count] = right_half[r_count]
                r_count += 1
            arr_count += 1

        while l_count < len(left_half):
            arr[arr_count] = left_half[l_count]
            arr_count += 1
            l_count += 1

        while r_count < len(right_half):
            arr[arr_count] = right_half[r_count]
            arr_count += 1
            r_count += 1
    return arr
