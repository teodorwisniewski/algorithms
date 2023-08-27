

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                break
        else:
            return num
        min_idx = i
        max_idx, max_digit = i+1, nums[i+1]
        for j in range(max_idx, n):
            if nums[j] >= max_digit:
                max_idx, max_digit = j, nums[j]

        if min_idx > 0:
            for i in range(min_idx, -1, -1):
                if nums[i] < max_digit:
                    min_idx = i
        
        nums[min_idx], nums[max_idx] = nums[max_idx], nums[min_idx]
        return int(''.join(nums))



            



sol = Solution()


# num = 2736

# res = sol.maximumSwap(num)
# print(f"input {num} maximumSwap {res}")

# input_2 = 9973
# print(f"input_2 {input_2} maximumSwap { sol.maximumSwap(input_2)}")

# input_3 = 115
# print(f"input_3 {input_3} maximumSwap { sol.maximumSwap(input_3)}")

input_4 = 1993
print(f"input_4 {input_4} maximumSwap { sol.maximumSwap(input_4)}")