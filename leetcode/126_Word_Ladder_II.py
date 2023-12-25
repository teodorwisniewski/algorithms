from typing import List, Dict
from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList:
            return []
        self.n = len(beginWord)
        neig_words_mapping = self.find_neighbors(beginWord, wordList)

        queue = deque([[beginWord]])
        res = []

        visited = set()

        shortest_path = float("inf")
        while queue:
            current_layer_words = set()
            for _ in range(len(queue)):
                current_list = queue.popleft()
                current_word = current_list[-1]
                if current_word == endWord:
                    new_path_len = len(current_list)
                    if new_path_len > shortest_path:
                        return res
                    shortest_path = new_path_len
                    res.append(current_list)

                for idx in range(self.n):
                    prefix = current_word[:idx] + "*" + current_word[idx+1:]
                    for neigh_word in neig_words_mapping[prefix]:
                     
                        
                        if neigh_word not in visited:
                            queue.append(current_list + [neigh_word])         
                            current_layer_words.add(neigh_word)    
            visited.update(current_layer_words)      
        return res
        
    
    def find_neighbors(self, beginWord, wordList) -> Dict:

        neig_words_mapping = defaultdict(list)
        for word in wordList:
            if beginWord == word:
                continue
            for idx in range(self.n):
                prefix = word[:idx] + "*" + word[idx+1:]
                neig_words_mapping[prefix].append(word)
        return neig_words_mapping

    
        

sol = Solution()

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]


# res = sol.findLadders(beginWord, endWord, wordList)
# print(f"findLadders {res}")

# assert 5 == len(res[0])


beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
res = sol.findLadders(beginWord, endWord, wordList)
print(f"findLadders {res}")