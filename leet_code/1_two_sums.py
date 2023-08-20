class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numbers:
                index_one = numbers[diff]
                index_two = i
                return [index_one, index_two]
            numbers[num] = i

