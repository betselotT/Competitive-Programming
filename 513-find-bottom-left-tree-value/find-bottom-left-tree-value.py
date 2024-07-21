# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=[]
        return bfs(root,queue)

def bfs(root,queue):
    if root != None:
        queue.append(root)
    while len(queue):
        k = queue.pop(0)
        if k.right != None:
            queue.append(k.right)
        if k.left != None:
            queue.append(k.left)
        
    return k.val

        