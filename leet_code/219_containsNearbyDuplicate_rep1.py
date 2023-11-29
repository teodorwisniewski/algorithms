from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {} # number -> idx
        for idx, num in enumerate(nums):
            if num in hash_map and (idx - hash_map[num]) <= k:
                return True
            hash_map[num] = idx
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

