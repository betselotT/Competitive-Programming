# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def called(self, p : Optional[TreeNode], q: Optional[TreeNode]):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            left= self.called(p.left, q.right) 
            right = self.called(p.right, q.left)
            return left and right
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.called(root.left, root.right)