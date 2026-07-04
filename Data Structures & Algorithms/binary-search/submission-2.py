class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            p = (r + l) // 2
            if nums[p] < target:
                l = p + 1
            elif nums[p] > target:
                r = p - 1
            else:
                return p
        return -1