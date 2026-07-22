# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_val: int = -101) -> int:
        def dfs(node: TreeNode, max_val: float) -> int:
            if not node:
                return 0
            
            if node.val >= max_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, max_val) + dfs(node.right, max_val)
        
        return dfs(root, float('-inf'))