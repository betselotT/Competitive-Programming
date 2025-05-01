# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, r: Optional[TreeNode], k: int) -> int:
        return (f:=lambda n:n and f(n.left)+[n.val]+f(n.right) or [])(r)[k-1]