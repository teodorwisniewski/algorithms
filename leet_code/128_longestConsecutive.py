from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         nums = set(nums)
#         longest = 0

#         for num in nums:
#             if (num - 1) not in nums:
#                 length = 1
#                 while (num + length) in nums:
#                     length += 1
#                 longest = max(longest, length)
#         return longest
                

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        longest = 0

        while nums:

            num = nums.pop()
            curr_len = 1

            l = num - 1
            r = num + 1

            if l in nums and r in nums:

                while r in nums:
                    nums.remove(r)
                    r += 1
                    curr_len += 1
                
                while l in nums:
                    nums.remove(l)
                    l -= 1
                    curr_len += 1 

            if l in nums:
                
                while l in nums:
                    nums.remove(l)
                    l -= 1
                    curr_len += 1                
 
            if r in nums:

                while r in nums:
                    nums.remove(r)
                    r += 1
                    curr_len += 1
            
            longest = max(curr_len, longest)
        return longest
                
   
sol = Solution()

nums = [100,4,200,1,3,2]
res = sol.longestConsecutive(nums)
print(f"longestConsecutive {res}")