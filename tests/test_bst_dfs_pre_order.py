
from data_structures.dfs_pre_order_bfs import BinarySearchTree


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


# Test delete_node method
def test_delete_node():
    bst = BinarySearchTree()
    # Insert elements
    for value in [15, 10, 20, 8, 12, 17, 25]:
        bst.insert(value)

    # Delete a leaf node
    bst.delete_node(8)
    assert bst.contains(8) is False

    # Delete a node with one child
    bst.delete_node(20)
    assert bst.contains(20) is False
    
    assert bst.contains(15)

    # Delete a node with two children
    bst.delete_node(15)
    assert bst.contains(15) is False


def test_min_value():
    bst = BinarySearchTree()

    # Test with an empty tree
    assert bst.min_value(bst.root) is None

    # Insert elements and test
    for value in [15, 10, 20, 8, 12, 17, 25]:
        bst.insert(value)
    
    # Test with multiple nodes
    assert bst.min_value(bst.root) == 8

    # Test with a single node tree
    bst = BinarySearchTree()
    bst.insert(10)
    assert bst.min_value(bst.root) == 10


def test_dfs():
    bst = BinarySearchTree()

    # Insert elements and test
    for value in [47, 21, 76, 18, 27, 52, 82]:
        bst.insert(value)
    
    assert bst.dfs() == [47, 21, 18, 27, 76, 52, 82]
    