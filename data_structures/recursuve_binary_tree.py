



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
               
    def delete_node(self, value):
        return self.__delete_node(self.root, value)
    
    def __delete_node(self, current_node, value) -> Node:

        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)  
        else:
            # removing leaf node:
            if current_node.left is None and current_node.right is None:
                return None
            # removing parent node with only right children
            elif current_node.left is None:
                current_node = current_node.right
            # removing parent node with only right children
            elif current_node.right is None:
                current_node = current_node.left
            # removing parent node with two children nodes
            else:
                min_right_tree_value = self.min_value(current_node.right)
                current_node.value = min_right_tree_value
                current_node.right = self.__delete_node(current_node.right, min_right_tree_value)
        return current_node    

    def min_value(self, current_node):
        while current_node and current_node.left is not None:
            current_node = current_node.left
        return current_node.value