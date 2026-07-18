class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        if n > 1:
            dp[1] = 1
            for i in range(n - 1):
                dp[i + 1] += dp[i]
                if i + 2 < n:
                    dp[i + 2] += dp[i]
        return dp[-1]
        