# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, o = "", ""
        def CreateList(arg):
            head = ListNode(arg[0])
            current=head
            for x in arg[1:]:
                node = ListNode(x)
                current.next = node
                current = current.next
            return head
        
        while l1:
            p+=str(l1.val)
            l1 = l1.next
        while l2:
            o+=str(l2.val)
            l2 = l2.next
        
        return CreateList(str(int(p)+int(o)))