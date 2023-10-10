
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix_sums.append(curr)
        
    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sums[right]
        left_sum = self.prefix_sums[left-1] if left > 0 else 0
        return right_sum - left_sum

        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(f"sumRange {param_1}")
param_2 = obj.sumRange(2,4)
print(f"sumRange {param_2}")