from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next



# O (max(m,n))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_l = None
        head = None
        remain = 0
        while l1 is not None or l2 is not None:

            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            new_val = val1 + val2 + remain
            remain = 0
            if new_val > 9:
                new_val = new_val % 10
                remain = 1
            if new_l is None:
                head = ListNode(new_val)
                new_l = head
            else:
                new_l.next = ListNode(new_val)
                new_l = new_l.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if remain:
            new_l.next = ListNode(remain)

        return head









def create_linked_list(values):
    dummy_head = ListNode()
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Creating the linked lists l1 and l2
l1_values = [2, 4, 3]
l2_values = [5, 6, 4]

# Creating the linked lists l1 and l2
# l1_values = [9,9,9,9,9,9,9]
# l2_values = [9,9,9,9]

l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

s = Solution()
output = s.addTwoNumbers(l1, l2)

print_linked_list(output)