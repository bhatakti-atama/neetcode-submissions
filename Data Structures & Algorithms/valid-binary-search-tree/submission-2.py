# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValidBst(root: optional[TreeNode], min_val, max_val):
            if not root:
                return True
            
            if min_val < root.val < max_val:
                return checkValidBst(root.left, min_val, root.val) and checkValidBst(root.right, root.val, max_val)
            else:
                return False
        return checkValidBst(root, float("-inf"), float("inf"))