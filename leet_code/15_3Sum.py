
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        triplets = []
        for idx in range(n-2):
            curr = nums[idx]
            left = idx + 1
            right = n - 1
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                cs = curr + left_num + right_num
                
                if cs == 0:
                    new_triplet = [curr, left_num, right_num]
                    if new_triplet not in triplets:
                        triplets.append(new_triplet)
                    left += 1
                    right -= 1
                elif cs < 0:
                    left += 1
                elif cs > 0:
                    right -= 1
        return triplets
        




s = Solution()


nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(f"threeSum {res}")

