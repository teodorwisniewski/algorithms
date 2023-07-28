


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        curr = head
        while curr is not None:
            s.append(curr.val)
            curr = curr.next
        
        curr = head
        while len(s) > 0:
            if curr.val != s.pop():
                return False
            curr = curr.next
        return True
