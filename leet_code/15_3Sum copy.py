
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # nums.sort()
        n = len(nums)
        triplets = []
        
        for idx in range(n):
            curr = nums[idx]
            rest_target = 0 - curr
            lookup = {}
            for i in range(idx+1, n):
                num = nums[i]
                rest = rest_target - num
                if i == idx:
                    continue
                if rest in lookup:
                    new_triplet = sorted([curr, rest, num])
                    if new_triplet not in triplets:
                        triplets.append(new_triplet)
                lookup[num] = True

            
        return triplets
        




s = Solution()


nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(f"threeSum {res}")

nums = [0,0,0]
res = s.threeSum(nums)
print(f"threeSum {res}")
