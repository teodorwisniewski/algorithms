
from typing import Optional, List

from collections import deque




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def print_tree_structure(root):
    if not root:
        return
    
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()  # Move to the next level after printing the current level





# TC O(2^n) SC O(n*2^n)
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        def create_tree_combs(res, leftTree, rightTree):
            for left_t in leftTree:
                for right_t in rightTree:
                    new_t_comb = TreeNode(left=left_t, right=right_t)
                    res.append(new_t_comb)

        def backtrack(n):

            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in cache:
                return cache[n]
            
            res = []
            for l in range(n):
                r = n - l - 1
                leftTree, rightTree = backtrack(l), backtrack(r)
                create_tree_combs(res, leftTree, rightTree)
            cache[n] = res
            return res

        return backtrack(n)
                





s = Solution()
res = s.allPossibleFBT(7)
assert 5 == len(res)
for i, possible_tree in enumerate(res):
    print(f"\nSolution {i+1}")
    print_tree_structure(possible_tree)

