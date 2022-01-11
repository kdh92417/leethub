class Solution:
    def reverse(self, x: int) -> int:
        minus = ''
        
        if x < 0:
            minus = '-'

        x =  int(minus + str(abs(x))[::-1])
        
        if x < -2**31 or x > 2**31 -1:
            return 0
        
        return x
        
        
            
        