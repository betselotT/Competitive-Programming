# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeHead = ListNode(0)
        before = beforeHead
        afterHead = ListNode(0)
        after = afterHead

        temp = head
        while temp:
            if temp.val < x:
                before.next = temp
                before = before.next
            else:
                after.next = temp
                after = after.next
            temp = temp.next
        
        after.next = None
        before.next = afterHead.next

        return beforeHead.next