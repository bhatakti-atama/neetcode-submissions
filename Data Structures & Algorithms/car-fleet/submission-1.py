class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = -1.0

        for p, s in cars:
            time_to_target = (target - p) / s
            
            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target
                
        return fleets