
from collections import deque
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_node(self.root, value)

    def _insert_node(self, current_node: Node, value: int) -> None:

        if current_node is None:
            return Node(value)
        
        if current_node.value > value:
            if current_node.left:
                self._insert_node(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif current_node.value < value:
            if current_node.right:
                self._insert_node(current_node.right, value)
            else:
                current_node.right = Node(value)
            
    def contains(self, value) -> bool:
        return self._recursive_contains(self.root, value)

    def _recursive_contains(self, current_node: Node, value: int) -> bool:
        if current_node is None:
            return False
        if current_node.value > value:
            return self._recursive_contains(current_node.left, value)
        elif current_node.value < value:
            return self._recursive_contains(current_node.right, value)
        elif current_node.value == value:
            return True

    def delete_node(self, value):
        self.root = self._delete_node(self.root, value)
    
    def _delete_node(self, current_node: Node, value: int):
        if current_node.value > value:
            current_node.left = self._delete_node(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self._delete_node(current_node.right, value)
        else:

            # removing a leaf node
            if (current_node.left is None and
                current_node.right is None):
                current_node = None
            # removing internal node with a left leaf
            elif current_node.right is None:
                current_node = current_node.left
            # removing internal node with a right leaf
            elif current_node.left is None:
                current_node = current_node.right
            # has left and right nodes
            else:
                min_right_value = self.min_value(current_node.right)
                current_node.value = min_right_value
                self._delete_node(current_node.right, min_right_value)

        return current_node

       
    def min_value(self, current_node: Node) -> int | None:
        if self.root is None:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def dfs(self) -> List:
        
        results = []

        def traverse(current_node: Node):

            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return results

        


