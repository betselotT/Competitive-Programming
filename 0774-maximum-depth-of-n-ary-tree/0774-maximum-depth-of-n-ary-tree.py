#Python3 Code
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if len(root.children) == 0:
            return 1
        n = -1
        for node in root.children:
            n = max(n, self.maxDepth(node) + 1)
        return n