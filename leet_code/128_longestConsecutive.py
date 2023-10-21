from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         nums_set = set(nums)
#         longest = 0

#         for num in nums:
#             if (num - 1) not in nums_set:
#                 length = 1
#                 while (num + length) in nums_set:
#                     length += 1
#                 longest = max(longest, length)
#         return longest
                

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest = 0

        while nums_set:

            num = nums_set.pop()
            curr_len = 1

            l = num - 1
            r = num + 1

            if l in nums_set and r in nums_set:

                while r in nums_set:
                    nums_set.remove(r)
                    r += 1
                    curr_len += 1
                
                while l in nums_set:
                    nums_set.remove(l)
                    l -= 1
                    curr_len += 1 

            if l in nums_set:
                
                while l in nums_set:
                    nums_set.remove(l)
                    l -= 1
                    curr_len += 1                
 
            if r in nums_set:

                while r in nums_set:
                    nums_set.remove(r)
                    r += 1
                    curr_len += 1
            
            longest = max(curr_len, longest)
        return longest
                
   
sol = Solution()

nums = [100,4,200,1,3,2]
res = sol.longestConsecutive(nums)
print(f"longestConsecutive {res}")