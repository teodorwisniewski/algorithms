


def searchForRange(array, target):
    final_range = [-1, -1]
    altered_binary_search(array, target, 0, len(array)-1, final_range, True)
    altered_binary_search(array, target, 0, len(array)-1, final_range, False)
    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left_flag):

    while left <= right:
        mid = (left+right) // 2
        potential_cand = array[mid]
        if potential_cand < target:
            left = mid + 1
        elif potential_cand > target:
            right = mid - 1
        else:
            # left side of range
            if go_left_flag:
                if mid == 0 or array[mid-1] != target:
                    final_range[0] = mid
                    return
                right = mid - 1
            # right side of range
            else:
                if (len(array)-1) == mid or array[mid+1] != target:
                    final_range[1] = mid
                    return
                left = mid + 1

        


        