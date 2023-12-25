


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            cs = numbers[left] + numbers[right]
            if cs < target:
                left += 1
            elif cs > target:
                right -= 1
            elif cs == target:
                return [left+1, right+1]
        return []


s = Solution()
numbers = [2,7,11,15]
target = 9
res = s.twoSum(numbers, target)
print(f"twoSum {res}")