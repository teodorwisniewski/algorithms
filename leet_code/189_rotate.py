

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        n = len(nums)
        # reverse the list
        self.reverse_lst(nums, 0, n-1)
        # reverse the first part 
        self.reverse_lst(nums, 0, k-1)
        # reverst the second part
        self.reverse_lst(nums, k, n-1)
        
    def reverse_lst(self, lst, left, right):

        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
            left += 1
        





sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums, k)
print(f"rotate {nums}")