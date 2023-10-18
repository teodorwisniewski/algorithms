from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq_len = len(nums) + 1
        frequency = {
            i: list()
            for i in range(freq_len)
        }
        for num, freq in counter.items():
            frequency[freq].append(num)

        res = []
        for freq in range(freq_len-1, 0, -1):
            for num in frequency[freq]:
                res.append(num)
            if len(res) >= k:
                return res
        
        

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
res = sol.topKFrequent(nums, k)
print(f"topKFrequent {res}")