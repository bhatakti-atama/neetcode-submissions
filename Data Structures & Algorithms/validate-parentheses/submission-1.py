class Solution:

    def isValid(self, s: str) -> bool:
        s1 = []
        for c in s:
            if c == "(" or c == "{" or c == "[" :
                s1.append(c)
            else:
                if len(s1) == 0:
                    return False
                else:
                    top = s1.pop()
                if c == ")" and top == "(":
                    continue
                if c == "}" and top == "{":
                    continue
                if c == "]" and top == "[":
                    continue
                else:
                    return False
        if len(s1) == 0:
            return True
        else:
            return False