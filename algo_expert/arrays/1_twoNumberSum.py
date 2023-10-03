

def twoNumberSum(array, targetSum):
    
    left_idx = 0
    right_idx = len(array) - 1
    array.sort()
    

    while left_idx < right_idx:

        left_nb = array[left_idx]
        right_nb = array[right_idx]
        cs = left_nb + right_nb
        if cs == targetSum:
            # left_idx += 1
            # right_idx -= 1
            return [left_nb, right_nb]
        elif cs < targetSum:
            left_idx += 1
        elif cs > targetSum:
            right_idx -= 1
    return []



# TC and SC O(n)
def twoNumberSum(array, targetSum):

    mapping = {}
    for num in array:
        diff = targetSum - num
        if diff in mapping:
            return [diff, num]
        mapping[num] = True

    return []
        



array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

res = twoNumberSum(array, targetSum)
print(f"twoNumberSum {res}")



array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum = 163
res = twoNumberSum(array, targetSum)
print(f"twoNumberSum {res}")
