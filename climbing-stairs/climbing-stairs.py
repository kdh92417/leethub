class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        a, b = 1, 2
        
        for i in range(n - 1):
            a, b = b, a+b
            
        return a
        
        