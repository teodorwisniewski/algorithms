from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_val = nums[0]
        middle_val = float("inf")

        for num in nums:

            if num <= min_val:
                min_val = num
            elif num <= middle_val:
                middle_val = num
            else: 
                return True
        return False
            

sol = Solution()

# nums = [2,1,5,0,4,6]


# res = sol.increasingTriplet(nums)
# print(f"increasingTriplet {res}")

# nums = [5,4,3,2,1]
# res2 = sol.increasingTriplet(nums)
# print(f"increasingTriplet {res2}")

nums = [2,4,-2,-3]
res4 = sol.increasingTriplet(nums)
print(f"increasingTriplet {res4}")


nums = [1,2,2,1]
res4 = sol.increasingTriplet(nums)
print(f"increasingTriplet {res4}")


