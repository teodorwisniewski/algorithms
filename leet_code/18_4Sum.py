from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        results, quad = [], []
        n = len(nums)
        nums.sort()

        def k_sum_rec(k: int, start: int, target: int):

            if k > 2:

                for i in range(start, n - k + 1):
                    num = nums[i]
                    if i > start and num == nums[i-1]:
                        continue
                    quad.append(num)
                    k_sum_rec(k-1, i+1, target-num)
                    quad.pop()
                return
            
            left, right = start, n-1
            while left < right:
                left_val = nums[left]
                right_val = nums[right]
                cs = left_val + right_val
                if cs < target:
                    left += 1
                elif cs > target:
                    right -= 1
                else:
                    results.append(quad + [left_val, right_val])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        k_sum_rec(4, 0, target)
        return results


nums = [1,0,-1,0,-2,2]
target = 0


sol = Solution()
res = sol.fourSum(nums, target)
print(f"fourSum {res}")