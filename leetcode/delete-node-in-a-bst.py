# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.val:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            right = root.right
            while right.left is not None:
                right = right.left
            root.val = right.val
            root.right = self.deleteNode(root.right, right.val)
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
