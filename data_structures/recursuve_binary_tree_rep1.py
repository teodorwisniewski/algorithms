



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
    
    def __delete_node(self, current_node, value) -> Node:
        pass 

    def min_value(self, current_node):
        pass