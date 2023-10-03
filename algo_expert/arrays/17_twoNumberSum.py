



def twoNumberSum(array, targetSum):



    array.sort()
    left, right = 0, len(array) - 1


    while left <= right:
        left_val, right_val = array[left], array[right]
        cs = left_val + right_val
        if cs == targetSum:
            return [left_val, right_val]
        elif cs < targetSum:
            left += 1
        else:
            right -= 1
    return []
        






# arr  = [3, 5, -4, 8, 11, 1, -1, 6]
# target = 10
# res = twoNumberSum(arr, target)
# print(f"twoNumberSum {res}")

arr = [4, 6, 1]
target = 5
res = twoNumberSum(arr, target)
print(f"twoNumberSum {res}")