# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxim = -sys.maxsize # global maximum, initialized to a very low integer value
        def go(root):
            if not root: 
                return 0 # if there is no children, send 0 upward
            lh = go(root.left) # Max sum path of left children
            rh = go(root.right) # Max sum path of right children

            # updating global maximum considering all possibilities
            self.maxim = max(
                        lh+root.val, 
                        rh+root.val, 
                        lh+rh+root.val, 
                        self.maxim, 
                        root.val) 
            return max(max(lh,rh) + root.val, root.val) # sending the maximum upward
        go(root)
        return self.maxim
