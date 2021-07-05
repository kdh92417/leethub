class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        
        for i in range(1, len(nums)):
            dp.append(nums[i] + (dp[i -1] if dp[i - 1] > 0 else 0))
                
        return max(dp)
            
            