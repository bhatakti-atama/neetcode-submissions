# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calcHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0, 0
        rh, rd = self.calcHeight(root.right)
        lh, ld = self.calcHeight(root.left)
        maxd = max(ld, rd, rh + lh)
        return 1 + max(rh, lh), maxd

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h, d = self.calcHeight(root)
        return d