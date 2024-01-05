from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return None
        
#         if root.val > val:
#             return self.searchBST(root.left, val)
#         elif root.val < val:
#             return self.searchBST(root.right, val)
#         else:
#             return root
        

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        temp = root
        while root is not None:
            
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
