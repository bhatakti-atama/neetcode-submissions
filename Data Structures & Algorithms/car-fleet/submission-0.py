class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psp = []
        for i in range(len(position)):
            psp.append((position[i], speed[i]))
        psp.sort()
        psp.reverse()

        fleet = 0
        t = -1
        for car in psp:
            ct = (target - car[0]) / car[1] 
            if ct <= t:
                continue
            else:
                fleet += 1
                t = ct
            
        return fleet