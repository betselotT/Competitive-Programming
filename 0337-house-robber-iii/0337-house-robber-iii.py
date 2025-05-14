# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mp={}
        def fun(r):
            if not r:
                return 0
            if r in mp:
                return mp[r]
            rc=r.val
            if r.left:
                rc+=fun(r.left.left) + fun(r.left.right)
            if r.right:
                rc+=fun(r.right.left) + fun(r.right.right)
            lc=fun(r.left)+fun(r.right)
            mp[r]=max(rc,lc)
            return mp[r]
        return fun(root)