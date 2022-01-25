class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        elif self.dp[n]:
            return self.dp[n]
            
        self.dp[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dp[n]
        