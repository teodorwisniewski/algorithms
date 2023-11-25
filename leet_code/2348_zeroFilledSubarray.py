from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        self.memo = {}
        
        conseq_cnt_zeros = 0
        res = 0
        for num in nums:
            if num == 0:
                conseq_cnt_zeros += 1
            else:
                res += self.count_zero_subarrays(conseq_cnt_zeros)
                conseq_cnt_zeros = 0
        res += self.count_zero_subarrays(conseq_cnt_zeros)
        return res


    def count_zero_subarrays(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = n + self.count_zero_subarrays(n-1)
        return self.memo[n]

        




sol = Solution()
nums = [0,0,0,2,0,0]
res = sol.zeroFilledSubarray(nums)
print(f"zeroFilledSubarray {res}")
assert res == 9 
