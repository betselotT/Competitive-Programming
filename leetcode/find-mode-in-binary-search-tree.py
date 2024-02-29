# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        myDict = defaultdict(int)
        def traverse(node):
            if node:
                myDict[node.val] += 1
                traverse(node.right)
                traverse(node.left)
        traverse(root)

        maximum = max(myDict.values())
        for key, value in myDict.items():
            if value == maximum:
                answer.append(key)
        return answer