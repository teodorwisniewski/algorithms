
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         s = []
#         curr = head
#         while curr is not None:
#             s.append(curr.val)
#             curr = curr.next
        
#         curr = head
#         while len(s) > 0:
#             if curr.val != s.pop():
#                 return False
#             curr = curr.next
#         return True





class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # find middle node
        slow = self.find_middle_node(head)
        # reverse from midle
        right = self.reverse_from_middle(slow)
        # comapre two lists
        left = head
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True
    

    def find_middle_node(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_from_middle(self, curr_node):
        prev = None
        while curr_node:
            tmp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = tmp
        return prev
    

def print_list(node):
    while node is not None:
        print(node.val, end = " ")
        node = node.next







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


