from typing import List
from collections import defaultdict, deque
from string import ascii_lowercase
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        words = set(wordList)
        queue = deque([beginWord])
        n = len(beginWord)
        level = 1

        while queue:
            
            for _ in range(len(queue)):
                current_word = queue.popleft()
                for idx in range(n):
                    original_ch = current_word[idx]
                    for ch in string.ascii_lowercase:
                        if original_ch == ch:
                            continue
                        new_word = current_word[:idx] + ch + current_word[idx+1:]
                        if new_word == endWord:
                            return level + 1
                        if new_word in words:
                            queue.append(new_word)
                            words.remove(new_word)
            level += 1
        return 0


    

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
res = sol.ladderLength(beginWord, endWord, wordList)
print(f"ladderLength {res}")

assert 5 == res