class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            p = (l + r) // 2
            if matrix[p][0] < target:
                l = p + 1
            elif matrix[p][0] > target:
                r = p - 1
            else:
                return True
                
        row = r 
        
        if row >= 0:
            l = 0
            r = len(matrix[row]) - 1
            
            while l <= r:
                p = (l + r) // 2
                if matrix[row][p] < target:
                    l = p + 1
                elif matrix[row][p] > target:
                    r = p - 1
                else:
                    return True
                    
        return False