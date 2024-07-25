"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        dummy = Node(-1)
        new_list = dummy
        refs = {}
        while current:
            if not current in refs:        
                new_node = Node(current.val)
                refs[current] = new_node
                new_list.next = new_node
            else:
                new_list.next = refs[current]
            new_list = new_list.next
            if not current.random:
                new_list.random = None
            else:
                if (current.random in refs):
                    new_list.random = refs[current.random]
                else:
                    new_node = Node(current.random.val)
                    refs[current.random] = new_node
                    new_list.random = new_node 
            current = current.next
        return dummy.next