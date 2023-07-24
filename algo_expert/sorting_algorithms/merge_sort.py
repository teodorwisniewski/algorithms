from typing import List, Union


# O(n *logn) SC O(n)
def mergeSort(arr: List) -> List:
    
    if len(arr) == 1:
        return arr
    
    mid_idx = len(arr) // 2
    left_part = arr[:mid_idx]
    right_part = arr[mid_idx:]

    return merge(
        mergeSort(left_part),
        mergeSort(right_part)
    )


def merge(left, right):

    merged_arr = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        left_value = left[left_idx]
        right_value = right[right_idx]
        if left_value < right_value:
            merged_arr.append(left_value)
            left_idx += 1
        else:
            merged_arr.append(right_value)
            right_idx += 1            

    return merged_arr + left[left_idx:] + right[right_idx:]


input_arr = [4, 54, 1, 0, -4, 9]
print(f"Input array goes as follows {input_arr}")
print(f"Sorted array {mergeSort(input_arr)}")


input_arr = [2, 1, 5]
print(f"\n\n Input array goes as follows {input_arr}")
print(f"Sorted array {mergeSort(input_arr)}")