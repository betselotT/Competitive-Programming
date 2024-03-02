class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        def zigzag(node, level):
            if not node:
                return
            if len(arr) <= level:
                arr.append([])
            if level % 2 == 0:
                arr[level].append(node.val)
            else:
                arr[level].insert(0, node.val)
            zigzag(node.left, level + 1)
            zigzag(node.right, level + 1)
        
        zigzag(root, 0)
        return arr
