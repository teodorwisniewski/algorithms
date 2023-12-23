
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list from a list of values
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def read_linked_list(head):
    curr = head
    while curr is not None:
        print(f'Node {curr.val} ->')
        curr = curr.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


sol = Solution()
# Test input
head = create_linked_list([1, 2, 3, 4, 5])
res = sol.reverseList(head)
read_linked_list(res)