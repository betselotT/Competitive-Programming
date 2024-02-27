# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif not head.next:
            return head
        left, right, temp = head, head.next, head.next.next
        head.next = None
        while right:
            right.next = left
            left = right
            right = temp
            if temp:
                temp = temp.next
        return left