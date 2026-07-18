class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            t = b
            b =  a + b
            a = t
        return b
        