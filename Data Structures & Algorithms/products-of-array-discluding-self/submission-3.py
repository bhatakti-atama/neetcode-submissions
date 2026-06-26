class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]

        prod = 1
        n = len(nums)
        for i in range(1,n):
            prod *= nums[i - 1]
            res.append(prod)
        prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res