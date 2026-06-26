class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = []
        pl = []

        prod = 1
        for num in nums:
            prod *= num
            pr.append(prod)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            pl.insert(0, prod)
        res = []
        for i in range(len(nums)):
            t = 1
            if i - 1 >= 0:
                t *= pr[i - 1]
            if i + 1 < (len(nums)):
                t *= pl[i + 1]
            res.append(t)
        return res