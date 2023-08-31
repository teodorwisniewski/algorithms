from typing import List
from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        if endWord not in words:
            return 0
        
        queue = deque([beginWord])
        n = len(beginWord)
        level = 1
        while queue:
            
            for _ in range(len(queue)):
                current_word = queue.popleft()
                for idx in range(n):
                    word_char = current_word[idx]
                    for ch in ascii_lowercase:
                        if ch == word_char:
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