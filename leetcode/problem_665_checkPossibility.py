from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change = False
        for i in range(len(nums)-1):     
            if nums[i+1] >= nums[i]:
                continue
            if change:
                return False
            # [4,2,3]
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                # [5,7,1,8]
                nums[i+1] = nums[i]
            change = True

        return True

sol = Solution()
nums = [4,2,3]
res = sol.checkPossibility(nums)
print(f'checkPossibility {res}')
assert res
# nums = [4,2,1]
# res = sol.checkPossibility(nums)
# print(f'checkPossibility {res}')
# nums = [3,4,2,3]
# res = sol.checkPossibility(nums)
# print(f'checkPossibility {res}')
nums = [5,7,1,8]
res = sol.checkPossibility(nums)
print(f'checkPossibility {res}')

