class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = []
        pl = []

        prod = 1
        n = len(nums)
        for num in nums:
            prod *= num
            pr.append(prod)
        prod = 1
        for i in range(n - 1, -1, -1):
            prod *= nums[i]
            pl.append(prod)
        pl.reverse()
        res = []
        for i in range(n):
            t = 1
            if i - 1 >= 0:
                t *= pr[i - 1]
            if i + 1 < (n):
                t *= pl[i + 1]
            res.append(t)
        return res