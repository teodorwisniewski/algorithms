from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:   

        current_node = head
        new_head = None
        prev = None
        while current_node:
            if new_head is None and current_node.val != val:
                new_head = current_node
            if current_node.val == val and new_head is not None:
                prev.next = current_node.next
                current_node.next = None
                current_node = prev.next
            else:
                prev = current_node
                current_node = prev.next

        return new_head



def print_list(node):
    while node is not None:
        print(node.val, end = " ")
        node = node.next




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating the list [1, 2, 6, 4, 5, 5, 6]
node7 = ListNode(6)
node6 = ListNode(5, node7)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(6, node4)
node2 = ListNode(2, node3)
head = ListNode(6, node2) # This is the head of the list

print("initial list: ", end="")
print_list(head)

s = Solution()
cleaned_list = s.removeElements(head, 6)
print("removeElements: ", end="")
print_list(cleaned_list)



node44 = ListNode(7)
node33 = ListNode(7, node44)
node22 = ListNode(7, node33)
head2 = ListNode(7, node22) # This is the head of the list

print("\n\ninitial list: ", end="")
print_list(head2)
s = Solution()
cleaned_list = s.removeElements(head2, 7)
print("removeElements: ", end="")
print_list(cleaned_list)

