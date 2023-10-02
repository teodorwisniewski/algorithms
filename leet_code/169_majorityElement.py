from typing import List



# # TC O(n) SC O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counter = {}
#         max_count, res = 0, 0
#         for num in nums:
#             counter[num] = 1 + counter.get(num, 0)
#             res = num if counter[num] > max_count else res
#             max_count = max(max_count, counter[num])
#         return res


# TC O(n) SC O(1)
# Boyer - Moore solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1
        return res



sol = Solution()
nums = [2,2,1,1,1,2,2]
res = sol.majorityElement(nums)
print(f"majorityElement {res}")