# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oddHead, evenHead = ListNode(0), ListNode(0)
        oddTail, evenTail = oddHead, evenHead
        isOdd = True

        while head:
            if isOdd:
                oddTail.next = head
                oddTail = oddTail.next
            else:
                evenTail.next = head
                evenTail = evenTail.next
            isOdd = not isOdd
            head = head.next
        
        oddTail.next = evenHead.next
        evenTail.next = None

        return oddHead.next