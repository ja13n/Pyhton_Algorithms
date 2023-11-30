def bubble_sort(arr, index1, index2):
    for i, el in enumerate(arr):
        if arr[i] > arr[i + 1]:
            temp = arr[index1]
            arr[index1] = arr[index2]
            arr[index2] = temp
