



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val) -> bool:
        if self.root is None:
            self.root = Node(val)
            return True
        return self.recursive_insert(self.root, val)

    def recursive_insert(self, node, value):
        if node is None:
            return Node(value)
        if node.value > value:
            node.left = self.recursive_insert(node.left, value)
        elif node.value < value:
            node.right = self.recursive_insert(node.right, value)
        return node

    def contains(self, val):
        return self.__recursive_contains(self.root, val)

    def __recursive_contains(self, node, val):
        if node is None:
            return False
        if node.value == val:
            return True
        if node.value > val:
            return self.__recursive_contains(node.left, val)
        else:
            return self.__recursive_contains(node.right, val)
               
            