


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p3 = m + n - 1
        a, b = m - 1, n - 1
        while b >= 0:
            val1 = nums1[a]
            val2 = nums2[b]
            if a >= 0 and val1 > val2:
                nums1[p3] = val1
                a -= 1
            else:
                nums1[p3] = val2
                b -= 1
            p3 -= 1
        
 

        


sol = Solution()

nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
print(f"merge {nums1}")