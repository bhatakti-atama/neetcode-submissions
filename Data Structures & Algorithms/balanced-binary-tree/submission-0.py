# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkDepth(root: Optional[TreeNode]) -> tuple[bool,int]:
            if not root:
                return True, 0
            lb, ld = checkDepth(root.left)
            rb, rd = checkDepth(root.right)
            if lb and rb and abs(ld - rd) <= 1:
                return True, max(ld, rd) + 1
            else:
                return False, -1
        res,_ = checkDepth(root)
        return res