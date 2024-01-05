



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
        
        temp = self.root
        new_node = Node(val)
        while True:
            if temp.value == new_node.value:
                return False
            # go left
            if temp.value > new_node.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right         

    def contains(self, value) -> bool:
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            # go left
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right   
        return False
    