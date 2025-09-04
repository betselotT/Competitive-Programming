# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        st = [(original,cloned)]
        while st:
            a, b = st.pop()
            if a is target:
                return b
            if a.left:
                st.append((a.left,b.left))
            if a.right:
                st.append((a.right,b.right))