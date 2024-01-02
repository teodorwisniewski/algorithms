
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    __slots__ = ["val", "next"]
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    

def to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge(l1, l2))
            lists = merged_lists
        return lists[0]


    def merge(self, l1, l2) -> List:

        dummy_head = ListNode()
        tail = dummy_head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next               
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy_head.next
        