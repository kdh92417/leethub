class Solution:
    def climbStairs(self, n: int) -> int:
        dp = { 1: 1, 2: 2}
        
        def fib(n):
            if n in dp:
                return dp[n]
            
            dp[n] = fib(n - 2) + fib(n - 1)
            return dp[n]
        
        return fib(n)