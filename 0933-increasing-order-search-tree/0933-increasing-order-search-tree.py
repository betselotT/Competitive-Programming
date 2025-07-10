# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a=[]
        def po(node):
            if node is None:
                return
            po(node.left)
            a.append(node.val)
            po(node.right)
        po(root)
        r=TreeNode(a[0])
        curr=r
        for i in range(1,len(a)):
            curr.right=TreeNode(a[i])
            curr=curr.right
        return r


        