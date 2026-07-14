class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pt = []
        res = []
        for i in range(len(temperatures) -1, -1, -1):
            while pt and pt[-1][1] <= temperatures[i]:
                pt.pop()
            
            if pt:
                res.append(pt[-1][0] - i)
            else:
                res.append(0)

            pt.append([i, temperatures[i]])
        res.reverse()
        return res