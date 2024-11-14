# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        
        def dfs(node):
            if not node:
                return 0, 0  # return sum and count of nodes as 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate total sum and count for current subtree
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            # Check if average of current subtree (rounded down) equals the node's value
            if total_sum // total_count == node.val:
                self.cnt += 1
            
            return total_sum, total_count
        
        dfs(root)
        return self.cnt