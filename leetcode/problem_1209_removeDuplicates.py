


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = [] # pair [ch, count]
        for ch in s:
            if stack and ch == stack[-1][0] and stack[-1][1] < k:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            if stack[-1][1] == k:
                stack.pop()
        
        stack = [
            cnt*ch for ch, cnt in stack
        ]

        return "".join(stack)



if __name__ == "__main__":
    s = "deeedbbcccbdaa"
    k = 3
    sol = Solution()
    ans = sol.removeDuplicates(s, k)
    print(f"removeDuplicates {ans}")
    assert ans == "aa"