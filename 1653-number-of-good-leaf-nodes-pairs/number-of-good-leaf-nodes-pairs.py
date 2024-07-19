# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def check(node, distance):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = check(node.left, distance)
            right = check(node.right, distance)
            for i in left:
                if i > distance:
                    continue
                for j in right:
                    if i + j <= distance:
                        count +=1 
            return [k + 1 for k in left+right]

        count = 0
        if not root:
            return 0
        check(root, distance)
        return count