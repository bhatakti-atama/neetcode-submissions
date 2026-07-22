# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_val: int = -101) -> int:
        if not root:
            return 0
        
        if root.val >= max_val:
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
        else:
            return self.goodNodes(root.left, max_val) + self.goodNodes(root.right, max_val)