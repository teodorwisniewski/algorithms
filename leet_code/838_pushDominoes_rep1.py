from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dom = list(dominoes)
        queue = deque()

        for idx, val in enumerate(dom):
            if val != ".":
                queue.append((idx, val))
        
        while queue:
            idx, domino = queue.popleft()
            if (
                domino == "L" and
                idx-1 >= 0 and
                dom[idx-1] == "."
            ):
                dom[idx-1] = "L"
                queue.append((idx-1, "L"))
            elif (
                domino == "R" and
                idx+1 < len(dom) and
                dom[idx+1] == "."
            ):
                if (
                    idx+2 < len(dom) and
                    dom[idx+2] == "L"
                ):
                    queue.popleft()
                else:
                    dom[idx+1] = "R"
                    queue.append((idx+1, "R"))

        return "".join(dom)


sol = Solution()
# dominoes = ".L.R...LR..L.."
# res = sol.pushDominoes(dominoes)
# print(f"res {res}")

dominoes = ".......L.L"
res = sol.pushDominoes(dominoes)
print(f"res {res}")


