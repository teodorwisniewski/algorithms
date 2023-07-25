


# TC average and best case: O(nlogn) worst case O(n^2), TC (logn)
def quickSort(array):
    quick_sort_helper(array, start_idx=0, end_idx=len(array)-1)
    return array


def quick_sort_helper(array, start_idx, end_idx):

    if start_idx >= end_idx:
        return 
    
    pivot_idx = get_pivot(array, start_idx, end_idx)

    is_left_subarray_smaller = pivot_idx - start_idx  < end_idx - pivot_idx

    if is_left_subarray_smaller:
        quick_sort_helper(array, start_idx, pivot_idx-1)
        quick_sort_helper(array, pivot_idx+1, end_idx)
    else:
        quick_sort_helper(array, pivot_idx+1, end_idx)
        quick_sort_helper(array, start_idx, pivot_idx-1)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def get_pivot(arr, start_idx, end_idx):

    left_idx = start_idx + 1
    right_idx = end_idx
    pivot_idx = start_idx
    pivot_val = arr[pivot_idx]
    while left_idx <= right_idx:
        left_val = arr[left_idx]
        right_val = arr[right_idx]
        if left_val > pivot_val and right_val < pivot_val:
            swap(arr, left_idx, right_idx)
        if left_val <= pivot_val:
            left_idx += 1
        if right_val >= pivot_val:
            right_idx -= 1
    swap(arr, pivot_idx, right_idx)
    return right_idx

input_arr = [4, 54, 1, 0, -4, 9]
print(f"Input array goes as follows {input_arr}")
print(f"Sorted array {quickSort(input_arr)}")


input_arr = [2, 1, 5]
print(f"\n\n Input array goes as follows {input_arr}")
print(f"Sorted array {quickSort(input_arr)}")