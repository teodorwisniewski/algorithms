from typing import List, Optional

# Definition for a binary tree node.

def print_tree(root):
    if not root:
        return

    # This queue will help us do a breadth-first traversal
    queue = [(root, 0)] # The second value in the tuple represents the level of the node
    current_level = 0

    while queue:
        node, level = queue.pop(0)

        # If we're entering a new level, print a newline
        if level != current_level:
            print()
            current_level = level

        # Print the node's value, or 'N' if it's None (to denote a missing node)
        print(node.val if node else 'N', end=' ')

        # If the current node is not None, add its children to the queue
        if node:
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        
        dp = {}

        def backtrack(left, right):

            if left > right:
                return [None]
            
            if (left, right) in dp:
                return dp[(left, right)]
            res = []
            for val in range(left, right+1):
                for left_tree in backtrack(left, val-1):
                    for right_tree in backtrack(val+1, right):
                        root = TreeNode(val, left_tree, right_tree)
                        res.append(root)
            dp[(left, right)] = res
            return res
        
       
        return  backtrack(1, n)
    


s = Solution()
res = s.generateTrees(3)
for tree in res:
    print_tree(tree)