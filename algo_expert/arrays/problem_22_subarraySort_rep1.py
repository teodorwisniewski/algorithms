


def subarraySort(array):

    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    for idx, num in enumerate(array):
        if is_out_of_order(idx, array, num):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)         

    if min_out_of_order == float("inf"):
        return [
            -1, -1
        ]
    
    left_out_of_order_idx = 0
    while array[left_out_of_order_idx] <= min_out_of_order:
        left_out_of_order_idx += 1
    
    right_out_of_order_odx = len(array) - 1
    while array[right_out_of_order_odx] >= max_out_of_order:
        right_out_of_order_odx -= 1
    
    return [
        left_out_of_order_idx,
        right_out_of_order_odx
    ]


def is_out_of_order(idx, array, num):
    if idx == 0:
        return num > array[idx+1]
    
    if idx == len(array) - 1:
        return num < array[idx-1]

    return num > array[idx+1] or num < array[idx-1]


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
res = subarraySort(array)
print(f"subarraySort {res}")
assert res == [3, 9]