class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = collections.Counter(jewels)
        result = 0
        
        for i in stones:
            result += c[i]
            
        return result