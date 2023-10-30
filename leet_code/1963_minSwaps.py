


# class Solution:
#     def minSwaps(self, s: str) -> int:
#         close_cnt, max_close_cnt = 0, 0
#         for ch in s:
#             if ch == "[":
#                 close_cnt -= 1
#             else:
#                 close_cnt += 1
#             max_close_cnt = max(max_close_cnt, close_cnt)
#         return (max_close_cnt + 1)//2
    

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and ch == "]":
                stack.pop()
            else:
                stack.append(ch)
        return (len(stack) + 1)//2
        


sol = Solution()
s = "][]["
res = sol.minSwaps(s)
print(f"minSwaps: {res}")

s = "]]][[["
res = sol.minSwaps(s)
print(f"minSwaps: {res}")