from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        ideas_set = set(ideas)
        res = 0
        
        while len(ideas)> 1:
            idea_a = ideas.pop(0)
            for idea_b in ideas:
                new_idea_a = idea_b[0] + idea_a[1:]
                if new_idea_a in ideas_set:
                    continue
                new_idea_b = idea_a[0] + idea_b[1:]
                if new_idea_b in ideas_set:
                    continue
                res += 2
        
        return res
            




sol = Solution()

ideas = ["coffee", 
         "donuts", 
         "time", 
         "toffee"]
res = sol.distinctNames(ideas)
print(f"distinctNames {res}")
assert res == 6

ideas = ["lack",
         "back"]
res = sol.distinctNames(ideas)
print(f"distinctNames {res}")
assert res == 0