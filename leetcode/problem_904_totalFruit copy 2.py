from typing import List
from collections import Counter



        
class Solution:
    def totalFruit(self, fruits):
        left = 0
        bucket = Counter()
        res = 0
        for right, fruit in enumerate(fruits):
            bucket[fruit] += 1
            while len(bucket) > 2:
                left_fruit = fruits[left]
                bucket[left_fruit] -= 1
                if bucket[left_fruit] == 0:
                    del bucket[left_fruit]
                left += 1
            res = max(res, right-left+1)
        return res


  


sol = Solution()
fruits = [0, 1, 2, 2]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")


fruits = [1,2,1]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")