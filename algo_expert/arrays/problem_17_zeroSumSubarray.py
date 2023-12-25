

#  TC O(n) SC O(n)
def zeroSumSubarray(nums):
    sums = {0}
    cs = 0
    for num in nums:
        cs += num
        if cs in sums:
            return True
        sums.add(cs)
    return False







# arr  = [3, 5, -4, 8, 11, 1, -1, 6]
# target = 10
# res = twoNumberSum(arr, target)
# print(f"twoNumberSum {res}")

arr = [-5, -5, 2, 3, -2]
res = zeroSumSubarray(arr)
print(f"zeroSumSubarray {res}")