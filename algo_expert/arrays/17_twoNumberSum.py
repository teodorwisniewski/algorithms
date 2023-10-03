


# TC and SC O(n)
def twoNumberSum(array, targetSum):

    mapping = {}
    for num in array:
        diff = targetSum - num
        if diff in mapping:
            return [diff, num]
        mapping[num] = True

    return []
        






# arr  = [3, 5, -4, 8, 11, 1, -1, 6]
# target = 10
# res = twoNumberSum(arr, target)
# print(f"twoNumberSum {res}")

arr = [4, 6, 1]
target = 5
res = twoNumberSum(arr, target)
print(f"twoNumberSum {res}")