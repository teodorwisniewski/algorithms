from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        



sol = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
res = sol.removeElement(nums, val)
print(f"removeElement {res}")
print(f"removeElement {nums}")