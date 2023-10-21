from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest = 0

        for num in nums:

            if (num - 1) not in nums_set:

                length = 1
                while (num + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest
                



sol = Solution()

nums = [100,4,200,1,3,2]
res = sol.longestConsecutive(nums)
print(f"longestConsecutive {res}")