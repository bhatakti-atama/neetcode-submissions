class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n -1
        max_vol = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            curr_vol = min(h_l, h_r) * (r - l)
            max_vol = max(max_vol, curr_vol)

            if h_l < h_r:
                while l < r and heights[l] <= h_l:
                    l += 1
            else:
                while l < r and heights[r] <= h_r:
                    r -= 1
                
        return max_vol