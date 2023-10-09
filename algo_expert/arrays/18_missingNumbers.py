

def missingNumbers(nums):
    included_nums = {
        num
        for num in nums
    }
    n = len(nums)
    res = []
    for i in range(1, n+3):
        if i not in included_nums:
            res.append(i)
    return res




arr  = [1, 4, 3]
res = missingNumbers(arr)
print(f"missingNumbers {res}")