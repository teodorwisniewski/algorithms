# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive implementation
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         results = []
#         def _preorder_traversal(node):

#             if node is None:
#                 return

#             results.append(node.val)
#             if node.left:
#                 _preorder_traversal(node.left)
#             if node.right:
#                 _preorder_traversal(node.right)
        
#         _preorder_traversal(root)
#         return results

# iterative implementation

# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         results = []
        
#         stack = [root]
#         while stack:
#             curr_node = stack.pop()
#             results.append(curr_node.val)

#             if curr_node.right:
#                 stack.append(curr_node.right)
#             if curr_node.left:
#                 stack.append(curr_node.left)
#         return results
    

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, stack = root, []
        results = []
        while curr or stack:
            if curr:
                results.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return results