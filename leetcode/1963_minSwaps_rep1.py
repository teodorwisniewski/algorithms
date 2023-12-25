



# TC O(n) SC O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        closed_nb = 0
        max_closed = 0
        for ch in s:
            if ch == "]":
                closed_nb += 1
            else:
                closed_nb -= 1
            max_closed = max(max_closed, closed_nb)
        return (max_closed+1)//2
            

    
# TC O(n) SC O(n)
# class Solution:
#     def minSwaps(self, s: str) -> int:
#         stack = []
#         for ch in s:
#             if stack and ch == "]":
#                 stack.pop()
#             else:
#                 stack.append(ch)
#         return (len(stack) + 1)//2


sol = Solution()
s = "][]["
res = sol.minSwaps(s)
print(f"minSwaps: {res}")

s = "]]][[["
res = sol.minSwaps(s)
print(f"minSwaps: {res}")