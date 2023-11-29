from typing import List


# class Solution:
#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

#         left = 0
#         res = 0
#         window_sum = 0
#         window_size = 0
#         for num in arr:
#             if window_size == k:
#                 window_sum -= arr[left]
#                 left += 1
#                 window_size -= 1

#             window_size += 1
#             window_sum += num
            
#             if window_size == k and (window_sum/k) >= threshold:
#                 res += 1

#         return res
        


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window_sum = sum(arr[:k-1])
        for left in range(len(arr) - k + 1):
            window_sum += arr[left + k - 1]
            if (window_sum/k) >= threshold:
                res += 1
            window_sum -= arr[left]
        return res
        



sol = Solution()
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

res = sol.numOfSubarrays(arr, k, threshold)
print(f"numOfSubarrays {res}")