# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def calc(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            l = calc(left, mid - 1)
            r = calc(mid + 1, right)
            return TreeNode(nums[mid], l, r)
        return calc(0, len(nums) - 1)