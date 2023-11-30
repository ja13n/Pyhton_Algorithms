def selection_sort(arr: list):
    for i, el in enumerate(arr):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
