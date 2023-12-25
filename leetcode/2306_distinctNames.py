from typing import List
from collections import defaultdict

# class Solution:
#     def distinctNames(self, ideas: List[str]) -> int:

#         ideas_set = set(ideas)
#         postfix_set = set()
#         res = 0
        
#         while len(ideas) > 1:
#             idea_a = ideas.pop(0)
#             postfix = idea_a[1:]
#             if postfix in postfix_set and len(idea_a) > 1:
#                 continue
#             else:
#                 postfix_set.add(postfix)
#             for idea_b in ideas:
#                 new_idea_a = idea_b[0] + postfix
#                 if new_idea_a in ideas_set:
#                     continue
#                 new_idea_b = idea_a[0] + idea_b[1:]
#                 if new_idea_b in ideas_set:
#                     continue
#                 res += 2
            
#         return res
            



class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        ideas_hash_map = defaultdict(set) # letters to -> sets of suffixes
        for w in ideas:
            ideas_hash_map[w[0]].add(w[1:])

        res = 0
        keys_to_iterate = list(ideas_hash_map.keys())

        for idx, ch1 in enumerate(keys_to_iterate):
            for idx_ch2 in range(idx+1, len(keys_to_iterate)):
                ch2 = keys_to_iterate[idx_ch2]

                intersection = len(ideas_hash_map[ch1].intersection(ideas_hash_map[ch2]))
                distinct1 = len(ideas_hash_map[ch1]) - intersection
                distinct2 = len(ideas_hash_map[ch2]) - intersection
                res += 2 * distinct1 * distinct2
                
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

ideas = ["wrbkfnhjw", "q", "i", "noysvsh", "p"]
res = sol.distinctNames(ideas)
print(f"distinctNames {res}")
assert res == 14