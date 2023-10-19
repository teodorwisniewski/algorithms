from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return set(nums)
        
        freq_len = len(nums) + 1
        counter = Counter(nums)
        frequencies = [[] for _ in range(freq_len)]

        for num, freq in counter.items():
            frequencies[freq].append(num)
        
        res = []
        for idx in range(freq_len-1, 0, -1):
            for num in frequencies[idx]:
                res.append(num)
            if len(res) >= k:
                return res
        return res
        

        

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
res = sol.topKFrequent(nums, k)
print(f"topKFrequent {res}")