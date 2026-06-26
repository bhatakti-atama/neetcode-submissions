class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        p = 0
        res = set()
        while p < n - 2:
            l = p + 1
            r = n -1
            while l < r:
                currSum = nums[p] + nums[l] + nums[r]
                if currSum == 0:
                    res.add((nums[p], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
            p += 1
        res_list = [list(item) for item in res]
        return res_list