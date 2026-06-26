class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= l:
                l = char_index_map[char] + 1
            char_index_map[char] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len