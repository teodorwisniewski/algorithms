

def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]


def pivot(arr, pivot_idx=0, end_idx=None) -> int:

    if end_idx is None:
        end_idx = len(arr)-1
    swap_idx = pivot_idx
    for idx in range(pivot_idx+1, end_idx+1):
        if arr[idx] < arr[pivot_idx]:
            swap_idx += 1
            swap(arr, idx, swap_idx)
    swap(arr, swap_idx, pivot_idx)
    return swap_idx


def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # base case
    if left >= right:
        return arr
    
    pivot_idx = pivot(arr, left, right)

    # recursive calls
    quick_sort(arr, left, pivot_idx-1)
    quick_sort(arr, pivot_idx+1, right)

    return arr


if __name__ == "__main__":

    my_list = [4, 6, 1, 7, 3, 2, 5]
    # print(pivot(my_list))
    print(my_list)
    print(quick_sort(my_list))

    # my_list = [2, 3, 4]
    # print(pivot(my_list))
    # print(my_list)

    # my_list = [4, 3, 2]
    # print(pivot(my_list))
    # print(my_list)
