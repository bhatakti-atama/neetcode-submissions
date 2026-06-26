class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        curr_len = 1
        max_len = 1

        l = 0
        r = 1
        
        chars = {s[0]}
        
        while r < n:
            if s[r] in chars:
                while s[l] != s[r]:
                    curr_len -= 1
                    chars.remove(s[l])
                    l += 1
                l += 1
                r += 1
            else:
                chars.add(s[r])
                r += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len