
from data_structures.recursuve_binary_tree import BinarySearchTree

def test_insert_and_contains():
    bst = BinarySearchTree()
    values = [15, 10, 20, 8, 12, 16, 25]

    for val in values:
        bst.insert(val)

    for val in values:
        assert bst.contains(val) is True

    assert bst.contains(100) is False

def test_empty_tree():
    bst = BinarySearchTree()
    assert bst.contains(15) is False