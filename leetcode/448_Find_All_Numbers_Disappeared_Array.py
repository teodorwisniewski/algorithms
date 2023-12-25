class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set(nums)
        output = []
        for num in range(1,len(nums)+1):
            if num not in hash_set:
                output.append(num)
        return output