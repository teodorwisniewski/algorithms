
from typing import Optional, List

from collections import deque


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






class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root


# The BST is now created

class Solution:

    # TC O(n) SC O(n)
    def trimBST(self, root: Optional[TreeNode], low, high):
        
        if root is None:
            return None
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root


#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7

# Given values [4, 2, 6, 1, 3, 5, 7]
values = [4, 2, 6, 1, 3, 5, 7]

# Create the BST
root = None
for val in values:
    root = insert(root, val)


print("Structure of the BST:")
print_tree_structure(root)


s = Solution()
res = s.trimBST(root, 2, 6)
print("Solution")
print_tree_structure(res)