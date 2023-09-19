from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_val = -1
        for idx in reversed(range(len(arr))):
            new_max = max(max_val, arr[idx])
            arr[idx] = max_val
            max_val = new_max

        return arr
        


s = Solution()
arr = [17,18,5,4,6,1]
res = s.replaceElements(arr)
print(f"replaceElements {res}")
