# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level):
            if not root:
                return
            myDict[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        myDict = defaultdict(list)
        res = []
        dfs(root, 0)

        for num in sorted(myDict):
            res.append(myDict[num][-1])

        return res