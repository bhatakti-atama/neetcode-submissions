class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        while r > l:
            print(s[l], s[r])
            if s[r].isalnum() and s[l].isalnum():
                if s[r].lower() != s[l].lower():
                    return False
                r -= 1
                l += 1
            else:
                if not s[r].isalnum():
                    r -= 1
                if not s[l].isalnum():
                    l += 1
        return True