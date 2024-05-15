


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        curr_node = self.root
        while curr_node:

            if curr_node.value == value:
                return False
            
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return True
                curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return True
                curr_node = curr_node.right

    def contains(self, value) -> bool:

        if self.root is None:
            return False

        curr_node = self.root
        while curr_node:

            if curr_node.value == value:
                return True
        
            if value < curr_node.value:
                if curr_node.left is None:
                    return False
                curr_node = curr_node.left

            else:
                if curr_node.right is None:
                    return False
                curr_node = curr_node.right
        
    def r_contains(self, value) -> bool:
        if self.root is None:
            return False
        return self._r_contains(self.root, value)
    
    def _r_contains(self, curr_node, value) -> bool:
        if curr_node is None:
            return False
        if value == curr_node.value:
            return True
        elif value < curr_node.value:
            return self._r_contains(curr_node.left, value)
        else:
            return self._r_contains(curr_node.right, value)


    def min_value(self, curr_node) -> int:
        
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node.value



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print('BST Contains 27:')
output = my_tree.contains(18)
assert output is True
print(output)

print('\nBST Contains 17:')
output = my_tree.contains(333)
assert output is not True
print(output)



print('BST Contains 27:')
output = my_tree.r_contains(27)
assert output is True
print(output)

print('\nBST Contains 17:')
output = my_tree.r_contains(17)
assert output is not True
print(output)


output = my_tree.min_value(my_tree.root)
assert output == 18
print(f"my_tree.min_value(my_tree.root)={output}")


output = my_tree.min_value(my_tree.root.right)
assert output == 52
print(f"my_tree.min_value(my_tree.root.right)={output}")