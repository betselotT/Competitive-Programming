# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def flatten(self, root: TreeNode | None) -> None:
    if not root:
      return
    self.flatten(root.left)
    self.flatten(root.right)
    left = root.left  
    right = root.right 
    root.left = None
    root.right = left
    rightmost = root
    while rightmost.right:
      rightmost = rightmost.right
    rightmost.right = right