from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
        




sol = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
res = sol.containsDuplicate(nums)
print(f"containsDuplicate {res}")