from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        # O(n*w)
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*"  + word[idx+1:]
                nei[pattern].append(word)
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for idx in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neigb_word in nei[pattern]:
                        if neigb_word not in visited:
                            visited.add(neigb_word)
                            queue.append(neigb_word)
            res += 1

        return 0

    

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
res = sol.ladderLength(beginWord, endWord, wordList)
print(f"ladderLength {res}")

assert 5 == res