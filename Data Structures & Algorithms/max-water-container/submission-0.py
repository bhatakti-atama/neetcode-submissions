class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n -1
        max_vol = 0
        while l < r:
            curr_vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, curr_vol)

            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol