
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
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         arr = []
#         while head is not None:
#             arr.append(head.val)
#             head = head.next
        
#         mid = len(arr) // 2
#         for i in range(mid):
#             el1 = arr[i]
#             el2 = arr[-i-1]
#             if el1 != el2:
#                 return False
#         return True



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        s = list()
        curr = head
        while curr is not None:
            s.append(curr.val)
            curr = curr.next

        while len(s) > 0:
            el1 = s.pop()
            el2 = head.val
            head = head.next
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



node22 = ListNode(2)
head2 = ListNode(1, node22) # This is the head of the list

print("\n\ninitial list: ", end="")
print_list(head2)
s = Solution()
is_palidrome2 = s.isPalindrome(head2)
print(f"isPalindrome2: {is_palidrome2}")


