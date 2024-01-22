
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

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, curr_node: Node, value: int) -> Node:
        if curr_node is None:
            return Node(value)
        
        if curr_node.value > value:
            curr_node.left = self._insert(curr_node.left, value)
        elif curr_node.value < value:
            curr_node.right = self._insert(curr_node.right, value)

        return curr_node
    
    def contains(self, value) -> bool:
        if self.root is None:
            return False
        else:
            return self._contains(self.root, value)

    def _contains(self, curr_node: Node, value: int) -> bool:
        if curr_node is None:
            return False

        if curr_node.value > value:
            return self._contains(curr_node.left, value)
        elif curr_node.value < value:
            return self._contains(curr_node.right, value)
        else:
            return True
        
    def delete_node(self, value):
        if self.root is None:
            return
        else:
            self.root = self._delete_node(self.root, value)

    def _delete_node(self, curr_node: Node, value: int):
        if curr_node is None:
            return None
        if curr_node.value > value:
            curr_node.left = self._delete_node(curr_node.left, value)
        elif curr_node.value < value:
            curr_node.right = self._delete_node(curr_node.right, value)
        else:
            if (
                curr_node.left is None and
                curr_node.right is None
            ):
                return None
            elif curr_node.right is None:
                curr_node = curr_node.left
            elif curr_node.left is None:
                curr_node = curr_node.right
            else:
                min_right_value = self.min_value(curr_node.right)
                curr_node.value = min_right_value
                self._delete_node(curr_node.right, min_right_value)
        return curr_node

    def min_value(self, curr_node: Node) -> int:
        if curr_node is None:
            return
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.value
    
    def dfs_pre_order(self) -> List:

        results = []
        def traverse()



    
