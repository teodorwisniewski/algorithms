


def searchForRange(array, target):
    final_range = [-1, -1]
    altered_binary_search(array, target, 0, len(array)-1, final_range, True)
    altered_binary_search(array, target, 0, len(array)-1, final_range, False)
    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left_flag):

    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if go_left_flag:
                if mid == 0 or array[mid-1] != target:
                    final_range[0] = mid
                    return 
                else:
                    right  = mid - 1
            else:
                if mid == (len(array) - 1) or array[mid+1] != target:
                    final_range[1] = mid
                    return
                else:
                    left = mid + 1
        