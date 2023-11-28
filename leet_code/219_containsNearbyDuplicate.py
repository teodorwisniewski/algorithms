from typing import List


# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if not k:
#             return False
        
#         window_nums = set()
#         for idx, num in enumerate(nums):

#             if len(window_nums) > k:
#                 window_nums.remove(nums[idx-k-1])
            
#             if num in window_nums:
#                 return True
            
#             window_nums.add(num)
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_nums = {}

        for i, n in enumerate(nums):
          if n in window_nums and abs(i - window_nums[n]) <= k:
            return True
          else:
            window_nums[n] = i
        
        return False


        


sol = Solution()

nums = [0,1,2,3,2,5]
k = 3
res = sol.containsNearbyDuplicate(nums, k)
assert res

nums = [1,2,3,1]
k = 3
res = sol.containsNearbyDuplicate(nums, k)
assert res

nums = [1,2,3,1,2,3]
k = 2
res = sol.containsNearbyDuplicate(nums, k)
assert not res

