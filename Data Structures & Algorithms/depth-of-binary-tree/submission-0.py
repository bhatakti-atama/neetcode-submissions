# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth
        
        ld, rd  = self.maxDepth(root.left), self.maxDepth(root.right)

        return max(ld, rd) + 1
