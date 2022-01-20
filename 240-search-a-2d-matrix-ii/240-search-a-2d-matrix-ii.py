class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i, r in enumerate(matrix):
            if r[-1] >= target:
                b_idx = bisect.bisect_left(r, target)
                if r[b_idx] == target: return True 
            else:
                continue
            
        return False
                
                
            
            