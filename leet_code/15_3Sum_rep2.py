
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, num in enumerate(nums):

            if i > 0 and  nums[i-1] == num:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cs = num + nums[left] + nums[right]

                if cs < 0:
                    left += 1
                elif cs > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                                   
        return res


    
        




s = Solution()


nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(f"threeSum {res}")


nums = [0, 0, 0, 0, 0]
res = s.threeSum(nums)
print(f"threeSum {res}")
