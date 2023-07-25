from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)





class Solution:

    # TC O(n) SC O(n)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        arr_of_numbers: str = []

        def get_numbers_for_each_branch(arr_of_numbers, root, branch_number: str):

            if root is None:
                return None
            elif root.left is None and root.right is None:
                arr_of_numbers.append(branch_number + str(root.val))
            elif root.left is not None or root.right is not None:
                new_str_component = str(root.val)
                get_numbers_for_each_branch(arr_of_numbers, root.left,
                                            branch_number+new_str_component)
                get_numbers_for_each_branch(arr_of_numbers, root.right,
                                            branch_number+new_str_component)
        
        get_numbers_for_each_branch(arr_of_numbers, root, "")
        final_sum = 0
        for number_repr in arr_of_numbers:
            final_sum += int(number_repr)
        return final_sum


#   1
#  / \
# 2   3

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Call the function
print_tree(root)

s = Solution()
res = s.sumNumbers(root)
print(f"sumNumbers for input [1, 2, 3] is {res}")