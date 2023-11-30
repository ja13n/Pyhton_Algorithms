def fibonacci(n):
    nums_list = []
    if n < 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    for num in range(1, n):
        fibnum = (num - 1) + num
        nums_list.append(fibnum)
        nums_list.append(num)
    return len(nums_list)
