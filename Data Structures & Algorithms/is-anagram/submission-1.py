from string import ascii_lowercase
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_fmap = [0] * 26
        t_fmap = [0] * 26
        alphabet_map = dict(zip(ascii_lowercase, range(0, 26)))

        for c in s:
            s_fmap[alphabet_map[c]] += 1
        for c in t:
            t_fmap[alphabet_map[c]] += 1
        if s_fmap == t_fmap:
            return True
        else:
            return False