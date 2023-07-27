
from typing import Optional


def print_list(node):
    while node is not None:
        print(node.val, end = " ")
        node = node.next




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



#  TC O(2n) SC O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        
        mid = len(arr) // 2
        for i in range(mid):
            el1 = arr[i]
            el2 = arr[-i-1]
            if el1 != el2:
                return False
        return True



# Creating the list [1, 2, 2, 1]
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2) # This is the head of the list

print("initial list: ", end="")
print_list(head)

s = Solution()
is_palidrome = s.isPalindrome(head)
print(f"isPalindrome: {is_palidrome}")
