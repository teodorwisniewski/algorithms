
from typing import List


# insertion sort O(n^2)
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:

#         for i in range(1, len(nums)):
#             j = i
#             while j > 0 and nums[j-1] > nums[j]:
#                 nums[j-1], nums[j] = nums[j], nums[j-1]
#                 j -= 1
        
#         return nums
        

# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return 
            
            mid = len(arr) // 2
            left_part = arr[:mid]
            right_part = arr[mid:]

            merge_sort(left_part)
            merge_sort(right_part)

            merge(arr, left_part, right_part)
            

        def merge(arr, left_part, right_part):

            lp, rp = 0, 0
            main_p = 0

            while lp < len(left_part) and rp < len(right_part):

                if left_part[lp] < right_part[rp]:
                    arr[main_p] = left_part[lp]
                    lp += 1
                else:
                    arr[main_p] = right_part[rp]
                    rp += 1

                main_p += 1

            while lp < len(left_part):
                arr[main_p] = left_part[lp]
                lp += 1
                main_p += 1
            
            while rp < len(right_part):
                arr[main_p] = right_part[rp]
                rp += 1
                main_p += 1            

        merge_sort(nums)
        return nums
        