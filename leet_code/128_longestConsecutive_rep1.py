from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         nums_set = set(nums)
#         longest = 0
#         for num in nums:

#             if (num - 1) not in nums_set:
#                 seq_len = 1
#                 while (num+seq_len) in nums_set:
#                     seq_len += 1
#                 longest = max(longest, seq_len)
#         return longest


                
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        longest = 0

        while nums:
            l, r = 1, 1
            num = nums.pop()
            curr_len = 1
            if (num-l) in nums and (num+r) in nums:
                while (num-l) in nums:
                    nums.remove(num-l)
                    l += 1
                    curr_len += 1
                
                while (num+r) in nums:
                    nums.remove(num+r)
                    r += 1
                    curr_len += 1

            if (num-l) in nums: 
                while (num-l) in nums:
                    nums.remove(num-l)
                    l += 1
                    curr_len += 1

            if (num+r) in nums:
                while (num+r) in nums:
                    
                    nums.remove(num+r)
                    r += 1
                    curr_len += 1

            longest = max(longest, curr_len)
        return longest
            
            
   
sol = Solution()

nums = [100,4,200,1,3,2]
res = sol.longestConsecutive(nums)
print(f"longestConsecutive {res}")