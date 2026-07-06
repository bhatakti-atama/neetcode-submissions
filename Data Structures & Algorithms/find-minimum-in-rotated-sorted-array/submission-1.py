class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            p = (l + r) // 2
            if nums[p] > nums[r]:
                l = p + 1
            else:
                r = p
        return nums[l]