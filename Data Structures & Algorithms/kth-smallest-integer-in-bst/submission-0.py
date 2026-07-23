class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Returns a tuple of (found_value, current_count)
        def findKthSmallest(node: Optional[TreeNode], count: int) -> tuple[Optional[int], int]:
            if not node:
                return None, count
            
            val, count = findKthSmallest(node.left, count)
            
            if val is not None:
                return val, count
            
            count += 1
            if count == k:
                return node.val, count
            
            return findKthSmallest(node.right, count)

        val, _ = findKthSmallest(root, 0)
        return val