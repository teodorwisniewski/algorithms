
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        # creating dummy indexes
        self.dummy_head = Node(0)
        self.dummy_tail = Node(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    # O(n)
    def get(self, index: int) -> int:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if self._is_valid_node_for_get_method(curr, index):
            return curr.value
        return -1
        
    def _is_valid_node_for_get_method(self, curr_node: Node, index) -> bool:
        return (
            curr_node is not Node and
            curr_node != self.dummy_tail and
            index == 0
        )

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        next = self.dummy_head.next
        self.dummy_head.next = new_head
        next.prev = new_head
        new_head.next = next
        new_head.prev = self.dummy_head
        
    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        prev = self.dummy_tail.prev
        prev.next = new_tail
        self.dummy_tail.prev = new_tail
        new_tail.prev = prev
        new_tail.next = self.dummy_tail
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            new_node = Node(val)
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0 and curr != self.dummy_tail:
            next = curr.next
            prev = curr.prev
            next.prev = prev
            prev.next = next


# Create a new linked list
linked_list = MyLinkedList()

# Add elements to the head
linked_list.addAtHead(1)
linked_list.addAtHead(2)
assert linked_list.get(0) == 2
assert linked_list.get(1) == 1

# Add elements to the tail
linked_list.addAtTail(3)
assert linked_list.get(2) == 3

# Add element at a specific index
linked_list.addAtIndex(1, 4)
assert linked_list.get(1) == 4
assert linked_list.get(2) == 1

# Delete an element
linked_list.deleteAtIndex(1)
assert linked_list.get(1) == 1

# Print the list
curr = linked_list.dummy_head.next
while curr != linked_list.dummy_tail:
    print(curr.value, end=" -> ")
    curr = curr.next
print("NULL")