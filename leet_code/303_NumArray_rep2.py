
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for num in nums:
            curr += num
            self.prefix.append(curr)
        
    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix[left-1] if left > 0 else 0
        right_sum = self.prefix[right]
        return right_sum - left_sum


        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(f"sumRange {param_1}")
param_2 = obj.sumRange(2,4)
print(f"sumRange {param_2}")