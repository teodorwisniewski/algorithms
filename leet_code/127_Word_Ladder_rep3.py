from typing import List
from collections import defaultdict, deque
from string import ascii_lowercase
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        neighbord_words = self.get_neighbor_words(beginWord, wordList)
        

        queue = deque([beginWord])
        level = 1
        word_length = len(beginWord)
        not_visited = set(wordList)

        while queue:

            for _ in range(len(queue)):
                current_word = queue.popleft()
                for idx in range(word_length):
                    pattern = current_word[:idx] + "*" + current_word[idx+1:] 
                    for neig in neighbord_words[pattern]:
                        if neig == endWord:
                            return level + 1
                        if neig in not_visited:
                            queue.append(neig)
                            not_visited.remove(neig)
            level += 1
        return 0

    def get_neighbor_words(self, beginWord, word_list):
        neighbord_words = defaultdict(list)

        for word in (word_list + [beginWord]):
            for idx in range(len(beginWord)):
                pattern = word[:idx] + "*" + word[idx+1:] 
                neighbord_words[pattern].append(word)
        return neighbord_words


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
res = sol.ladderLength(beginWord, endWord, wordList)
print(f"ladderLength {res}")

assert 5 == res