



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
           self.root = Node(val)
        else:
            self._insert_node(self.root, val)
    
    def _insert_node(self, node: Node, val):
        if val < node.value:
            if node.left is not None:
                self._insert_node(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._insert_node(node.right, val)
            else:
                node.right = Node(val)

    def contains(self, val):
        return self.__recursive_contains(self.root, val)

    def __recursive_contains(self, node, val):
        if node is None:
            return False
        if node.value < val:
            return self.__recursive_contains(node.right, val)
        elif node.value > val:
            return self.__recursive_contains(node.left, val)
        else:
            return True
        return False
               
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
    def __delete_node(self, current_node: Node, value) -> Node:
        if current_node is None:
            return None
        
        if current_node.value > value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # removing a leaf node
            if current_node.left is None and current_node.right is None:
                return None
            # removing an internal node with a left node
            elif current_node.left is not None:
                return current_node.left
            # removing an internal node with a right node
            elif current_node.right is not None:
                return current_node.right
            # removing an internal node with a right and a left node
            else:
                min_value_right_leaf: int = self.min_value(current_node.right)
                # nadpisanie wartosci usuwanego wezla
                current_node.value = min_value_right_leaf
                self.__delete_node(current_node.right, min_value_right_leaf)
        return current_node
       
    def min_value(self, current_node) -> int:
        if current_node is None:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value