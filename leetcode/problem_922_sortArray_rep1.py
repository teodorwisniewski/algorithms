
from typing import List


# insertion sort O(n^2)
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:

#         for i in range(1, len(nums)):
#             j = i
#             while j > 0 and nums[j] < nums[j-1]:
#                 nums[j], nums[j-1] = nums[j], nums[j-1]
#                 j -= 1
#         return nums
        

# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        def merge_sort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            
            mid = n // 2
            
            left_part = merge_sort(arr[:mid]) 
            right_part = merge_sort(arr[mid:]) 

            return merge(n, left_part, right_part)

        def merge(n, left_part, right_part):
            sorted_merged_arr = []
            lp, rp = 0, 0

            while len(sorted_merged_arr) < n:

                if left_part[lp] < right_part[rp]:
                    sorted_merged_arr.append(left_part[lp])
                    lp += 1
                else:
                    sorted_merged_arr.append(right_part[rp])
                    rp += 1
            
                if rp == len(right_part):
                    sorted_merged_arr.extend(left_part[lp:])

                if lp == len(left_part):
                    sorted_merged_arr.extend(right_part[rp:])
            return sorted_merged_arr

        return merge_sort(nums)



