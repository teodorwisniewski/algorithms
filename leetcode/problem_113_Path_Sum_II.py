from typing import List, Optional



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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        if not root:
            return []

        def backtrack(path, total, current_node):
            
            leave_cond = current_node.left is None and current_node.right is None
            if leave_cond and total == targetSum:
                res.append(list(path))
                return

            if leave_cond:
                return
            
            # if targetSum < 0 and total > 0:
            #     return
            
            if current_node.left is not None:
                node_val = current_node.left.val
                path.append(node_val)
                total += node_val
                backtrack(path, total, current_node.left)
                path.pop()
                total -= node_val

            if current_node.right is not None:
                node_val = current_node.right.val
                path.append(node_val)
                total += node_val
                backtrack(path, total, current_node.right)
                path.pop()
                total -= node_val


        node_val = root.val
        path = []
        path.append(node_val)
        total = node_val
        backtrack(path, total, root)
        return res
            



# Binary Tree 1:
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1

root1 = TreeNode(5)
root1.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root1.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))

s = Solution()
res = s.pathSum(root1, 18)
print(f"pathSum {res}")


# Binary Tree 2:
#        1
#          \
#           2

root2 = TreeNode(1, TreeNode(2))
res = s.pathSum(root2, 1)
print(f"pathSum {res}")

# Binary Tree 2:
#        -2
#          \
#           -3

# root2 = TreeNode(-2, TreeNode(-4), TreeNode(-3))
# res = s.pathSum(root2, -6)
# print(f"pathSum {res}")
