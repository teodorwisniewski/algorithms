from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums_idx_map = {
            num: idx
            for idx, num in enumerate(nums1)
        }
        res = [-1] * len(nums1)

        for i, num2 in enumerate(nums2):
            if num2 not in nums_idx_map:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > num2:
                    idx = nums_idx_map[num2]
                    res[idx] = nums2[j]
                    break
        return res





sol = Solution()


nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = sol.nextGreaterElement(nums1, nums2)
print(f"nextGreaterElement {res}")