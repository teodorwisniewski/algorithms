


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def backtrack(node, paths, path):
            if node is None:
                return
            if len(path) == 0:
                path = str(node.val)
            else:
                path = path + '->' + str(node.val)
            path = path 
            if node.left is None and node.right is None:
                paths.append(path)
            else:
                backtrack(node.left, paths, path)
                backtrack(node.right, paths, path)

        paths = []
        initial_path = ''
        backtrack(root, paths, initial_path)
        return paths

