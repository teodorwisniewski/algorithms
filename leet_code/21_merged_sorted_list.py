from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(m+n)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         if list1 is None and list2 is not None:
#             merged_head = list2
#             list2 = list2.next
#         elif list1 is not None and list2 is None:
#             merged_head = list1
#             list1 = list1.next        
#         elif list1 is None and list2 is None:
#             return None
#         elif list1.val < list2.val:
#             merged_head = list1
#             list1 = list1.next
#         else:
#             merged_head = list2
#             list2 = list2.next

#         merged_node = merged_head
#         while list1 is not None and list2 is not None:
#             if list1.val < list2.val:
#                 merged_node.next = list1
#                 merged_node = merged_node.next
#                 list1 = list1.next
#             else:
#                 merged_node.next = list2
#                 merged_node = merged_node.next
#                 list2 = list2.next
#         if list1 is None:
#             while list2 is not None:
#                 merged_node.next = list2
#                 merged_node = merged_node.next
#                 list2 = list2.next
#         if list2 is None:
#             while list1 is not None:
#                 merged_node.next = list1
#                 merged_node = merged_node.next
#                 list1 = list1.next
#         return merged_head



# TC  O(n) SC O(n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None: return list2
        if list2 is None: return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def print_list(node):
    while node is not None:
        print(node.val, end = " ")
        node = node.next
    print()







# Creating the first list [1, 2, 4]
list1_node1 = ListNode(4)
list1_node2 = ListNode(2, list1_node1)
list1 = ListNode(1, list1_node2) # This is the head of the first list

# Creating the second list [1, 3, 4]
list2_node1 = ListNode(4)
list2_node2 = ListNode(3, list2_node1)
list2 = ListNode(1, list2_node2) # This is the head of the second list


# Now let's print our lists
print("List 1: ", end="")
print_list(list1)

print("List 2: ", end="")
print_list(list2)

s = Solution()
merged_list = s.mergeTwoLists(list1, list2)
print("merged_list: ", end="")
print_list(merged_list)


# Creating the first list [-9,3]
list1_node1 = ListNode(3)
list3 = ListNode(-9, list1_node1) # This is the head of the first list

# Creating the second list [5,7]
list2_node1 = ListNode(7)
list4 = ListNode(5, list2_node1) # This is the head of the second list


# Now let's print our lists
print("\n\nList 3: ", end="")
print_list(list3)

print("List 4: ", end="")
print_list(list4)


s = Solution()
merged_list = s.mergeTwoLists(list3, list4)
print("merged_list: ", end="")
print_list(merged_list)
