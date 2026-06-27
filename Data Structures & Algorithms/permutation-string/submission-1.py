class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)

        if ls1 > ls2:
            return False
        
        fr = [0] * 26
        fc = [0] * 26

        for c in s1:
            fr[ord(c) - ord("a")] += 1
        
        cws = 0
        for i in range(ls2):
            fc[ord(s2[i]) - ord("a")] += 1
            cws += 1

            if cws > ls1:
                fc[ord(s2[i -ls1]) - ord("a")] -= 1
            
            if fc == fr:
                return True
        
        return False