from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                l += 1
        return l



sol = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
res = sol.removeElement(nums, val)
print(f"removeElement {res}")
print(f"removeElement {nums}")