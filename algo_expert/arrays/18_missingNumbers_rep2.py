

def missingNumbers(nums):

    n = len(nums) + 3
    total = sum(range(1, n))
    for num in nums:
        total -= num

    av_missing_nums = total // 2

    left_sum = 0 
    right_sum = 0

    for num in nums:
        if num <= av_missing_nums:
            left_sum += num
        else:
            right_sum += num
    
    expected_left_sum = sum(range(1, av_missing_nums+1))
    expected_right_sum = sum(range(av_missing_nums+1, n))
    
    return [
        expected_left_sum - left_sum,
        expected_right_sum - right_sum
    ]


arr  = [1, 4, 3]
res = missingNumbers(arr)
print(f"missingNumbers {res}")