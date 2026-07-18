class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = nums[1]
            for i in range(n - 2):
                for j in range(i + 2, n):
                    dp[j] = max(dp[j], dp[i] + nums[j])
        return max(dp)