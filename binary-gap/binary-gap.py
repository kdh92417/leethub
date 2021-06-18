class Solution:
    def binaryGap(self, n: int) -> int:
        pre = dis = 0
        
        for i, v in enumerate(bin(n)[2:]):
            if v == "1":
                dis = max(dis, i-pre)
                pre = i
                
        return dis    
            