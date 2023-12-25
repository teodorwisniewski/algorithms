from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        diff1 = list(nums1 - nums2)
        diff2 = list(nums2 - nums1)
        return [diff1, diff2]
        




sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
res = sol.findDifference(nums1, nums2)
assert res == [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
res = sol.findDifference(nums1, nums2)
assert res == [[3],[]]