# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        def call(root, low, high):
            nonlocal count
            if not root:
                return count
            if root.val >= low and root.val <= high:
                count += root.val
            call(root.left, low, high)
            call(root.right, low, high)
        call(root, low, high)
        return count