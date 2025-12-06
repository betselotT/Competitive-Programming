"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we can go for a recursive approach 
        # whenever we encounter a child node, we can just call 'flatten' on it 
        # and the resulting pointer will be of a linked list that we would then traverse to insert into the main list
        if not head:
            return None
        curr = head
        while curr:
            if curr.child:
                childList = self.flatten(curr.child)
                temp = curr.next
                if not temp:
                    curr.next = childList
                    childList.prev = curr
                    curr.child = None
                else:
                    curr.child = None
                    curr.next = childList
                    childList.prev = curr
                    temp2 = childList
                    while temp2.next:
                        temp2 = temp2.next
                    temp2.next = temp
                    temp.prev = temp2
            curr = curr.next
        return head