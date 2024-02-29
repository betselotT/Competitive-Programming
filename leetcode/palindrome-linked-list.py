# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow
        if fast:
            right = right.next

        curr, prev = head, None
        while curr != slow:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while right and prev:
            if right.val != prev.val:
                return False
            right = right.next
            prev = prev.next
        
        return True