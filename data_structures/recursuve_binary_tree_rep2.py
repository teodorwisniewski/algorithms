



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.__insert_recursive(self.root, value)

    def __insert_recursive(self, node: TreeNode, value):

        if node.value > value and node.left:
            self.__insert_recursive(node.left, value)
        elif node.value < value and node.right:
            self.__insert_recursive(node.right, value)
        else:
            if node.value > value:
                node.left = TreeNode(value)
            else: 
                node.right = TreeNode(value)

    def contains(self, value) -> bool:
        return self.__contains(self.root, value)
    
    def __contains(self, node: TreeNode, value) -> bool:
        if node is None:
            return False
        
        if node.value > value and node.left:
            return self.__contains(node.left, value)
        elif node.value < value and node.right:
            return self.__contains(node.right, value)
        elif node.value == value:
            return True
        return False
    
    def min_value(self, current_node: TreeNode) -> int:
        if current_node is None:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def delete_node(self, value: int):
        self.__delete_node(self.root, value)

    def __delete_node(self, current_node: TreeNode, value) -> int:

        if current_node is None:
            return 
        
        if current_node.value > value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if (current_node.left is None and
                current_node.right is None):
                return None
            elif current_node.right is None:
                current_node = current_node.left
            elif current_node.left is None:
                current_node = current_node.right
            else:
                min_right_value = self.min_value(current_node.right)
                current_node.value = min_right_value
                self.__delete_node(current_node.right, min_right_value)
        
        return current_node



