from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not n:
            return True 
        new_flowerbed = [0] + flowerbed + [0]
        for idx in range(1, len(new_flowerbed)-1):

            if (
                not new_flowerbed[idx-1] and
                not new_flowerbed[idx] and
                not new_flowerbed[idx+1]
            ):
                new_flowerbed[idx] = 1
                n -= 1
                if not n:
                    return True
        return False




sol = Solution()




flowerbed = [1,0,0,0,1]
n = 1
res = sol.canPlaceFlowers(flowerbed, n)
assert res


flowerbed = [1,0,0,0,1]
n = 2
res = sol.canPlaceFlowers(flowerbed, n)
assert not res
