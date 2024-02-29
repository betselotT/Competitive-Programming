# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        aheadPtr = temp
        while n >= 0:
            aheadPtr = aheadPtr.next
            n -= 1
        behindPtr = temp
        while aheadPtr:
            behindPtr = behindPtr.next
            aheadPtr = aheadPtr.next
        if behindPtr and behindPtr.next:
            behindPtr.next = behindPtr.next.next
        return temp.next