class Solution:
    pow_num: int = 0
    
    def isPowerOfTwo(self, n: int) -> bool:
        if 2 ** self.pow_num > n:
            return False
        
        if 2 ** self.pow_num == n:
            return True
        
        self.pow_num +=1 
        
        return self.isPowerOfTwo(n)
