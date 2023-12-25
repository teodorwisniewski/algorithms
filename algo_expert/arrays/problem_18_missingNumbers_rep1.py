

def missingNumbers(nums):
    
    n = len(nums) + 3
    total = sum(range(1, n))
    for num in nums:
        total -= num

    av_missing_val = total // 2
    found_left_sum = 0
    found_right_sum = 0
    for num in nums:
        if num <= av_missing_val:
            found_left_sum += num
        else:
            found_right_sum += num
    
    expected_left = sum(range(1, av_missing_val+1))
    expected_right = sum(range(av_missing_val+1, n))
    return [
        expected_left - found_left_sum,
        expected_right - found_right_sum
    ]
    


arr  = [1, 4, 3]
res = missingNumbers(arr)
print(f"missingNumbers {res}")