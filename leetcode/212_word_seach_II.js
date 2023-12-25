
from typing import List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        
        for word in words:
            trie.insert_word(word)
        
        ROWS, COLS = len(board), len(board[0])
        found_words, visited_nodes = set(), set()

        def backtrack(row: int, col: int, node: TrieNode, word: str):
            
            
            is_invalid_letter_comb = (
                row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                board[row][col] not in node.children or
                (row, col) in visited_nodes
            )
            if is_invalid_letter_comb:
                return 
            letter = board[row][col]
            visited_nodes.add((row, col))
            word += letter
            next_node = node.children[letter]
            if next_node.is_word:
                found_words.add(word)
            
            for i in range(-1, 2, 2):
                backtrack(row+i, col, next_node, word)
                backtrack(row, col+i, next_node, word)
            visited_nodes.remove((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row, col, trie.root, "")

        return list(found_words)


board = [
    list("SIEE"),
    list("SFMS"),
    list("ONAE")
]
words = ["SIEMANO", "SIEMA", "EMA", "SIEMU", "ELO"]

s = Solution()

# Print the board
for row in board:
    print(' '.join(row))


# Print the word
print("words:", words)
print(f"findWords {s.findWords(board, words)}")





# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]