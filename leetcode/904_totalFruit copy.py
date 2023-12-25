from typing import List
from collections import Counter



        
class Solution:
    def totalFruit(self, fruits):

        max_fruit_size = 0
        fruits_counter = Counter()
        left = 0
        for right, fruit in enumerate(fruits):
            fruits_counter[fruit] += 1
            while len(fruits_counter) > 2:
                left_fruit = fruits[left]
                fruits_counter[left_fruit] -= 1
                if fruits_counter[left_fruit] == 0:
                    del fruits_counter[left_fruit]
                left += 1
            max_fruit_size = max(max_fruit_size, right - left + 1)
        return max_fruit_size


  


sol = Solution()
fruits = [0, 1, 2, 2]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")


fruits = [1,2,1]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")