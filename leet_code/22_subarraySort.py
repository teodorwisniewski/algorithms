


def subarraySort(array):
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    for idx, val in enumerate(array):
        if is_out_of_order(array, val, idx):
            min_out_of_order = min(min_out_of_order, val)
            max_out_of_order = max(max_out_of_order, val)

    if min_out_of_order == float("inf"):
        return [-1, -1]
    
    left_subarray_idx = 0
    while min_out_of_order >= array[left_subarray_idx]:
        left_subarray_idx += 1
    
    right_subarray_idx = len(array) - 1
    while max_out_of_order <= array[right_subarray_idx]:
        right_subarray_idx -= 1

    return [
        left_subarray_idx,
        right_subarray_idx
    ]


def is_out_of_order(array, num, idx) -> bool:
    if idx == 0:
        return num > array[idx+1]
    
    if idx == len(array) - 1:
        return num < array[idx-1]
    
    return num > array[idx+1] or num < array[idx-1]




array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
res = subarraySort(array)
print(f"subarraySort {res}")